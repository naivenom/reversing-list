import sys
import time
def time_sweetened():
    b = time.strftime("%M",time.gmtime())
    sweetened = int(b)+65
    return sweetened

#SYM.Y FUNCTION
def symy(key):
    key_list = []
    try:
        key0 = 0xc9 ^ 0x91
        key0 = chr(key0)
        if key[0] == key0 and int(key[1]) in range(0,10):
            key_list.append(key0)
        key2 = 0x70 ^ 0x32
        key2 = chr(key2)
        if key[2] == key2 and int(key[3]) in range(0,10):
            key_list.append(key2)
        key5 = 0x94 ^ 0xce
        key5 = chr(key5)
        if key[5] == key5 and int(key[6]) in range(0,10):
            key_list.append(key5)
        key7 = 0x41 ^ 0x0b
        key7 = chr(key7)
        if key[7] == key7 and int(key[8]) in range(0,10):
            key_list.append(key7)
        key10 = 0x4c ^ 0x15
        key10 = chr(key10)
        if key[10] == key10 and int(key[11]) in range(0,10):
            key_list.append(key10)
        key12 = 0xa9 ^ 0xe2
        key12 = chr(key12)
        if key[12] == key12 and int(key[13]) in range(0,10):
            key_list.append(key12)
        key15 = 0x2d ^ 0x6e
        key15 = chr(key15)
        if key[15] == key15 and int(key[16]) in range(0,10):
            key_list.append(key15)
        key17 = 0x37 ^ 0x7b
        key17 = chr(key17)
        if key[17] == key17 and int(key[18]) in range(0,10):
            key_list.append(key17)
        else:
            print("[!] Error: Wrong KEY!")
            sys.exit(1)
    except ValueError:
        print("[!] Error: Wrong VALUE TYPE IN KEY!")
        sys.exit(1)
    return key_list

#SYM.X FUNCTION
def symx(y_value):
    list_ = []
    xor_list = []
    good = []
    for x in range(0,10):
        list_.append("0x3"+str(x))
    for i in range(0,10):                    
        if int(key[1]) or int(key[3]) or int(key[6]) or int(key[8]) or int(key[11]) or int(key[13]) or int(key[16]) or int(key[18]) == int(list_[i][3]):
            hex_key = list_[i]               #movzx eax, byte [rax]
                                             #movsx eax, al
            sub = int(hex_key,16)-48         #sub eax, 0x30
            value = 6                        #mov eax, dword [local_3ch]
            xor = sub ^ value                #xor eax, dword [local_38h]
            xor_list.append(xor)             #mov dword [local_34h], eax
    print (chr(27) + "[0;33m" + "\tXOR Values of 0x30 to 0x39: "+"".join(str(xor_list))+chr(27) + "[0m")
    for i in range(len(y_value)):
        rax = symc(y_value[i])
        if y_value[i] == y_value[0]:
            if rax == xor_list[int(key[1])]: #cmp eax, dword [local_34h]
                print (chr(27) + "[0;33m" + "\tGood EAX = RBP-0x34: "+str(rax)+chr(27) + "[0m")
                good.append(int(key[1]))
            else:
                print("[!] Error: Wrong VALUE IN KEY!")
                sys.exit(1)
        elif y_value[i] == y_value[1]: 
            if rax == xor_list[int(key[3])]: #cmp eax, dword [local_34h]
                print (chr(27) + "[0;33m" + "\tGood EAX = RBP-0x34: "+str(rax)+chr(27) + "[0m")
                good.append(int(key[3]))
            else:
                print("[!] Error: Wrong VALUE IN KEY!")
                sys.exit(1)
        elif y_value[i] == y_value[2]:
            if rax == xor_list[int(key[6])]: #cmp eax, dword [local_34h]
                print (chr(27) + "[0;33m" + "\tGood EAX = RBP-0x34: "+str(rax)+chr(27) + "[0m")
                good.append(int(key[6]))
            else:
                print("[!] Error: Wrong VALUE IN KEY!")
                sys.exit(1)
        elif y_value[i] == y_value[3]:
            if rax == xor_list[int(key[8])]: #cmp eax, dword [local_34h]
                print (chr(27) + "[0;33m" + "\tGood EAX = RBP-0x34: "+str(rax)+chr(27) + "[0m")
                good.append(int(key[8]))
            else:
                print("[!] Error: Wrong VALUE IN KEY!")
                sys.exit(1)
        elif y_value[i] == y_value[4]:
            if rax == xor_list[int(key[11])]: #cmp eax, dword [local_34h]
                print (chr(27) + "[0;33m" + "\tGood EAX = RBP-0x34: "+str(rax)+chr(27) + "[0m")
                good.append(int(key[11]))
            else:
                print("[!] Error: Wrong VALUE IN KEY!")
                sys.exit(1)
        elif y_value[i] == y_value[5]:
            if rax == xor_list[int(key[13])]: #cmp eax, dword [local_34h]
                print (chr(27) + "[0;33m" + "\tGood EAX = RBP-0x34: "+str(rax)+chr(27) + "[0m")
                good.append(int(key[13]))
            else:
                print("[!] Error: Wrong VALUE IN KEY!")
                sys.exit(1)
        elif y_value[i] == y_value[6]:
            if rax == xor_list[int(key[16])]: #cmp eax, dword [local_34h]
                print (chr(27) + "[0;33m" + "\tGood EAX = RBP-0x34: "+str(rax)+chr(27) + "[0m")
                good.append(int(key[16]))
            else:
                print("[!] Error: Wrong VALUE IN KEY!")
                sys.exit(1)
        elif y_value[i] == y_value[7]:
            if rax == xor_list[int(key[18])]: #cmp eax, dword [local_34h]
                print (chr(27) + "[0;33m" + "\tGood EAX = RBP-0x34: "+str(rax)+chr(27) + "[0m")
                good.append(int(key[18]))
            else:
                print("[!] Error: Wrong VALUE IN KEY!")
                sys.exit(1)
    return good
