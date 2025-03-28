from client import crc16_compute, make_packet

def test_crc16_compute():
    assert crc16_compute(bytearray(b'\x03\x02\x07\x00\x02')) == (0x64, 0xb7)

def test_make_packet():
    assert make_packet(0x0302, bytearray(b'\x02')) == bytearray(b'\x03\x02\x07\x00\x02\x64\xb7')
