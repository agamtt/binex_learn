// Name: basic000.c
// Compile: gcc -o basic000 basic000.c -fno-stack-protector -z execstack -no-pie -m32

#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>


void alarm_handler() {
    puts("TIME OUT");
    exit(-1);
}


void initialize() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    signal(SIGALRM, alarm_handler);
    alarm(30);
}


int main(int argc, char *argv[]) {

    char buf[0x80];					// 128 Byte 크기의 문자열 변수 선언

    initialize();
    
    printf("buf = (%p)\n", buf);	// buf의 주소 출력
    scanf("%141s", buf);			// buf에 141 Byte 크기의 문자열을 입력받음

    return 0;
}