// gcc -o reader_until reader_until.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

#define BUFFER_SIZE 1024

int main() {
    int pipe_stdin[2], pipe_stdout[2];
    pid_t pid;
    char buffer[BUFFER_SIZE];
    int read_bytes;
    char *output = NULL;
    size_t output_size = 0;

    // 두 쌍의 파이프 생성
    if (pipe(pipe_stdin) == -1 || pipe(pipe_stdout) == -1) {
        perror("pipe");
        exit(EXIT_FAILURE);
    }

    pid = fork();
    if (pid == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    } else if (pid == 0) { // 자식 프로세스
        // 부모로부터의 입력을 받기 위한 파이프 준비
        close(pipe_stdin[1]);
        dup2(pipe_stdin[0], STDIN_FILENO);
        
        // 부모에게 출력을 보내기 위한 파이프 준비
        close(pipe_stdout[0]);
        dup2(pipe_stdout[1], STDOUT_FILENO);
        
        // 외부 프로그램 실행
        execl("./basic_input", "basic_input", (char *)NULL);
        perror("execl");
        exit(EXIT_FAILURE);
    } else { // 부모 프로세스
        close(pipe_stdin[0]);
        close(pipe_stdout[1]);

        // 자식 프로세스의 출력 읽기
        while ((read_bytes = read(pipe_stdout[0], buffer, BUFFER_SIZE - 1)) > 0) {
            buffer[read_bytes] = '\0'; // NULL-terminate the string
            char *found = strstr(buffer, "Started");
            if (found != NULL) {
                // "stop" 단어가 발견되면 출력을 저장하고 루프 종료
                size_t stop_length = found - buffer;
                output = realloc(output, output_size + stop_length + 1);
                memcpy(output + output_size, buffer, stop_length);
                output_size += stop_length;
                output[output_size] = '\0';
                break;
            } else {
                // 아직 "stop" 단어가 발견되지 않았다면 계속 읽기
                output = realloc(output, output_size + read_bytes + 1);
                memcpy(output + output_size, buffer, read_bytes);
                output_size += read_bytes;
                output[output_size] = '\0';
            }
        }
        close(pipe_stdout[0]);
        
        // 자식 프로세스가 종료될 때까지 대기
        wait(NULL);

        printf("Received output until 'Started':\n%s\n", output);
        free(output);
    }

    return EXIT_SUCCESS;
}