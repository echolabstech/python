# Major Sapp III 02/11/2017
import unittest
from selectionsort import selectionsort

class TestSelectionsort(unittest.TestCase):
	def setup(self):
		pass

	def teardown(self):
		pass

	def test_swap(self):
		ARRAY = [5,2,3]
		array = [5,2,3]
		selectionsort(array)
		self.assertEqual(ARRAY[0], array[2])
		self.assertEqual(ARRAY[1], array[0])
		self.assertEqual(ARRAY[2], array[1])

if __name__ == '__main__':
  unittest.main()