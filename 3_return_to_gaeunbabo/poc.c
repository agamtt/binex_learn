// gcc -o poc -fno-stack-protector -z execstack --no-pie -m32 poc.c
#include <stdio.h>
#include <unistd.h>

void vuln(){
	char buf[50];
	printf("buf[50] address : %p\n",buf);
	read(0, buf, 100);
	printf("your input : %s\n",buf);
}
void main(){
	vuln();
}
