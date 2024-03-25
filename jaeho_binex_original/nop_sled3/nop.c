// gcc -o nop nop.c -fno-stack-protector -z execstack -no-pie

#include <stdio.h>
#include <string.h>

int vuln(char* src){
    char buf[32] = {};
    strcpy(buf, src);
    return 0;
}

int main(int argc, char* argv[], char* environ[]){
    vuln(argv[1]);
    return 0;
}