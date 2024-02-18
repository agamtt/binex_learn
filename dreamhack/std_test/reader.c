#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>

int main() {
    int pipe_fd[2];
    pid_t pid;
    char buf[1024];
    int read_bytes;

    // 파이프 생성
    if (pipe(pipe_fd) == -1) {
        perror("pipe");
        exit(EXIT_FAILURE);
    }

    // 자식 프로세스 생성
    pid = fork();
    if (pid == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    } else if (pid == 0) {
        // 자식 프로세스에서 실행
        
        // 파이프의 쓰기 끝 닫기
        close(pipe_fd[1]);
        
        // 파이프의 읽기 끝을 표준 입력으로 복제
        dup2(pipe_fd[0], STDIN_FILENO);
        close(pipe_fd[0]);

        // 외부 프로그램 실행
        execl("./basic_input", "basic_input", (char *)NULL);
        // execl이 성공적으로 실행되면, 이 아래 코드는 실행되지 않음
        perror("execl");
        exit(EXIT_FAILURE);
    } else {
        // 부모 프로세스에서 실행
        
        // 파이프의 읽기 끝 닫기
        close(pipe_fd[0]);

        // 자식 프로세스에 데이터 쓰기
        write(pipe_fd[1], "Hello, child process!\n", 22);
        
        // 파이프의 쓰기 끝 닫기
        close(pipe_fd[1]);

        // 자식 프로세스가 종료될 때까지 대기
        wait(NULL);
    }

    return EXIT_SUCCESS;
}
