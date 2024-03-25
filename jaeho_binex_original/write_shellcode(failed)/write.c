// gcc -fno-stack-protector -o write write.c 
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    char filename[] = "new_file.txt";
    char buffer[] = "Hello, world!";

    int fd = open(filename, O_CREAT | O_WRONLY, 0666);

    if (write(fd, buffer, sizeof(buffer)) == -1) {
        perror("write");
        exit(EXIT_FAILURE);
    }
    close(fd);

    return 0;
}
