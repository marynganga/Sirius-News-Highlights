import unittest
import sys
sys.path.append('./app')
from models import Article

class TestArticle(unittest.TestCase):
	'''
	Test Case to test the behaviour of the Article Model
	Args:
		unittest.TestCase - helps in creating Test Cases
	'''
	def setUp(self):
		'''
		Inbuilt function that runs before each test is executed
		'''
		self.new_article = Article("Sarah Jeong","How the judge on Oracle v. Google taught himself to code","Judge William Alsup taught himself to code for fun in the 1980s. Now he's the judge on Silicon Valley's biggest cases.","https://www.theverge.com/2017/10/19/16503076/oracle-vs-google-judge-william-alsup-interview-waymo-uber","https://cdn.vox-cdn.com/thumbor/yWidf1mAgXfNhxEWbkDc8p6SJjE=/0x146:2040x1214/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/9389895/sjeong_170510_2032_0003.jpg","2017-10-19T14:57:19Z")

	def test_isArticleInstance(self):
		'''
		Function to test if the object created in the setup is indeed a Source Object
		'''
		self.assertTrue(isinstance(self.new_article,Article))
		
if __name__ == '__main__':
	unittest.main(verbosity=2)