from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
class TestGoogleSearchKiara:
    @pytest.fixture(scope='module')
    def setUpClasstearDownClass(self):
        global driver
        driver=webdriver.Chrome()
        driver.maximize_window()
        time.sleep(2)
        driver.get('https://www.google.co.in')
        print(driver.title)
        print(driver.current_url)
        time.sleep(2)
        yield
        driver.close()
        
    def test_kiaraSearch(self,setUpClasstearDownClass):
        print("test_kiaraSearch method executes...")
        driver.find_element("class name",'gLFyf').send_keys('Kiara Advani')
        time.sleep(5)
        driver.find_element("class name",'gNO89b').click()
        time.sleep(20)
        driver.find_element(By.CLASS_NAME,'DKV0Md').click()
        time.sleep(10)
        print(driver.title)
        print(driver.current_url)
        
   
        