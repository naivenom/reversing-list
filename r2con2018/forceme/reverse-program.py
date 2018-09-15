#REVERSE ENGINEERING
password = [101,115,105,108,114,117,108,101,122] 


#SYM.CODE
def code():
    list_ = []
    for i in range(len(password)):
        local14 = password[i]
        local8 = 7                     #mov dword [local_8h], 7
        local4 = 69                    #mov dword [local_4h], 0x45							   
        shl = local8<<4                #shl eax,4
        xor = password[i] ^ local4
        add = xor + shl
        list_.append(hex(add))
        #print hex(add)

    return list_ 

if __name__ == "__main__":
    hardcoded_check = code()                      
    print(hardcoded_check)                            
  
