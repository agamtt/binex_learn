BITS 32

call helloworld
db "Hello, world!",0x0a,0x0d

helloworld:
	pop ecx
	mov eax, 4
	mov ebx, 1
	mov edx, 15
	int 0x80

	mov eax,1
	mov ebx,0
	int 0x80
