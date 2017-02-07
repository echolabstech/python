class LinkedList:
	class Node:
		def __init__(self, data):
			self.data = data
			self.next = None
		def __str__(self):
			return str(self.data)

	def __init__(self):
		self.head = None

	def __str__(self):
		values = []
		if self.head:
			node = self.head
			values.append(node.data)
			while node.next:
				node = node.next
				values.append(node.data)
		return str(values)

	def push(self, data):
		newNode = self.Node(data)
		newNode.next = self.head
		self.head = newNode
		return newNode

	def insertAfter(self, oldNode, data):
		if not self._findNode(oldNode):
			raise KeyError('node {} not found'.format(oldNode.data))
		newNode = self.Node(data)
		newNode.next = oldNode.next
		oldNode.next = newNode
		return newNode

	def _findNode(self, targetNode):
		node = self.head
		if node:
			if node is targetNode:
				return True
			else:
				while node.next:
					if node.next is targetNode:
						return True
					else:
						node = node.next
		return False

	def append(self, data):
		newNode = self.Node(data)
		
		if not self.head:
			self.head = newNode
		else:
			node = self.head
			while node.next:
				node = node.next
			node.next = newNode
		return newNode

	def delete(self, key):
		if self.head:
			node = self.head
			if node.data == key:
				self.head = node.next
				return True
			else:
				while node.next:
					if node.next.data == key:
						node.next = node.next.next
						return True
					else:
						node = node.next
		return False

if __name__ == '__main__':
	list = LinkedList()
	
	print("push an element onto the front of the list");
	node = list.push(20)
	print(node)

	try:
		print("insert an element after another element");
		newNode = 30
		node = list.insertAfter(node, newNode)
		print(node)
	except KeyError as e:
		print('could not insert {0} because {1}'.format(newNode, e))

	print("append an element to the end of the list");
	node = list.append(40)
	print(node)

	print("delete element {}".format(node.data))
	list.delete(node.data)

	print("all elements")
	print(list)
