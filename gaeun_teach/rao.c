#include <stdio.h>

void hidden_function(){
  printf("Hello, Im Hidden!\n");
}

int main(){
  char buf[0x28];
  printf("Input: ");
  scanf("%s",buf);
  printf("your input : %s\n",buf);

  return 0;
}
