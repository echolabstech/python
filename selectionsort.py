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
		i=k
		indexOfSmallest = k
		while(i < len(array)-1):
			if array[k] > array[i+1]:
				if array[indexOfSmallest] > array[i+1]:
					indexOfSmallest = i+1
			i +=1
		swapIndex(array, k, indexOfSmallest)
		print(array)
		k += 1

if __name__ == "__main__":
	seed()
	array = [x for x in sample(range(100), k=5)]
	print("before:",array)
	selectionsort(array)
	print("after:",array)
