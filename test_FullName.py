import unittest
import FullName
class test_FullName(unittest.TestCase):
	def test_FullName_Valid(self):
                #Testing Valid Inputs
		result = FullName.FullName("first", "last")
		self.assertEqual(result, "first last")
		
		result = FullName.FullName("", "")
		self.assertEqual(result, " ")
		
		result = FullName.FullName('f', 'l')
		self.assertEqual(result, "f l")

		
	def test_FullName_TypeError(self):
                #Testing Other input types
		result = FullName.FullName(-1, -1)
		self.assertEqual(result, "Error")
		
		result = FullName.FullName(complex(5,2), complex(5,2))
		self.assertEqual(result, "Error")


		result = FullName.FullName([1,2], [9,0])
		self.assertEqual(result, "Error")

		result = FullName.FullName(["f", "i", "r", "s", "t"], ["l", "a", "s", "t"])
		self.assertEqual(result, "Error")
	def test_FullName_other(self):
		result = FullName.FullName([], [])
		self.assertEqual(result, "Error")
		


if __name__ == "__main__":
        unittest.main()




