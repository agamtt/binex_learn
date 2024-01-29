from pwn import *
from ctypes import *

with open('ASM32','rb') as f:
    data = f.read()
    print(data)


memory = create_string_buffer(data,len(data))
shell_func = cast(memory, CFUNCTYPE(None))

shell_func()

