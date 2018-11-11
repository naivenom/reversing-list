import random
import sys
import r2pipe
import time

'''profile: chall.rr2
#!/usr/bin/rarun2
program=./chall
stdin="AAAA"
stdout=
'''
r = r2pipe.open("./chall")
r.cmd('e dbg.profile=chall.rr2')
r.cmd('doo') # initially you are debugging rarun2
r.cmd('db 0x0040008e')
r.cmd('dc')
print r.cmd('drj')
print (chr(27) + "[0;33m" + "[+]Key: "+chr(27) + "[0m")
key = r.cmdj('pxj 46@%s'%0x0040010c)
print(key)
key_value = 10

def check_key(key):
    char_sum = 0
    for c in key:
        char_sum += ord(c)
    sys.stdout.write("{0:3} | {1}      \r".format(char_sum, key))
    sys.stdout.flush()
    return char_sum

timeout = time.time()+1
print (chr(27) + "[1;36m" + "[+] STAGE 1 - RECON: Estimate first values" + chr(27) + "[0m")
while True:
    test = 0
    if test == 1 or time.time() > timeout:
        break
    a = ""
    a += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_!{}")
    b = ""
    b += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_!{}")
    rand_a = check_key(a)
    rand_b = check_key(b)


    xored = rand_a ^ rand_b
    if key_value == xored:
        print (chr(27) + "[0;33m" + "\n\tEstimate values: %s, %s "%(chr(rand_a),chr(rand_b))+chr(27) + "[0m")
    test = test-1

print (chr(27) + "[1;36m" + "[+] STAGE 2 - SOLVE" + chr(27) + "[0m")
input_zero = raw_input("Input[0]>>>")
input_one = raw_input("Input[1]>>>")
input_n = ord(input_one)
flag = []
for i in range(len(key)-1):
    input_n = key[i+1]^input_n
    flag.append(chr(input_n))
print("".join(input_zero)+"".join(input_one)+"".join(flag))

'''
<output>
108 | l      
	Estimate values: f, l
 70 | F      
	Estimate values: L, F 
 90 | Z      
	Estimate values: P, Z 
113 | q      
	Estimate values: {, q 
[+] STAGE 2 - SOLVE
Input[0]>>>f
Input[1]>>>l
flag{Yay_if_th1s_is_yer_f1rst_gnisrever_flag!}
'''
