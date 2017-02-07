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
		newNode = self.Node(data)
		newNode.next = oldNode.next
		oldNode.next = newNode
		return newNode

	def append(self, data):
		newNode = self.Node(data)
		
		if self.head is None:
			self.head = newNode
		else:
			node = self.head
			while node.next:
				node = node.next
			node.next = newNode
		return newNode

if __name__ == '__main__':
	list = LinkedList()
	
	print("push an element onto the front of the list");
	node = list.push(20)
	print(node)

	print("insert an element after another node");
	node = list.insertAfter(node, 30)
	print(node)

	print("append an element to the end of the list");
	node = list.append(40)
	print(node)

	print("all nodes")
	print(list)
