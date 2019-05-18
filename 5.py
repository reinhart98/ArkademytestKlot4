
arr = ["G","W","A","W","E","C"]

def sort_arr(parr):
	for i in range (len(parr)):
		minval = min(parr)
		maxval = max(parr)

		mindex = parr.index(minval)
		maxdex = parr.index(maxval)

		if(mindex>maxdex):
			parr.pop(maxdex)
	print([minval,maxval])

sort_arr(arr)