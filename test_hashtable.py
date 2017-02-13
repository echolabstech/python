# Major Sapp III 02/13/2017
import unittest
from hashtable import *

class TestHashTable(unittest.TestCase):
	pass

class TestLinkedList(unittest.TestCase):
	def setUp(self):
		self.ll = LinkedList()	
		self.key = "foo"
		self.value = "bar"
		self.key2 = "lord"
		self.value2 = "fawquad"
		self.key3 = "backyard"
		self.value3 = "bootyburglar"

	def tearDown(self):
		self.ll = None

	def test_pushReplacesHead(self):
		self.assertEqual(None, self.ll.head)

		self.ll.push(self.key, self.value)

		self.assertEqual(self.key, self.ll.head.key)
		self.assertEqual(self.value, self.ll.head.value)

	def test_pushAddsLinksToChain(self):
		self.ll.push(self.key, self.value)
		self.ll.push(self.key2, self.value2)
		self.ll.push(self.key3, self.value3)

		self.assertEqual(self.key3, self.ll.head.key)
		self.assertEqual(self.value3, self.ll.head.value)

		self.assertEqual(self.key2, self.ll.head.next.key)
		self.assertEqual(self.value2, self.ll.head.next.value)

		self.assertEqual(self.key, self.ll.head.next.next.key)
		self.assertEqual(self.value, self.ll.head.next.next.value)

	def test_getReturnsCorrectValue(self):
		self.ll.push(self.key, self.value)
		self.ll.push(self.key2, self.value2)
		self.ll.push(self.key3, self.value3)

		self.assertEqual(self.value3, self.ll.get(self.key3))
		self.assertEqual(self.value2, self.ll.get(self.key2))
		self.assertEqual(self.value, self.ll.get(self.key))

	def test_removeWhenNoHead(self):
		self.assertFalse(self.ll.remove(self.key))

	def test_removeWhenOnlyHead(self):
		self.ll.push(self.key, self.value)
		self.assertTrue(self.ll.remove(self.key))
		self.assertFalse(self.ll.remove(self.key))

	def test_removeWhenMultipleLinksInChain(self):
		self.ll.push(self.key, self.value)
		self.ll.push(self.key3, self.value3)
		self.ll.push(self.key2, self.value2)
		self.assertTrue(self.ll.remove(self.key3))

unittest.main()