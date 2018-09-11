import r2pipe

#r = r2pipe.open(
#filename='', flags=['-d', 'rarun2', 'program=psv', 'stdin="r2con{"'])
r = r2pipe.open("./psv")
r.cmd('e dbg.profile=psv.rr2')
r.cmd('doo') # initially you are debugging rarun2 
r.cmd('db 0x0040084a')
r.cmd('dc')
#print r.cmd('drj')
def step():
    r.cmd('ds')
    r.cmd('sr rip')
while True:
    list_ = []
    disass = []
    if r.cmd('dr rdx') == "0x0000ffff":
        break 
    while True:
        instruction = r.cmdj('pdj 1')[0]
        disass.append(instruction['opcode'])
        if instruction['type'] == 'xor':
            print("[+] RDX Value: "+r.cmd('dr rdx')+" RCX Value: "+r.cmd('dr rcx')+" RAX Value: "+r.cmd('dr rax'))
            xor = int(r.cmd('dr rdx'),16)^int(r.cmd('dr rax'),16) #xor operation to get password
            if xor > 256:
                print("\tNon chr")
            else:
                print (chr(27) + "[0;33m" + "\tXOR Operation RAX ^ RDX: " +chr(xor)+chr(27) + "[0m")
            value = r.cmdj('drj')["rcx"]
            list_.append(value)
            
        elif r.cmd('dr rdx') == "0x0000ffff":
            #print(list_)
            break
        step()
