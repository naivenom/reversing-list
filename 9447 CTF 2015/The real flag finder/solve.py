import r2pipe

r = r2pipe.open("./flagFinderRedux")
r.cmd('e dbg.profile=redux.rr2')
r.cmd('doo') # initially you are debugging rarun2 
r.cmd("db 0x00400729") #We realize with debugging that the flag is store at this memory address in stack...
r.cmd('dc')
flag = r.cmdj('pxj@rax')
chrlist = []
for x in range(len(flag)):
    chrlist.append(chr(int(flag[x])))
    if chr(int(flag[x])) == "}":
        print (chr(27) + "[0;33m" + "\tFlag: "+"".join(chrlist)+chr(27) + "[0m")
        break
