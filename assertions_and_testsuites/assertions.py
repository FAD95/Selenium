import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class AssertionsTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        chrome = Service(r"/usr/bin/chromedriver")
        cls.driver = webdriver.Chrome(service=chrome)
        driver = cls.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
    
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, "q"))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, "select-language"))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as variable:
            return False
        return True

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'find-elements-report'))

