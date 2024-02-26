from pwn import *

data = b'\x01\x02\x03\x04\x05\x06\x07\x08'

print(u64(data))
print(hex(u64(data)))
print(p64(u64(data)))