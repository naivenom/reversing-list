def main_():
	ea = idc.ScreenEA()
	print "0x%x %s" % (ea,ea)


def debug_(addr):
	idc.RunTo(BeginEA())
	idc.AddBpt(addr) #breakpoint	004016D5
	idc.GetDebuggerEvent(WFNE_SUSP,-1)
	idc.RunTo(addr)


def help_():
	print("""Functions:
		debug_(addr)
		recon()
		solve()""")

def recon(): 
	stdin = "abcdefghijklmnopqrstuvwxyz01234567890{}"
	GetDebuggerEvent(WFNE_SUSP, -1)    
	rax = idc.GetRegValue('RAX')
	print("[+] Value of RAX is: %s "%rax)
	cipher = idc.GetString(rax)
	print("[+] Value of Substitution cipher is: %s "%cipher)
	sc = Strings()
	for s in sc:
		if s.ea == 4661280:
			print "%x: len=%d type=%d --> '%s'" % (s.ea, s.length, s.type, str(s))
			key = str(s)
	print("[+] Value of Key: %s"%key)
	flag = ''
	for i in key:                                    
		try:
			flag += stdin[cipher.index(i)]  
			print(flag)
		except ValueError:
			pass  
def solve():
	stdin = "abcdefghijklmnopqrstuvwxyz01234567890{}"
	cipher = "fedcba`onmlkjihwvutsrqp_~}76543210?>|z"
	key = "o3dl6s|41a42344d110746d574e35c2f77ab6>3z"
	flag = ''
	for i in key:
		flag += stdin[cipher.index(i)]
	print(flag)

if __name__ == '__main__':
	#main_()
	#debug_(addr)
	#recon()
	#solve()
	help_()
