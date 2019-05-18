import random
import string

arr = []
final_list = []
def arrRandom(param):
	
	for x in range (param):
		x = ''.join(random.choice(string.ascii_letters) for x in range(32))
		arr.append(x)
	return arr

def noDuplicate():
	for num in arr:
		if num not in final_list:
			final_list.append(num)
	return final_list

		

arrRandom(3) # generate arr[random] with index==32 char and len==3
print(noDuplicate())#print arr[random] with no duplicate of index
