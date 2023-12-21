//gcc -fno-stack-protector -o test test.c

#include <stdio.h>
#include <unistd.h>

void vuln(){
}
void main(){
	vuln();
}
