from selenium import webdriver
import unittest

class PageTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
	
#	def tearDown(self):
#		set.browser.quit()
	
	def test_browser_title(self):
		self.browser.get('http://localhost:8000')
#		self.assertIn('His Grace Church', self.browser.title)
#		self.fail('Finish the test NOW!')
		
if __name__ == '__main__':
	unittest.main(warnings='ignore')
browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000')
