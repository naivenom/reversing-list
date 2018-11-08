import random
import sys

#REVERSE ENGINEERING
key_ = [87,107,50,112,50,112,109,51,119,103,55,101,111,55,100]  #key
#password = [84,104,49,115,49,115,110,48,116,100,52,102,108,52,103]
def check_key(key):
    char_sum = 0
    for c in key:
        char_sum += ord(c)
    sys.stdout.write("{0:3} | {1}      \r".format(char_sum, key))
    sys.stdout.flush()
    return char_sum

def main():
    i = 0
    list_ = []
    while True:
        key = ""
        key += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_!$%&#'()*+,./:;<>=?@[]`{~}\"")
        password = check_key(key)
        local18 = 0
        xor = key_[i] ^ 3                 #xor eax, 3               
        local14 = xor-password            #sub edx, eax
        #print("Distance: "+str(local14))
        if local14 == 0:                  #cmp dword [local_14h], 0          Compare to win
            list_.append(chr(xor))
            print("Distance: "+str(local14))
            if key_[i] == 100:
                return list_
            i += 1 
if __name__ == "__main__":
    print("For win the distance has to be = 0  cmp dword [local_14h], 0")
    hardcoded_check = main()
    print("Flag --> "+"".join(hardcoded_check)) 
