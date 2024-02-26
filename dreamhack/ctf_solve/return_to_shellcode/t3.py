from pwn import *

context.arch = "i386"
print(shellcraft.sh())

context.arch = "mips"
print(shellcraft.sh())

context.arch = "amd64"
print(shellcraft.sh())

#print(''.join(f'\\x{byte:02x}' for byte in asm(shellcraft.sh())))
