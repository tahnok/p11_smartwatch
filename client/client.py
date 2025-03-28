SERVICE_UUID = "be940000-7333-be46-b7ae-689e71722bd5"
UUID = "be940001-7333-be46-b7ae-689e71722bd5"
UUID_BULK = "be940003-7333-be46-b7ae-689e71722bd5"

ADDRESS = "EE:13:93:CE:C3:24"

import asyncio

from bleak import BleakClient
from bleak.backends.characteristic import BleakGATTCharacteristic


def callback(char: BleakGATTCharacteristic, data: bytearray):
    print(f"{char.uuid} rx: {data.hex()}")

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
    crc_value = 0xFFFF  # Initialize with all bits set (equivalent to -1 in signed 16-bit)
    
    for byte in data:
        # Swap high and low bytes of current CRC value
        high_byte = (crc_value >> 8) & 0xFF
        low_byte_shifted = (crc_value << 8) & 0xFF00
        crc_value = low_byte_shifted | high_byte
        
        # XOR with current data byte
        crc_value ^= (byte & 0xFF)
        
        # XOR with the lower byte shifted right by 4 bits
        xor_value = (crc_value & 0xFF) >> 4
        crc_value ^= xor_value
        
        # Double shift operation and XOR
        shifted_value = (crc_value << 8) << 4
        crc_value ^= (shifted_value & 0xFFFF)
        
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

    result[4:4 + len(data)] = data

    l,h = crc16_compute(result[:length - 2])
    result[-2] = l
    result[-1] = h

    return result

APP_START_MEASURE = 815

async def main():
    print("Connecting")
    # I think this is to start a heart rate measure
    packets = [make_packet(APP_START_MEASURE, bytearray(b'\x00\x01'))]
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
        for _ in range(10):
            await asyncio.sleep(1)
            print(".")

asyncio.run(main())
