from pwn import *

byte_string = b'\x01\x02\x03\x04\x05\x06\x07\x08'
print(data)

# 이 데이터를 64비트 정수로 변환
value = u64(byte_string)
print(value)

print(hex(value))