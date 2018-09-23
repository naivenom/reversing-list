import sys

#REVERSE ENGINEERING
def control(suma):
    if len(hex(suma)) == 11:
        splitt = hex(suma).split()[0][3:]
        suma = int(splitt,16)
        return suma

#SYM.HASH FUNCTION
def symhash(password):
    for i in range(len(password)):
        if i == 0:
            fabada = 16431834              #mov eax, ebp-0x4 (0xfabada)
            shl = fabada<<6                #shl eax,6
            #print hex(shl)
        elif i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
            #print hex(local4)
            fabada = local4                #mov eax, ebp-0x4
            shlOP = fabada<<6              #shl eax,6
            splitt = hex(shlOP).split()[0][4:]
            shl = int(splitt,16)
            #print hex(shl)
                     
                                           #mov edx, eax
                                           #mov eax, ebp-0x4
    
    
        
        if len(hex(shl+fabada)) > 10:
            sum1 = control(shl+fabada)
            chrr = password[i]             #mov eax, ebp-0x8
            #print chrr
            if len(hex(sum1+chrr)) > 10:
                sum2 = control(sum1+chrr)  #add eax,edx
                sum3 = sum2+sum2           #add eax,eax
                local4 = sum3              #mov ebp-0x4,eax
                #print hex(local4)
            else:
                sum2 = sum1+chrr   
                sum3 = sum2+sum2   
                local4 = sum3      
                #print hex(local4)
        else:
            sum1 = shl+fabada     
            ##print(hex(sum1))
            chrr = password[i]    
            #print chrr
            if len(hex(sum1+chrr)) > 10:
                sum2 = control(sum1+chrr)
                sum3 = sum2+sum2
                local4 = sum3
                #print hex(local4)
            else:
                sum2 = sum1+chrr      
                #print hex(sum2)
                if len(hex(sum2+sum2)) > 10:
                    sum3 = control(sum2+sum2)
                    local4 = sum3
                    #print hex(local4)
                else:
                    sum3 = sum2+sum2     
                    local4 = sum3         
                    #print hex(local4)

    return hex(local4)

#SYM.HASH2 FUNCTION
def symhash2(password):
    for i in range(len(password)):
        if i == 0:
            beef = 48879                   #mov eax, ebp-0x4 (0xbeef)
            shl = beef<<5                  #shl eax,6
            #print hex(shl)
        elif i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
            #print hex(local4)
            beef = local4                  #mov eax, ebp-0x4
            shlOP = beef<<5                #shl eax,5
            if len(hex(shlOP)) > 11:
                splitt = hex(shlOP).split()[0][4:]
                shl = int(splitt,16)
                #print hex(shl)
            elif len(hex(shlOP)) > 10:
                splitt = hex(shlOP).split()[0][3:]
                shl = int(splitt,16)
                #print hex(shl)
            else:
                shl = shlOP
                #print hex(shl)
                                           #mov edx,eax
                                           #mov eax,ebp-0x4
    
       
        if len(hex(shl+beef)) > 10:
            sum1 = control(shl+beef)       #add edx, eax
            chrr = password[i]             #mov eax, ebp-0x8
            #print chrr
            if len(hex(sum1+chrr)) > 10:
                sum2 = control(sum1+chrr)  #add eax,edx
                local4 = sum2              #mov ebp-0x4,eax
                #print hex(local4)
            else:
                sum2 = sum1+chrr      
                local4 = sum2      
                #print hex(local4)
        else:
            sum1 = shl+beef     
            ##print(hex(sum1))
            chrr = password[i]    
            #print chrr
            if len(hex(sum1+chrr)) > 10:
                sum2 = control(sum1+chrr)
                local4 = sum2
                #print hex(local4)
            else:
                sum2 = sum1+chrr      
                #print hex(sum2)    
                local4 = sum2         
                #print hex(local4)

    return hex(local4)

if __name__ == "__main__":
    try:
        if sys.argv[1]:
            password = []
            for i in range(len(sys.argv[1])):
                password.append(ord(sys.argv[1][i]))
            if len(password) == 7:
                print (chr(27) + "[1;36m" + "[+] STAGE 1 - REVERSE ENGINEERING" + chr(27) + "[0m")
                local20 = 2941729636                   #mov qword [local_20h], -0x50a8c49c == 0xffffffffaf573b64 == parte baja 0xaf573b64
                local28 = 1512702707                   #mov QWORD PTR [rbp-0x28], 0x5a2a02f3
                hash1 = symhash(password)                      #ret
                print("First Hash: "+hash1)                            
                local30 = int(hash1, 16)               #mov ebp-0x30, rax
                hash2 = symhash2(password)                     #ret
                print("Second Hash: "+hash2)
                local38 = int(hash2, 16)               #mov ebp-0x38, rax
                rax = local30                          #mov rax, ebp-0x30
            
                #Now the first check compare the first hash with local variable local20 whose content in stack is 0xaf573b64

                if rax == local20:                     #cmp rax,QWORD PTR [rbp-0x20] 
                    rax = local38                      #mov rax,QWORD PTR [rbp-0x38]
                    if rax == local28:                 #cmp rax,QWORD PTR [rbp-0x28] Segundo check con el hash2 y el local28 hardcoded arriba
                        print("\nGood!")               #mov DWORD PTR [rbp-0x4],0x10  

                    else:                              
                        print("\nBad")                 #mov DWORD PTR [rbp-0x4],0xc
                else:                            
                    print("\nBad")                     #mov DWORD PTR [rbp-0x4],0xc
            else:
                print("[!] Error: Wrong LENGHT!")
    except IndexError:
        print("Usage: python reverse.py password")

