//gcc -m32 -o poc32 poc.c -fno-stack-protector
//gcc -o poc64 poc.c -fno-stack-protector

#include <unistd.h>
#include <stdio.h>

int main(){
	char buf[8];
	printf("&buf : %p\n",&buf);
	read(0,buf,32);
	return 0;
}

