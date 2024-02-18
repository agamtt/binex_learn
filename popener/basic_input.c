// basic_input.c

#include <stdio.h>

int main(){
	char buf[128];
	printf("Program Started!\n");
	gets(buf);
	printf("Your Input : %s\n",buf);

	return 0;
}
