#include <stdio.h>
#include <string.h>

int main(void)
{
    unsigned char code[] = "\xeb\x15\x59";

    printf("Shellcode length: %d\n", strlen(code));

    void (*s)() = (void *)code;
    s();

    return 0;
}