import random
import sys
def check_key(key):
	char_sum = 0
	for c in key:
		char_sum += ord(c)
	sys.stdout.write("{0:3} | {1}      \r".format(char_sum, key))
	sys.stdout.flush()
	return char_sum

key = ""

while True:
	key += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_")
	s = check_key(key)
        key_= [13,60,15,72,30,87,48]
        xor = []
        leak = [68,99,87,120]
        suma1 = 0
        suma2 = 0
        for b in range(len(leak)):
            suma1+=leak[b]
	if s > 666:
		key = ""
        elif s==666:
            if len(key[0:3])== 3:
                for x in range(len(key[0:3])):
                    try:
                        leak.append(ord(key[x]))
                        suma1+= ord(key[x])
                    except IndexError:
                        pass
                for i in range(len(key_)):
                    xor.append(leak[i] ^ key_[i])
                    suma2 += xor[i]
                charr = ''
                if suma2 == 569 and suma1 ==666:
                    for v in range(len(xor)):
                        charr+=chr(xor[v])
                    print "Localizado una clave valida: {0}".format(charr)
                    
            else:
                pass
