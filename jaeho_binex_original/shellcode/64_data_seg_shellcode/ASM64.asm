section .data
	msg db "hello, world",0x0a,0x0d

section .text
	global _start

_start:
	mov rax,1
	mov rdi,1
	mov rsi,msg
	mov rdx,14
	syscall
	
	mov rax, 60
	mov rdi, 0
	syscall
