import unittest
from tinyhands.bug import Bug

class TestBugClass(unittest.TestCase):

	def test_bug_init(self):
		b = Bug()
		self.assertIsInstance(b, Bug)

if __name__ == '__main__':
	unittest.main()