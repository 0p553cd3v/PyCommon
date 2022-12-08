import unittest
from src.base import hello_world 

class TestHelloWorld(unittest.TestCase):

	def test_hello_world(self):
		self.assertEqual(print_hello_world(), "Hello world")

unittest.main()