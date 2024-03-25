// gcc -o ummtoshop ummtoshop.c -fno-stack-protector -z execstack -no-pie

#include <stdio.h>
#include <string.h>
#include <unistd.h>

int photo(char* buf){
    char va[900];
    strcpy(va, buf);

    FILE* new_file = fopen("new_data","w");
    size_t bytesWritten = fwrite(va, 1, 1000, new_file);
    fclose(new_file);

    return 0;
}

int main(){
    char buf[1000];
    FILE* file = fopen("data","r");
    size_t bytesRead = fread(buf, 1, 1000, file);
    fclose(file);

    printf("%s\n",buf);

    vuln(buf);

    return 0;
}