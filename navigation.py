import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
from time import sleep


class CompareProducts(unittest.TestCase):
    """Accept or dismiss alert pop-ups

    Args:
        unittest (): The class that contains the test methods
    """

    @classmethod
    def setUpClass(cls):
        chrome = Service(r"/usr/bin/chromedriver")
        cls.driver = webdriver.Chrome(service=chrome)
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://google.com")

    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()

        driver.back()  # retroceder navegador
        sleep(3)  # espera 3 segundos
        driver.forward()  # avanzar
        sleep(3)
        driver.refresh()  # actualizar página
        sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(3)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='reportes', report_name='find-elements-report'))
