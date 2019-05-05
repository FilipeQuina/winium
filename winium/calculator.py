# coding: utf-8

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://localhost:9999',
            desired_capabilities={
                "debugConnectToRunningApp": 'false',
                "app": r"C:/windows/system32/calc.exe"
        })
    def test_untitled_test_case(self):
        driver = self.driver
        windown = driver.find_element_by_name("Calculadora")
        print("1")
        windown.find_element_by_name("Um").click()
        windown.find_element_by_name("Mais").click()
        windown.find_element_by_name("Um").click()
        windown.find_element_by_name("Igual a").click()
if __name__ == '__main__':
    unittest.main()