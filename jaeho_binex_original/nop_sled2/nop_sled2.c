// gcc -o nop_sled2 nop_sled2.c -fno-stack-protector -z execstack -no-pie

#include <stdio.h>
#include <unistd.h>

int main(){
    char buf[0x256];
    scanf("%s", buf);
    printf("%s\n",buf);
    return 0;
}