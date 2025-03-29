SERVICE_UUID = "be940000-7333-be46-b7ae-689e71722bd5"
UUID = "be940001-7333-be46-b7ae-689e71722bd5"
UUID_BULK = "be940003-7333-be46-b7ae-689e71722bd5"

ADDRESS = "EE:13:93:CE:C3:24"

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


def make_packet(kind: int, data: bytearray) -> bytearray:
    length = len(data) + 6
    result = bytearray(length)

    # Set header bytes (kind and length)
    result[0] = (kind >> 8) & 0xFF
    result[1] = kind & 0xFF
    result[2] = length & 0xFF
    result[3] = (length >> 8) & 0xFF

    result[4 : 4 + len(data)] = data

    l, h = crc16_compute(result[: length - 2])
    result[-2] = l
    result[-1] = h

    return result


def parse_device_info(b_arr: bytearray) -> dict:
    result = {}
    result["code"] = 0

    device_id = (b_arr[0] & 0xFF) + ((b_arr[1] & 0xFF) << 8)
    sub_version = b_arr[2] & 0xFF
    main_version = b_arr[3] & 0xFF
    battery_state = b_arr[4] & 0xFF
    battery_value = b_arr[5] & 0xFF
    bind_state = b_arr[6] & 0xFF
    sync_state = b_arr[7] & 0xFF

    version_str = f"{main_version}.{sub_version}"

    # Create data dictionary
    data = {
        "deviceId": device_id,
        "deviceVersion": version_str,
        "deviceBatteryState": battery_state,
        "deviceBatteryValue": battery_value,
        "deviceMainVersion": main_version,
        "deviceSubVersion": sub_version,
        "devicetBindState": bind_state,
        "devicetSyncState": sync_state,
    }

    hardware_type = 0

    # Process additional data if available
    if len(b_arr) >= 24:
        ble_agreement_sub_version = b_arr[8] & 0xFF
        ble_agreement_main_version = b_arr[9] & 0xFF
        blood_algo_sub_version = b_arr[10] & 0xFF
        blood_algo_main_version = b_arr[11] & 0xFF
        tp_sub_version = b_arr[12] & 0xFF
        tp_main_version = b_arr[13] & 0xFF
        blood_sugar_sub_version = b_arr[14] & 0xFF
        blood_sugar_main_version = b_arr[15] & 0xFF
        ui_sub_version = b_arr[16] & 0xFF
        ui_main_version = b_arr[17] & 0xFF
        hardware_type = b_arr[18] & 0xFF

        # Add additional data to dictionary
        data.update(
            {
                "bleAgreementSubVersion": ble_agreement_sub_version,
                "bleAgreementMainVersion": ble_agreement_main_version,
                "bloodAlgoSubVersion": blood_algo_sub_version,
                "bloodAlgoMainVersion": blood_algo_main_version,
                "tpSubVersion": tp_sub_version,
                "tpMainVersion": tp_main_version,
                "bloodSugarSubVersion": blood_sugar_sub_version,
                "bloodSugarMainVersion": blood_sugar_main_version,
                "uiSubVersion": ui_sub_version,
                "uiMainVersion": ui_main_version,
                "hardwareType": hardware_type,
            }
        )

    data["hardwareType"] = hardware_type

    # Build final result
    result["dataType"] = 512
    result["data"] = data

    return result


GET_DEVICE_INFO = 512
APP_START_MEASURE = 815

# not working
HEART_RATE_MEASURE = make_packet(APP_START_MEASURE, bytearray(b"\x01\x00"))

GET_DEVICE_INFO_PACKET = make_packet(GET_DEVICE_INFO, bytearray([71, 67]))


def callback(char: BleakGATTCharacteristic, data: bytearray):
    print(f"{char.uuid} rx: {data.hex()}")
    dataType = int.from_bytes(data[0:2])
    if dataType == GET_DEVICE_INFO:
        print(
            parse_device_info(data[4:])
        )  # trim dataType, length, probably should trim crc as wel...


async def main():
    print("Connecting")
    # I think this is to start a heart rate measure
    packets = [GET_DEVICE_INFO_PACKET]
    async with BleakClient(ADDRESS) as client:
        print("Connected")
        service = client.services.get_service(SERVICE_UUID)
        assert service
        char = service.get_characteristic(UUID)
        assert char
        await client.start_notify(char, callback)

        await client.start_notify(UUID_BULK, callback)

        for packet in packets:
            print(f"sending {packet.hex()}")
            x = await client.write_gatt_char(char, packet, response=True)
            print(f"immediate response {x}")
        for _ in range(2):
            await asyncio.sleep(1)
            print(".")


if __name__ == "__main__":
    asyncio.run(main())
