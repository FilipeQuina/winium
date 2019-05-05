# coding: utf-8
from selenium import webdriver
driver = webdriver.Remote(
    command_executor='http://localhost:9999',
    desired_capabilities={
        "debugConnectToRunningApp": 'false',
        "app": r"C:/Program Files (x86)/Zoiper5/Zoiper5.exe"
    })

driver.find_element_by_id("33943904").send_keys("123")
print("ok")
#driver.close()