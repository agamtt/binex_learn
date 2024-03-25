// Name: hid64.c
// Compile: gcc -o hid hid.c -fno-stack-protector -no-pie

#include <stdio.h>

int hidden_function() {
  printf("Hello, Im Hidden!\n");
  return 0;
}

int main() {
  char buf[0x28];

  printf("Input: ");
  scanf("%s", buf);
  printf("your input : %s\n",buf);

  return 0;
}
