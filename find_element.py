import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindElements(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        chrome = Service(r"/usr/bin/chromedriver")
        cls.driver = webdriver.Chrome(service=chrome)
        driver = cls.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()

    def test_search_text_field(self):
        search_field = self.driver.find_element(By.ID, "search")
    
    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element(By.NAME, "q")

    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element(By.CLASS_NAME, "input-text")

    def test_search_button_enabled(self):
        search_field = self.driver.find_element(By.CLASS_NAME, "button")

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element(By.CLASS_NAME, 'promos')
        banners = banner_list.find_elements(By.TAG_NAME, 'img')
        self.assertEqual(3, len(banners))
    
    def test_vip_promo(self):
        vip_promo = self.driver.find_elements(By.XPATH, "/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[2]/a/img")
    
    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element(By.CSS_SELECTOR, "div.header-minicart span.icon")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'find-elements-report'))

