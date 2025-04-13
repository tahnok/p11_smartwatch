SERVICE_UUID = "be940000-7333-be46-b7ae-689e71722bd5"
UUID = "be940001-7333-be46-b7ae-689e71722bd5"
UUID_BULK = "be940003-7333-be46-b7ae-689e71722bd5"

ADDRESS = "EE:13:93:CE:C3:24"

import commands as c
import parser

from enum import IntEnum
from dataclasses import dataclass
import asyncio

from bleak import BleakClient
from bleak.backends.characteristic import BleakGATTCharacteristic


def crc16_compute(data: bytearray) -> tuple[int, int]:
    """
    Compute a custom 16-bit checksum of input data.

    This function implements a specific checksum variant that includes
    byte swapping and multiple XOR operations with shifted values.

    Args:
        data (bytearray): Input data bytes to calculate checksum for

    Returns:
        tuple[int, int]: A tuple containing (low_byte, high_byte) of the CRC value
                         Each byte is in the range 0-255
    """
    crc_value = (
        0xFFFF  # Initialize with all bits set (equivalent to -1 in signed 16-bit)
    )

    for byte in data:
        # Swap high and low bytes of current CRC value
        high_byte = (crc_value >> 8) & 0xFF
        low_byte_shifted = (crc_value << 8) & 0xFF00
        crc_value = low_byte_shifted | high_byte

        # XOR with current data byte
        crc_value ^= byte & 0xFF

        # XOR with the lower byte shifted right by 4 bits
        xor_value = (crc_value & 0xFF) >> 4
        crc_value ^= xor_value

        # Double shift operation and XOR
        shifted_value = (crc_value << 8) << 4
        crc_value ^= shifted_value & 0xFFFF

        # Final transformation for this iteration
        final_shift = ((crc_value & 0xFF) << 4) << 1
        crc_value ^= final_shift

        # Ensure we maintain a 16-bit value
        crc_value &= 0xFFFF

    # Extract and return the low and high bytes
    low_byte = crc_value & 0xFF
    high_byte = (crc_value >> 8) & 0xFF

    return (low_byte, high_byte)


def make_packet(
    command: c.Command | int, subCommand: IntEnum | int, data: bytearray
) -> bytearray:
    length = len(data) + 6
    result = bytearray(length)

    # Set header bytes
    result[0] = command & 0xFF
    result[1] = subCommand & 0xFF
    result[2] = length & 0xFF
    result[3] = (length >> 8) & 0xFF

    result[4 : 4 + len(data)] = data

    l, h = crc16_compute(result[: length - 2])
    result[-2] = l
    result[-1] = h

    return result


@dataclass
class Packet:
    dataType: int
    command: c.Command
    subCommand: IntEnum | int
    length: int
    crc: int
    data: bytearray


def raw_to_packet(raw: bytearray) -> Packet:
    dataType = int.from_bytes(raw[0:2])
    command, subCommand = c.parse_dataType(dataType)
    length = int.from_bytes(raw[2:4], byteorder="little")
    crc = int.from_bytes(raw[-2:])
    data = raw[4:-2]
    return Packet(dataType, command, subCommand, length, crc, data)


def hex_to_packet(raw: str) -> Packet:
    return raw_to_packet(bytearray.fromhex(raw))


import base64


def b64_to_packet(raw: str) -> Packet:
    return raw_to_packet(bytearray(base64.b64decode(raw)))


# not working
HEART_RATE_MEASURE = make_packet(
    c.Command.CONTROL, c.Control.START_MEASUREMENT, bytearray(b"\x01\x00")
)  # 815

GET_DEVICE_INFO_PACKET = make_packet(
    c.Command.GET, c.Get.DEVICE_INFO, bytearray([71, 67])
)  # 512

GET_DEVICE_SUPPORT_PACKET = make_packet(
    c.Command.GET, c.Get.SUPPORT_FUNCTION, bytearray([71, 70])
)

GET_DEVICE_NAME_PACKET = make_packet(
    c.Command.GET, c.Get.DEVCIE_NAME, bytearray([71, 80])
)

START_ECG_PACKET = make_packet(
    c.Command.CONTROL, c.Control.BLOOD_TEST, bytearray([2])
)  # 770

SOMETHING_ECG_START = make_packet(
    c.Command.CONTROL, c.Control.WAVE_UPLOAD, bytearray([1, 1])
)  # 779

SOMETHING_ECG_START_2 = make_packet(
    c.Command.CONTROL, c.Control.REAL_DATA, bytearray([1, 3, 2])
)  # 777


SOMETHING_ECG_START_3 = make_packet(
    c.Command.CONTROL, c.Control.WAVE_UPLOAD, bytearray([1, 0])
)  # 779


# hacky wait until we get a packet before sending next
event = asyncio.Event()

GET_PARSERS = {
        c.Get.DEVICE_INFO: parser.parse_device_info,
        c.Get.SUPPORT_FUNCTION: parser.parse_features,
        c.Get.DEVCIE_NAME: parser.parse_name,
    }

def callback(char: BleakGATTCharacteristic, data: bytearray):
    event.set()
    print(f"{char.uuid} rx: {data.hex()}")
    p = raw_to_packet(data)
    print(p)
    if p.command == c.Command.GET:
        if p.subCommand in GET_PARSERS:
            print(GET_PARSERS[p.subCommand](p.data))


async def main():
    print("Connecting")
    # I think this is to start a heart rate measure
    packets = [GET_DEVICE_NAME_PACKET, GET_DEVICE_INFO_PACKET, GET_DEVICE_SUPPORT_PACKET]
    #packets = [START_ECG_PACKET, SOMETHING_ECG_START, SOMETHING_ECG_START_2, SOMETHING_ECG_START_3]
    async with BleakClient(ADDRESS) as client:
        print("Connected")
        service = client.services.get_service(SERVICE_UUID)
        assert service
        char = service.get_characteristic(UUID)
        assert char
        await client.start_notify(char, callback)

        await client.start_notify(UUID_BULK, callback)

        for packet in packets:
            event.clear()
            print(f"sending {packet.hex()}")
            x = await client.write_gatt_char(char, packet, response=True)
            print(f"immediate response {x}")
            await event.wait()
        for _ in range(250):
            await asyncio.sleep(1)
            print(".")


if __name__ == "__main__":
    asyncio.run(main())
