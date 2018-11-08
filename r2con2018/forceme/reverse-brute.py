import random
import sys

def check_key(key):
    char_sum = 0
    for c in key:
        char_sum += ord(c)
    sys.stdout.write("{0:3} | {1}      \r".format(char_sum, key))
    sys.stdout.flush()
    return char_sum


#REVERSE ENGINEERING
#password = [101,115,105,108,114,117,108,101,122] #Solve it 
key_ = [0x90, 0xa6, 0x9c, 0x99, 0xa7, 0xa0, 0x99, 0x90, 0xaf]

#SYM.CODE
def code():
    i = 0
    list_ = []
    while True:
        key = ""
        key += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_!$%&#'()*+,./:;<>=?@[]`{~}\"")
        local14 = check_key(key)
        local8 = 7                     #mov dword [local_8h], 7
        local4 = 69                    #mov dword [local_4h], 0x45							   
        shl = local8<<4                #shl eax,4
        xor = local14 ^ local4
        add = xor + shl
        if add == key_[i]:
            list_.append(chr(local14))
            #print hex(add)
            if key_[i] == 0xaf:
                return list_
            i += 1

if __name__ == "__main__":
    hardcoded_check = code()                      
    print("Flag -->"+"".join(hardcoded_check)) 
