from client import crc16_compute, make_packet, parse_device_info


def test_crc16_compute():
    assert crc16_compute(bytearray(b"\x03\x02\x07\x00\x02")) == (0x64, 0xB7)


def test_make_packet():
    assert make_packet(0x03, 0x02, bytearray(b"\x02")) == bytearray(
        b"\x03\x02\x07\x00\x02\x64\xb7"
    )


def test_parse_device_info():
    raw = bytearray.fromhex("75000601005b000100030000000001000000000008000000")

    expected = {
        "code": 0,
        "dataType": 512,
        "data": {
            "deviceId": 117,
            "deviceVersion": "1.6",
            "deviceBatteryState": 0,
            "deviceBatteryValue": 91,
            "deviceMainVersion": 1,
            "deviceSubVersion": 6,
            "devicetBindState": 0,
            "devicetSyncState": 1,
            "bleAgreementSubVersion": 0,
            "bleAgreementMainVersion": 3,
            "bloodAlgoSubVersion": 0,
            "bloodAlgoMainVersion": 0,
            "tpSubVersion": 0,
            "tpMainVersion": 0,
            "bloodSugarSubVersion": 1,
            "bloodSugarMainVersion": 0,
            "uiSubVersion": 0,
            "uiMainVersion": 0,
            "hardwareType": 0,
        },
    }

    assert parse_device_info(raw) == expected
