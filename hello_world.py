import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    
    def setUp(self):
        chrome = Service(r"/usr/bin/chromedriver")
        self.driver = webdriver.Chrome(service=chrome)
        driver = self.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get('http://www.platzi.com')
    
        # def test_visit_wikipedia(self):
        #     self.driver.get('http://www.wikipedia.org')
    
    def tearDown(self):
       self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))

