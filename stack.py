# Major Sapp III 02/13/2017
def push(array, value):
	swap = []
	for k,v in enumerate(array):
		swap.insert(k+1, v)
	swap.insert(0, value)
	return swap

if __name__ == "__main__":
	array = []
	print("before:",array)
	array = push(array, "first")
	array = push(array, "second")
	array = push(array, "third")
	print("after:",array)
