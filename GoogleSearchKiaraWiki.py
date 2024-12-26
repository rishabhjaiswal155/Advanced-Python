from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
class AutomateGoogleKiara(unittest.TestCase):
    def setUp(self):
        print("setUp method executes...")
        global driver
        driver=webdriver.Chrome()
        driver.maximize_window()
        time.sleep(2)
        driver.get('https://www.google.co.in')
        print(driver.title)
        print(driver.current_url)
        time.sleep(2)
        
    def test_kiaraSearch(self):
        print("test_kiaraSearch method executes...")
        driver.find_element("class name",'gLFyf').send_keys('Kiara Advani')
        time.sleep(5)
        driver.find_element("class name",'gNO89b').click()
        time.sleep(20)
        driver.find_element(By.CLASS_NAME,'DKV0Md').click()
        time.sleep(10)
        print(driver.title)
        print(driver.current_url)
        
    def tearDown(self):
        print("tearDown method executes...")
        driver.close()
        
unittest.main()
        