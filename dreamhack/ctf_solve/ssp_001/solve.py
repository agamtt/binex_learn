from pwn import *

p = process('./ssp_001')

p.sendafter(b'> ',b'F')
p.sendafter(b' : ',b'Hello World')

p.interactive()