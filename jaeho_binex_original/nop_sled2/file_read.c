// gcc -o file_read file_read.c -fno-stack-protector -z execstack -no-pie

#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main(){
    char buf[0x256];
    FILE* file = fopen("data","r");
    size_t bytesRead = fread(buf, 1, 0x512, file);
    printf("%s\n",buf);

    fclose(file);

    FILE* new_file = fopen("new_data","w");
    size_t bytesWritten = fwrite(buf, 1, bytesRead, new_file);
    fclose(new_file);

    return 0;
}