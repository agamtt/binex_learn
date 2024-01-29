BITS 32

call helloworld
db "Hello, World!",0x0a,0x0d

helloworld:
    pop ecx
    mov eax, 4
    mov ebx, 1
    mov edx, 15
    syscall

    mov eax,1
    mov ebx,0
    syscall