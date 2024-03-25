// ubuntu 18.04
// gcc -m32 -o ret ret.c -z execstack -fno-stack-protector -no-pie -z relro

#include <stdio.h>

void vuln()
{
        char buf[10];

        printf("input : ");
        scanf("%s", buf);

        printf("%s\n", buf);
}

void success()
{
        printf("success!\n");
}

int main()
{
        vuln();
        return;
}