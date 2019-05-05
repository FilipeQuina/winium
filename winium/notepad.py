# coding: utf-8

import unittest
from selenium import webdriver
class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://localhost:9999',
            desired_capabilities={
                "debugConnectToRunningApp": 'false',
                "app": r"C:/Program Files (x86)/Notepad++/notepad++.exe"
        })
    def test_untitled_test_case(self):
        self.driver.find_element_by_class_name("Scintilla").send_keys("ola")

if __name__ == '__main__':
    unittest.main()