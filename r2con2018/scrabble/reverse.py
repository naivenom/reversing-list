#REVERSE ENGINEERING
key = [87,107,50,112,50,112,109,51,119,103,55,101,111,55,100]  #key
password = [84,104,49,115,49,115,110,48,116,100,52,102,108,52,103]


def main():
    list_ = []
    local18 = 0
    for i in range(len(key)):
        xor = key[i] ^ 3                 #xor eax, 3               
        resta = xor-password[i]          #sub edx, eax
        local14 = resta
        print("Distance: "+str(local14))
        if local14 == 0:                 #cmp dword [local_14h], 0          Compare to win
            list_.append(hex(xor))

    return list_ 

if __name__ == "__main__":
    print("For win the distance has to be  == 0              #cmp dword [local_14h], 0")
    hardcoded_check = main()                      
    print(hardcoded_check) 
