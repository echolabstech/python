# Major Sapp III 02/12/2017
class LinkedList:
	class Node:
		def __init__(self, key, value):
			self.next = None
			self.key = key
			self.value = value

	def __init__(self):
		self.head = None

	def push(self, key, value):
		newNode = self.Node(key, value)
		if self.head:
			newNode.next = self.head
		self.head = newNode

	def get(self, key):
		node = self.head
		while node.next and node.key != key:
			node = node.next
		if node.key == key:
			return node.value
		return False
			
	def remove(self, key):
		if self.head:
			prevNode = None
			node = self.head
			if node.key == key:
				node = None
				self.head = node
				return True
			else:
				while node.next and node.key != key:
					prevNode = node
					node = node.next
				if node.key == key:
					prevNode.next == node.next
					return True
		return False

	def update(self, key, value):
		pass

class HashTable:
	table = []

	def __init__(self, size=128):
		self.table = [None]*size

	def _hash(self, key):
		return (key % len(self.table))

	def add(self, key, value):
		index = self._hash(key)
		if not self.table[index]:
			ll = LinkedList()
			ll.push(key, value)
			self.table[index] = ll
		else:
			ll = self.table[index]
			ll.push(key, value)			
		return True

	def get(self, key):
		index = self._hash(key)
		ll = self.table[index]
		return ll.get(key)

if __name__ == "__main__":
	names = HashTable()
	names.add(3, "anthony")
	names.add(4, "sam")
	names.add(5, "major")
	names.add(5, "james")

	print(names.get(3))
	print(names.get(4))
	print(names.get(5))
