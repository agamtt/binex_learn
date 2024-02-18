#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    FILE *fp;
    const char *executable = "./basic_input"; // 실행할 파일의 경로

    // 실행 파일을 실행하고, 표준 입력을 통해 데이터를 전송할 수 있는 파이프를 엽니다.
    // "w"는 쓰기 모드입니다.
    fp = popen(executable, "w");
    if (fp == NULL) {
        fprintf(stderr, "실행 파일을 실행할 수 없습니다.\n");
        return EXIT_FAILURE;
    }

    // 실행 파일에 전송할 바이너리 데이터
    unsigned char data[] = {0x61, 0x62, 0x63};
    size_t dataLength = sizeof(data) / sizeof(data[0]);

    // 바이너리 데이터를 실행 파일의 표준 입력으로 전송
    fwrite(data, sizeof(unsigned char), dataLength, fp);

    // 파이프를 통한 데이터 전송을 완료하고 파이프를 닫습니다.
    pclose(fp);

    printf("바이너리 데이터가 실행 파일에 전송되었습니다.\n");

    return EXIT_SUCCESS;
}

