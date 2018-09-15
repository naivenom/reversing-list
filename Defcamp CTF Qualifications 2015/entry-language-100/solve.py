import r2pipe

r = r2pipe.open("./r100patch")
r.cmd('e dbg.profile=r100patch.rr2')
r.cmd('doo') # initially you are debugging rarun2 
r.cmd('db 0x00400771')
r.cmd('dc')
#print r.cmd('drj')
def step():
    r.cmd('ds')
    r.cmd('sr rip')
while True:
    list_ = []
    disass = []
    if r.cmdj('drj')["rip"] == 4196212:
        break
    print (chr(27) + "[1;36m" + "[+] STAGE 1 - SOLVE: Lenght of password is 11= 0xb" + chr(27) + "[0m")
    while True:
        instruction = r.cmdj('pdj 1')[0]
        disass.append(instruction['opcode'])
        if r.cmdj('drj')["rip"] == 4196212:
            key = r.cmdj('drj')["rax"]
            print(key)
            password = key-1
            print(r.cmd('drj'))
            print (chr(27) + "[0;33m" + "\tSUB Operation EDX-EAX and flag value: " +chr(password)+chr(27) + "[0m")
            list_.append(chr(password))
        if instruction['type'] == 'cmp eax, 1':
            if r.cmdj('drj')['rax'] == 1:
                continue
            else:
                break  
        step()
