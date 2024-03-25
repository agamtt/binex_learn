// gcc -o bof bof.c -fno-stack-protector -z execstack -no-pie

#include <stdio.h>
#include <unistd.h>

int main(){
    char buf[0x256];
    scanf("%s", buf);
    printf("%s\n",buf);
    return 0;
}