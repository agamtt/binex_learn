from pwn import *

# 바이너리 파일을 엽니다.
with open("bin_hello", "rb") as file:
    binary_data = file.read()

# 바이너리 데이터를 \xXX 형식의 문자열로 변환합니다.
exploit = "".join("\\x{:02x}".format(b) for b in binary_data)

print(exploit)

