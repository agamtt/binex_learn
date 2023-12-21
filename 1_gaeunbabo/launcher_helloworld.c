// gcc -o shellcode2 -fno-stack-protector -z execstack --no-pie -m32 shellcode2.c
#include<stdio.h>

void main()
{
	unsigned char shellcode [] = "\xeb\x15\x59\x31\xc0\xb0\x04\x31\xdb\xb3\x01\x31\xd2\xb2\x0f\xcd\x80\xb0\x01\x31\xdb\xcd\x80\xe8\xe6\xff\xff\xffHello, world!\n\r";
    	(*(void(*)()) shellcode)(); // pointer 연산으로 함수로써 참조하여 실행한다.(함수포인터로 형변환)
}
