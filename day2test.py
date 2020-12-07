import unittest
from advent2 import part2

class ActivityTests(unittest.TestCase):
		
		def test1(self):
			pw = [{"p1":1, "p2":3, "char":"a", "pw":"abcde"}]
			self.assertTrue(part2(pw))

		def test2(self):
			pw = [{"p1":1, "p2":3, "char":"b", "pw":"cdefg"}]
			self.assertFalse(part2(pw))

		def test3(self):
			pw = [{"p1":2, "p2":9, "char":"c", "pw":"ccccccccc"}]
			self.assertFalse(part2(pw))

if __name__ == "__main__":
	unittest.main()