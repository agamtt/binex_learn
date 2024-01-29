from pwn import *

asm_code = """
    mov eax, 4
    pop ecx
"""

compiled_code = asm(asm_code)

print(compiled_code)

disasm_code = disasm(compiled_code)

print(disasm_code)