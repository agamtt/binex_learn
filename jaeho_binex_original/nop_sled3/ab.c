// gcc -o ab ab.c

#include <stdio.h>

int main() {
    FILE *file = fopen("example.txt", "w"); // "w" 모드로 파일을 열거나 생성합니다.

    fprintf(file, "Hello, world!\n");

    fclose(file);

    return 0;
}