import r2pipe

#r = r2pipe.open(
#filename='', flags=['-d', 'rarun2', 'program=psv', 'stdin="r2con{"'])
r = r2pipe.open("./rev_patch")
r.cmd('e dbg.profile=rev150.rr2')
r.cmd('doo') # initially you are debugging rarun2 
r.cmd('db 0x0040069a')
r.cmd('dc')
print r.cmd('drj')
def step():
    r.cmd('ds')
    r.cmd('sr rip')
while True:
    list_ = []
    disass = []
    while True:
        instruction = r.cmdj('pdj 1')[0]
        disass.append(instruction['opcode'])
        if instruction['opcode'] == 'mov edx, ecx':
            print("[+]RCX Value: "+r.cmd('dr rcx'))
            value = r.cmdj('drj')["rcx"]
            list_.append(chr(value))
            print("".join(list_))
                 
        step()
