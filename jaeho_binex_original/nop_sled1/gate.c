// gcc -o gate gate.c -m32 -fno-stack-protector -z execstack -no-pie
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    char buffer[256];
    if(argc < 2){
        printf("argv error\n");
        exit(0);
    }
    strcpy(buffer, argv[1]);	// 크기에 제한 없이 buffer에 argv[1]의 값 복사
    printf("%s\n", buffer);
}