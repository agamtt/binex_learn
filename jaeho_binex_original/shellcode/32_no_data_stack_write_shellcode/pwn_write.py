from pwn import *

with open("hello_shellcode",'wb') as f:
    f.write(b'\xe8\x0f\x00\x00\x00\xb0\x04\x31\xdb\xb3\x01\x31\xd2\xb2\x0f\xcd\x80\xb0\x01\x31\xdb\xcd\x80\xe8\xe6\xff\xff\xffHello, world!\n\r')