import r2pipe
import sys

def lenght(value):
    for i in value[:]:
        if i == 0:
            value.remove(i)
    return value

#SYM.TR1 FUNCTION
def symtr1(msg):
    list_ = []                                   #mov rax, qword obj.msg
    for i in range(len(msg)):                    #mov rdi, rax
        xor = msg[i] ^ 22                        #call sym.imp.strlen
        list_.append(xor)                        #xor eax, ebx
    return list_

#SYM.TR2 + SWEETENED ESTIMATE TIME               #lea rdx, obj.j
def sweetened(xored,values,key):                 #movzx ecx, byte [rax + rdx]
    list_flag = []                               #mov eax, dword obj.tiempo
    list_estimate = []                           #add eax, eax
    for i in range(len(values)):                 #lea rdx, obj.t
        for b in range(44):                      #movzx eax, byte [rax + rdx]
            c = values[i] ^ key[b]               #xor ecx, eax
            if xored[i] == c:                    
                list_flag.append(c)              
                list_estimate.append(key[b])
                break
    return list_flag[:-2],list_estimate[:-2]   
                

if __name__ == "__main__":

    r = r2pipe.open("./in-time")
    r.cmd('e dbg.profile=intime.rr2')
    r.cmd('doo')                 #initially you are debuggign rarun2 
    r.cmd('db main')             #Random memory address code so setting bp in main
    r.cmd('dc')
    rip = r.cmdj('drj')['rip']
    bp = rip+139                 #distance from main to offset we want to continue
    r.cmd('db %s'%hex(bp))
    r.cmd('dc')

    print (chr(27) + "[1;36m" + "[+] STAGE 1 - RECON: Getting final value, key and initial xored with input" + chr(27) + "[0m")
    final_values = rip+11654     #distance from main to obj.s offset. We know that this obj is the final values to cmp with sym.imp.strcmp my obj.j xored

    print("[+] Final values:")
    print(r.cmd('px 24@%s'%hex(final_values)))
    values = r.cmdj('pxj 24@%s'%hex(final_values))
    values_ = lenght(values)
    lenght_values = len(values_)

    print (chr(27) + "[0;33m" + "\tLenght of final values is exactly: "+str(lenght_values)+chr(27) + "[0m")

    raw_key = rip+11718          #distance from main to obj.t offset. This key is xored with xored lenght input value.
    print("[+] Key:")
    print(r.cmd('px 50@%s'%hex(raw_key)))
    key = r.cmdj('pxj 50@%s'%hex(raw_key))
    key_ = lenght(key)
    lenght_key = len(key_)

    print (chr(27) + "[0;33m" + "\tLenght of key is exactly: "+str(lenght_key)+chr(27) + "[0m")
    
    input_password = rip+11942   #distance from main to obj.msg offset. This key is our input password via stdin.
    print("[+] Our stdin:")
    print(r.cmd('px 50@%s'%hex(input_password)))
    passwd = r.cmdj('pxj 50@%s'%hex(input_password))
    passwd_ = lenght(passwd)
    lenght_passwd = len(passwd_)

    print (chr(27) + "[0;33m" + "\tLenght of our input: "+str(lenght_passwd)+chr(27) + "[0m")
    if lenght_passwd != lenght_values:
        print("[!] Error: Our input value has to be 22 of lenght and you put: %s"%str(lenght_passwd))
        sys.exit(1)
    r.quit()
    print("[+] Final values: %s"%values_)
    print (chr(27) + "[1;36m" + "[+] STAGE 2 - ESTIMATED TIME: We estimate the time because of the frecuency key index used, using as example flag{ format" + chr(27) + "[0m")
    xored_input = symtr1(passwd_)
    print("[+] Xored input with input lenght: %s"%xored_input)
    estimated = sweetened(xored_input,values_,key_) 
    print("[+] Valid Xored values: %s"%estimated[0])
    tohex = []
    est_ = estimated[1]
    for i in range(len(est_)):
        hex_ = hex(est_[i])
        tohex.append(hex_)
    print("[+] Valid key values: %s"%estimated[1]+"~"+"".join(str(tohex)))
    hex_key = []
    print("[+] Hex list key values reference:")
    for i in range(len(key_)):
        hex_key.append(hex(key_[i]))
    print(hex_key)
    print (chr(27) + "[0;33m" + "\tTo SOLVE XOR Operation: Final values ^ Valid key values = xored_input^0x16"+chr(27) + "[0m")
