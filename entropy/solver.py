from z3 import *

def func_input_transf(x):
    x = (x * 0x5deece66d + 0xb) & 0xffffffffffff;
    return simplify(x)

input_transf = BitVec("x", 48 ) #creates a bit-vector variable in Z3 named x with 48 BITS 8*6

#Decrypt 100 times
for i in range(100):
    input_transf = func_input_transf(input_transf)

#But check is just with func_input_transf 100 times, and not xored. 
solve(input_transf == 0xfd94e6e84a0a)
#result in decimal, little endian
