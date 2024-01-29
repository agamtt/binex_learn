from pwn import *

context.arch = 'amd64'

assembly_code = """
push 0x0a
mov rax, 0x21646c726f57202c
push rax
mov rax, 0x6f6c6c6548
push rax

mov rax, 1
mov rdi, 1
mov rsi, rsp
mov rdx, 13
syscall

mov rax, 60
xor rdi, rdi
syscall
"""

shellcode = asm(assembly_code)
print(shellcode)

with open('hello_hex','wb') as f:
    f.write(shellcode)

print(shellcode)