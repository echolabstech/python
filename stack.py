# Major Sapp III 02/13/2017
def push(array, value):
	swap = [None]*(len(array)+1)
	if len(array) > 0:
		for k,v in enumerate(array):
			swap[k+1] = v
	swap[0] = value
	return swap

if __name__ == "__main__":
	array = [None]
	print("before:",array)
	array = push(array, "first")
	array = push(array, "second")
	array = push(array, "third")
	print("after:",array)