#SYM.C FUNCTION
def symc(y_value):
    rax = 0
    char_ = ord(y_value)                     #mov eax, dword [local_14h]
    while True:
        local4 = char_ & 1                   #and eax, 1
                                             #mov dword [local_4h], eax
        char_ = char_>>1                     #sar eax, 1
        if char_ == 1:
            rax = rax+1                      #add eax, 1
            return rax
        if local4 == 1:                      #cmp dword [local_4h], 1
            rax = rax+1                      #add dword [local_8h], 1   

if  __name__ == "__main__":
    print(''' 
 /$$   /$$                              /$$$$$$              /$$     /$$
| $$  /$$/                             /$$__  $$            | $$    | $$
| $$ /$$/   /$$$$$$  /$$   /$$        | $$  \ $$ /$$   /$$ /$$$$$$  | $$$$$$$
| $$$$$/   /$$__  $$| $$  | $$ /$$$$$$| $$$$$$$$| $$  | $$|_  $$_/  | $$__  $$
| $$  $$  | $$$$$$$$| $$  | $$|______/| $$__  $$| $$  | $$  | $$    | $$  \ $$
| $$\  $$ | $$_____/| $$  | $$        | $$  | $$| $$  | $$  | $$ /$$| $$  | $$
| $$ \  $$|  $$$$$$$|  $$$$$$$        | $$  | $$|  $$$$$$/  |  $$$$/| $$  | $$
|__/  \__/ \_______/ \____  $$        |__/  |__/ \______/    \___/  |__/  |__/
                     /$$  | $$
                    |  $$$$$$/         Ultimate ultra-mega hacker key checker
                     \______/       Version: 01.1337 (Only 1 key has been saved)''')
    try:
        if sys.argv[1] and sys.argv[2]:
            time_value = time_sweetened()
            print (chr(27) + "[0;33m" + "\tTime is time, do you know what I mean...: "+"".join(chr(time_value))+chr(27) + "[0m")
            try:
                if ord(sys.argv[1][1:]) == time_value and sys.argv[1][:1] == "-": 
                    if len(sys.argv[2]) == 19:
                        key = sys.argv[2]
                        if key[4] and key[9] and key[14] == "-":
                            y_value = symy(key)
                            if y_value == None:
                                print("[!] Error: Wrong KEY!")
                                sys.exit(1)
                            else:
                                print (chr(27) + "[1;36m" + "[+] STAGE 1: Checking A-Z char in Key succesfully!: %s"%(y_value) + chr(27) + "[0m")
                                x_value = symx(y_value)
                                print (chr(27) + "[1;36m" + "[+] STAGE 2: Checking 0-9 numbers in Key succesfully!: %s"%(x_value) + chr(27) + "[0m")
                                final_key = []
                                for a in range(len(y_value)):
                                    final_key.append(y_value[a])
                                    final_key.append(str(x_value[a]))
                                    if a == 1 or a == 3 or a == 5:
                                        final_key.append("-")
                                print (chr(27) + "[0;33m" + "\tFlag: "+"".join(final_key)+chr(27) + "[0m")  
                        else:
                            print("[!] Error: Wrong FORMAT KEY!")
                    else:
                        print("[!] Error: Wrong LENGHT!")
                else:
                    print("[!] Error: Wrong TIME!")
            except TypeError:
                print("[!] Error: Wrong ARG FORMAT!")
    except IndexError:
        print("Usage: python reverse.py arg1 arg2")
    
    
