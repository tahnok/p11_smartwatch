SERVICE_UUID = "be940000-7333-be46-b7ae-689e71722bd5"
UUID = "be940001-7333-be46-b7ae-689e71722bd5"
UUID_BULK = "be940003-7333-be46-b7ae-689e71722bd5"

ADDRESS = "EE:13:93:CE:C3:24"

import asyncio
from bleak import BleakClient
from bleak.backends.characteristic import BleakGATTCharacteristic


def callback(char: BleakGATTCharacteristic, data: bytearray):
    print(f"{char.uuid} rx: {data}")

async def main():
    print("Connecting")
    packet = bytes.fromhex("030207000264b7")
    async with BleakClient(ADDRESS) as client:
        print("Connected")
        service = client.services.get_service(SERVICE_UUID)
        assert service
        char = service.get_characteristic(UUID)
        assert char
        await client.start_notify(char, callback)

        await client.start_notify(UUID_BULK, callback)

        print("sending")
        x = await client.write_gatt_char(char, packet, response=True)
        print(x)
        while True:
            await asyncio.sleep(5)
            print(".")

asyncio.run(main())
