
def crossPattern(x):
	for i in range(0,x):
		for k in range(0,x):
			if(k==i or k+i==x-1):
				print("X",end="")
			else:
				print("=",end="")
		print("")

crossPattern(9)