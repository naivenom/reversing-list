import random
import sys
import r2pipe
import time

r = r2pipe.open("./chall")
r.cmd('e dbg.profile=chall.rr2')
r.cmd('doo') # initially you are debugging rarun2
r.cmd('db 0x0040008e')
r.cmd('dc')
print r.cmd('drj')
print (chr(27) + "[0;33m" + "[+]Key: "+chr(27) + "[0m")
key = r.cmdj('pxj 46@%s'%0x0040010c)
print(key)
key_value = raw_input("Key value>>>")

def check_key(key):
    char_sum = 0
    for c in key:
        char_sum += ord(c)
    sys.stdout.write("{0:3} | {1}      \r".format(char_sum, key))
    sys.stdout.flush()
    return char_sum

timeout = time.time()+1
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
    if int(key_value) == xored:
        print (chr(27) + "[0;33m" + "\n\tEstimate values: %s, %s "%(chr(rand_a),chr(rand_b))+chr(27) + "[0m")
    test = test-1
