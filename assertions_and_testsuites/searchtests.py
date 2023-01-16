import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class SearchTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        chrome = Service(r"/usr/bin/chromedriver")
        cls.driver = webdriver.Chrome(service=chrome)
        driver = cls.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
    
    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, "q")
        search_field.clear()

        search_field.send_keys("tee")
        search_field.submit()
    
    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, "q")
        search_field.clear()

        search_field.send_keys("salt shaker")
        search_field.submit()

        products = driver.find_elements(By.XPATH, "//h2[@class='product-name']/a")
        self.assertEqual(1, len(products))


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

