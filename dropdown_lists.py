import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pyunitreport import HTMLTestRunner
from dotenv import load_dotenv
import os

load_dotenv()

class RegisterNewUser(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        chrome = Service(r"/usr/bin/chromedriver")
        cls.driver = webdriver.Chrome(service=chrome)
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")
    
    def test_select_language(self):
        exp_options = ['English', 'French', 'German']
        act_options = []

        select_language = Select(self.driver.find_element(By.ID, "select-language"))

        self.assertEqual(3, len(select_language.options))

        for option in select_language.options:
            act_options.append(option.text)

        self.assertListEqual(exp_options, act_options)

        self.assertEqual('English', select_language.first_selected_option.text)

        select_language.select_by_visible_text('German')

        self.assertTrue('store=german' in self.driver.current_url)

        # It's necessary to use Select again , otherwise, the next test will fail
        select_language = Select(self.driver.find_element(By.ID, "select-language"))

        select_language.select_by_index(0)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(3)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'find-elements-report'))

