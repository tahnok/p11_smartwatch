from bleak import BleakClient
import asyncio
import struct

UUID_WRITE = "be940001-7333-be46-b7ae-689e71722bd5"
UUID_NOTIFY = "be940002-7333-be46-b7ae-689e71722bd5"


def calculate_crc16(data, length):
    crc = 0xFFFF
    for i in range(length):
        crc = ((crc << 8) & 0xFF00) | ((crc >> 8) & 0x00FF)
        crc ^= data[i] & 0xFF
        crc ^= (crc & 0xFF) >> 4
        crc ^= (crc << 8) << 4
        crc ^= ((crc & 0xFF) << 4) << 1
    return crc & 0xFFFF


def notification_handler(sender, data):
    """Handle incoming PPG data"""
    if len(data) < 6:
        return

    cmd_id = (data[0] << 8) | data[1]
    length = (data[3] << 8) | data[2]

    if cmd_id == 0x0604:  # Real PPG data
        ppg_data = data[4:-2]  # Remove header and CRC
        # Process raw PPG data...
        print(f"Got PPG data: {ppg_data.hex()}")


async def start_ppg(client):
    # Command to start PPG
    device_type = 0
    sample_type = 1
    cmd = struct.pack(">BBBB", 0x03, 0x09, device_type, sample_type)

    # Add length and CRC
    length = len(cmd) + 6
    header = struct.pack(">HH", 0x0309, length)
    full_cmd = header + cmd
    crc = calculate_crc16(full_cmd, len(full_cmd))
    full_cmd += struct.pack("<H", crc)

    await client.write_gatt_char(UUID_WRITE, full_cmd)


async def main():
    client = BleakClient("EE:13:93:CE:C3:24")
    try:
        await client.connect()
        await client.start_notify(UUID_NOTIFY, notification_handler)
        await start_ppg(client)
        await asyncio.sleep(30)  # Get data for 30 seconds
    finally:
        await client.disconnect()


asyncio.run(main())
