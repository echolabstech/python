# Major Sapp III 02/11/2017
from random import seed, sample
# time O(1) space: O(1)
def swapIndex(array, left, right):
	swap = array[left]
	array[left] = array[right]
	array[right] = swap

# time: O(N**2) space: O(1)
def selectionsort(array):
	k=0
	while(k < len(array)-1):
		i=k+1
		indexOfSmallest = k
		while(i < len(array)):
			if array[indexOfSmallest] > array[i]:
				indexOfSmallest = i
			i +=1
		swapIndex(array, k, indexOfSmallest)
		k += 1

if __name__ == "__main__":
	seed()
	array = [x for x in sample(range(10), k=5)]
	print("before:",array)
	selectionsort(array)
	print("after:",array)
