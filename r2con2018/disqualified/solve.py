import r2pipe
import sys
#r = r2pipe.open(
#filename='', flags=['-d', 'rarun2', 'program=psv', 'stdin="r2con{"'])
r = r2pipe.open("./disqualified")
r.cmd('e dbg.profile=disqualified.rr2')
r.cmd('doo') #initially you are debuggign rarun2 
r.cmd('db main') #Random memory address code so setting bp in main
r.cmd('dc')
#print r.cmd('drj')


#STAGE 1
if sys.argv[1] == "stage1":
    print (chr(27) + "[1;36m" + "[+] STAGE 1 - RECON: Getting key and xor 4 bytes with function prelude opcodes:554889e5" + chr(27) + "[0m")
    while True:
        list_ = []
        disass = []
        chrlist = []
        if r.cmdj('drj')["rcx"] == 196:
            break
        while True:
            instruction = r.cmdj('pdj 1')[0]
            disass.append(instruction['opcode'])
            #RECON: Getting key and xor 4 bytes with function prelude opcodes:554889e5
            #push rbp
            #mov rbp, rsp
            if instruction['opcode'] == "movzx eax, byte [rax]":
                if r.cmdj('drj')["rcx"] == 28:
                    print(instruction['opcode'])
                    print(r.cmdj('drj')["rcx"])
                    xor = r.cmdj('drj')["rcx"] ^ 85
                    list_.append(xor)
                elif r.cmdj('drj')["rcx"] == 101:
                    print(instruction['opcode'])
                    print(r.cmdj('drj')["rcx"])
                    xor = r.cmdj('drj')["rcx"] ^ 72
                    list_.append(xor)
                elif r.cmdj('drj')["rcx"] == 197:
                    print(instruction['opcode'])
                    print(r.cmdj('drj')["rcx"])
                    xor = r.cmdj('drj')["rcx"] ^ 137
                    list_.append(xor)
                elif r.cmdj('drj')["rcx"] == 196:
                    print(instruction['opcode'])
                    print(r.cmdj('drj')["rcx"])
                    xor = r.cmdj('drj')["rcx"] ^ 229
                    list_.append(xor)   
                    #print(list_)
                    for x in range(len(list_)):
                        #print(chr(int(list_[x])))
                        chrlist.append(chr(int(list_[x])))
                    print (chr(27) + "[0;33m" + "\tFirst characters of flag: "+"".join(chrlist)+chr(27) + "[0m")
                    break
            r.cmd('ds')
            r.cmd('sr rip')  

#STAGE 2
elif sys.argv[1] == "stage2":
    print (chr(27) + "[1;36m" + "[+] STAGE 2 - SOLVE: Getting the next keys using the previous part of flag and xor 4 bytes with function prelude opcodes:554889e5" + chr(27) + "[0m")
    while True:
        list_ = []
        disass = []
        chrlist = []
        opcodes = [85,72,137,229] #function prelude opcodes
        if r.cmdj('drj')["rax"] == 72:
            break
        while True:    
            instruction = r.cmdj('pdj 1')[0]
            disass.append(instruction['opcode'])
            #SOLVE: Getting the next keys using the previous part of flag and xor 4 bytes with function prelude opcodes:554889e5
            #push rbp
            #mov rbp, rsp
            if instruction['opcode'] == "mov esi, eax":
                if r.cmdj('drj')["rax"] == 72:
                    r.cmd('ds')
                    r.cmd('sr rip')
                    print("[+]Getting instruction: "+instruction['opcode'])
                    #print(r.cmdj("drj")["rdi"])
                    dir_addr = hex(r.cmdj("drj")["rdi"]-664) #0x298 = Distance to get the next memory address whose content is the key
                    print("[+]Memory address of key: "+dir_addr)
                    key = r.cmdj("pxj 4 @%s"%dir_addr)
                    for x in range(len(key)):
                        xor = int(key[x]) ^ opcodes[x]
                        chrlist.append(chr(xor))
                    print (chr(27) + "[0;33m" + "\tNext 4 Bytes of flag: "+"".join(chrlist)+chr(27) + "[0m")
                    dir_ = r.cmdj("drj")["rdi"]-664-72 #We realize that the distance to get the other keys it is at 0x48
                    print("[+]Memory address of key: "+hex(dir_))  #So we just need to subtraction 0x48 each time and xored for getting the flag
                    for x in range(4):
                        chrlist = []
                        key = r.cmdj("pxj 4 @%s"%dir_)
                        for x in range(len(key)):
                            xor = int(key[x]) ^ opcodes[x]
                            chrlist.append(chr(xor))
                        print (chr(27) + "[0;33m" + "\tNext 4 Bytes of flag: "+"".join(chrlist)+chr(27) + "[0m")
                        dir_ = dir_-72
                        print("[+]Memory address of key: "+hex(dir_))
                    break
            r.cmd('ds')
            r.cmd('sr rip')
