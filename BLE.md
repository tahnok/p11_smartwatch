
First device has an address: `EE:13:93:CE:C3:24`

SmartWear supports a few different "product ids"

- 1078
- 30737
- 30738
- 1178
- 1278
- 1378

it also looks for a 

from ScanResult (from android bluetooth). 

There's 2 gatt writes? `gatt2WriteData` and `gattWriteData`. Implies 2 write gatt services, which makes sense, there's the nordic one and the other one.

`be940001-7333-be46-b7ae-689e71722bd5` is the first one

`be940002-7333-be46-b7ae-689e71722bd5` is the second one... they're identical?

Eventually those are both called by `sendData2Device`

Python equivalent from claude

```python
def send_data_to_device(i2: int, data: bytes) -> bytes:
    # Calculate total length (data + 6 bytes for header and CRC)
    length = len(data) + 6
    
    # Create new byte array
    result = bytearray(length)
    
    # Set header bytes (i2 value and length)
    result[0] = (i2 >> 8) & 0xFF
    result[1] = i2 & 0xFF
    result[2] = length & 0xFF
    result[3] = (length >> 8) & 0xFF
    
    # Copy data bytes
    data_length = length - 6
    result[4:4 + data_length] = data
    
    # Calculate position for CRC
    crc_pos = data_length + 4
    
    # Calculate CRC16
    crc16 = ByteUtil.crc16_compute(result[:length - 2])  # Assuming ByteUtil is available
    
    # Set CRC bytes
    result[crc_pos] = crc16 & 0xFF
    result[crc_pos + 1] = (crc16 >> 8) & 0xFF
    
    return bytes(result)
```

So, the first 2 bytes are a "packet type", then 2 bytes of length. Next we have the actual data to send. Finally we have 2 bytes of crc16.


I think we want to look at `YCBTClient` as the place that does most of the send / receive stuff.

## ECG

1541 is the "date type" for ecg data maybe?

```
ecgMeasure: {"code":0,"data":[-1104,-880,-667,-496,-399,-386,-448,-570,-719,-857,-939,-921,-770,-460,6,599,1259,1908,2455,2840,3013,2974,2736,2348,1860,1323,777,242,-272,-764,-1237,-1676,-2069,-2397,-2633,-2755,-2744,-2601,-2342,-2001,-1629,-1295,-1052,-937,-952,-1069,-1221,-1327,-1326,-1191,-950,-698,-564,-654,-1032,-1655,-2384,-2969],"dataType":1541,"originalData":[7586,7550,8995,4105,2144,6002,4862,4574,7488,6653,6467,6762,6814,5786,5328,5515,7100,6869,4440,6596,6850,4501,976,2366,1743,-1354,1899,4000,-1079,-428,4175,2613,-852,-403,1400,-1213,-2881,-4692,-1125,-1074,3296,1023,-3707,-270,972,2882,1854,-3524,-1169,-1797,-259,263,-939,-770,117,1556,3660,704]}
```