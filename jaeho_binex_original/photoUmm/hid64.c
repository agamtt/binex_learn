// Name: hid64.c
// Compile: gcc -o hid64 hid64.c -fno-stack-protector -no-pie

#include <stdio.h>
#include <string.h>
#include <unistd.h>

int hidden_function() {
  printf("Hello, Im Hidden!\n");
  return 0;
}
int vuln(char* buf){
    char va[200];
    strcpy(va, buf);

    FILE* new_file = fopen("new_data","w");

    fwrite(va, 1, 200, new_file);

    fclose(new_file);

    return 0;
}

int main(){
    char buf[256];
    FILE* file = fopen("data","r");
    fread(buf, 1, 256, file);
    fclose(file);

    printf("%s\n",buf);

    vuln(buf);

    return 0;
}