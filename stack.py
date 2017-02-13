# Major Sapp III 02/13/2017
def push(array, value):
	swap = []
	for k,v in enumerate(array):
		swap.insert(k+1, v)
	swap.insert(0, value)
	return swap

def pop(array):
	value = array[0]
	swap = []
	i=0
	while i < (len(array)):
		swap.insert(i, array[i+1])
		i += i + 1
	return (value, swap)

if __name__ == "__main__":
	array = []
	print("before:",array)
	array = push(array, "first")
	array = push(array, "second")
	array = push(array, "third")
	print("after:",array)
	value, array = pop(array)
	print("pop {}".format(value))
	print("after pop:",array)
