from pwn import *

p = process('./vuln')

p.interactive()
