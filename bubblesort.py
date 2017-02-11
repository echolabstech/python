# Major Sapp III 02/11/2017
from random import seed, sample
from time import time

# time: O(n**2) space: O(1)
def bubblesort(array):
	k=0
	while k < len(array)-1:
		i=0
		done = True
		while i < len(array)-1:
			if array[i] > array[i+1]:
				swapIndex(array, i, i+1)
				done = False
			i += 1
		if done:
			return
		k += 1

# time: O(1) space: O(1)
def swapIndex(array, left, right):
	swap = array[left]
	array[left] = array[right]
	array[right] = swap

if __name__ == "__main__":
	seed()
	array = [x for x in sample(range(100), k=5)];
	print("before:",array)
	bubblesort(array)
	print("after:",array)

