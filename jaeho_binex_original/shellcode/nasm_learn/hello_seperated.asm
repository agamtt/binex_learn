BITS 32

global _start

_start:
    ; 이곳에 명령어 작성
    call helloworld

helloworld:
    ; 이곳에서 데이터를 사용하는 명령어 작성
    mov eax, 4
    mov ebx, 1
    mov ecx, hello
    mov edx, 15
    syscall
    ; ...

section .data
hello db "Hello, World!",0x0a,0x0d
