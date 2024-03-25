// gcc -o bof bof.c -m32 -fno-stack-protector -z execstack -no-pie

#include <stdio.h>
#include <unistd.h>

int main(){
    char buf[0x256];
    read(0, buf, 0x512);
    printf("%s\n",buf);
    return 0;
}