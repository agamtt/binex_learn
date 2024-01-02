//gcc -o t t.c -fno-stack-protector -no-pie
//gcc -m32 -march=i386 -o i386_t t.c -fno-stack-protector -no-pie

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

    char buf[0x80];

    initialize();
    
    printf("buf = (%p)\n", buf);
    scanf("%141s", buf);

    return 0;
}
