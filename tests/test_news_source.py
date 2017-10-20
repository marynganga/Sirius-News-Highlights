import unittest
import sys
sys.path.append('./app')
from models import Source

class TestSource(unittest.TestCase):
	'''
	Test Case to test the behaviour of the Source Model
	Args:
		unittest.TestCase - helps in creating Test Cases
	'''
	def setUp(self):
		'''
		Inbuilt function that runs before each test is executed
		'''
		self.new_source = Source('bloomberg','Bloomberg','Bloomberg delivers business and markets news, data, analysis, and video to the world, featuring stories from Businessweek and Bloomberg News.','http://www.bloomberg.com','business')

	def test_isSouceInstance(self):
		'''
		Function to test if the object created in the setup is indeed a Source Object
		'''
		self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
	unittest.main(verbosity=2)