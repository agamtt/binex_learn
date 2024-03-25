// Name: ret64.c
// Compile: gcc -o ret64 ret64.c -fno-stack-protector -z execstack -no-pie

#include <stdio.h>


int main() {
  char buf[200];
  printf("buf : %p\n",buf);
  scanf("%s", buf);
  printf("your input : %s\n",buf);

  return 0;
}
