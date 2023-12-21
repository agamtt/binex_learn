section .data
    message db 'gaeun babo!', 0xA    ; 문자열 끝에 개행 문자 추가

section .text
    global _start

_start:
    ; 문자열의 길이 계산 (개행 문자 포함)
    mov edx, 11

    ; 문자열 메시지 포인터 설정
    mov ecx, message

    ; 시스템 콜 번호 설정 (sys_write)
    mov ebx, 1           ; 파일 디스크립터 (1 = 표준 출력)
    mov eax, 4           ; sys_write 시스템 콜 번호

    ; 시스템 콜 호출
    int 0x80

    ; 프로그램 종료
    mov eax, 1           ; sys_exit 시스템 콜 번호
    xor ebx, ebx         ; 종료 코드 (0)
    int 0x80

