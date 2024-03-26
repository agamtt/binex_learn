// Name: photoDot.c
// Compile: gcc -o photoDot photoDot.c -fno-stack-protector -no-pie

#include <stdio.h>
#include <string.h>
#include <unistd.h>

int hidden_function() {
  printf("YOU ARE ADMIN...\n");
  return 0;
}
int vuln(char* buf){
    char va[400];
    strcpy(va, buf);

    int i;
    for(i = 0; i < 400; i++) {
      
      if(va[i]=='\x45'){
        break;
      }

      if(va[i] != '\x20' && va[i] != '\x0A') {
      va[i] = '.';
      }
      printf("%c",va[i]);
    }
    printf("\n\n");

    return 0;
}

int main(){
    char buf[512];
    FILE* file = fopen("data","r");
    fread(buf, 1, 512, file);
    fclose(file);

    vuln(buf);

    return 0;
}