# Major Sapp III 02/12/2017
class HashTable:
	table = []

	def __init__(self, size=128):
		self.table = [None]*size

	def _hash(self, key):
		return (key % len(self.table))

	def add(self, key, value):
		index = self._hash(key)
		self.table[index] = value

	def get(self, key):
		index = self._hash(key)
		return self.table[index]

if __name__ == "__main__":
	hashtable = HashTable()
	hashtable.add(4, "sam")
	hashtable.add(5, "james")
	print(hashtable.get(5))
	print(hashtable.get(4))
