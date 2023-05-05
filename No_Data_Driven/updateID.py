import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class TestUpdateID(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def get_element_wait(self, element_id, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
        except TimeoutException:
            err = 'Element with id {} could not be found!'
            raise Exception(err.format(element_id))
    
    def test_1(self): 
        self.driver.get('https://sso.hcmut.edu.vn/cas/login?service=http%3A%2F%2Fmybk.hcmut.edu.vn%2Fstinfo%2F')

        self.driver.find_element(By.NAME,"username").send_keys("hoang.nguyen")
        self.driver.find_element(By.NAME,"password").send_keys("123456")
        self.driver.find_element(By.NAME,"submit").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/a').click()
        time.sleep(10)

        self.driver.find_element(By.ID, "menu-cmnd-edit").click()
        time.sleep(10)
        
        self.driver.execute_script("arguments[0].setAttribute('value','202001888')", self.driver.find_element(By.ID,"cmndEditCMND"))
        self.driver.execute_script("arguments[0].setAttribute('value','Đồng Nai')", self.driver.find_element(By.ID,"cmndnoicapEditCMND"))
        self.driver.execute_script("arguments[0].setAttribute('value','2021')", self.driver.find_element(By.ID,"cmndngaycapEditCMND"))
        
        self.driver.find_element(By.ID,"btn_save_cmnd").click()
        time.sleep(10)

        self.driver.find_element(By.XPATH,'/html/body/div[5]')
    
    def test_2(self): 
        self.driver.get('https://sso.hcmut.edu.vn/cas/login?service=http%3A%2F%2Fmybk.hcmut.edu.vn%2Fstinfo%2F')

        self.driver.find_element(By.NAME,"username").send_keys("hoang.nguyen")
        self.driver.find_element(By.NAME,"password").send_keys("123456")
        self.driver.find_element(By.NAME,"submit").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/a').click()
        time.sleep(10)

        self.driver.find_element(By.ID, "menu-cmnd-edit").click()
        time.sleep(10)
        
        self.driver.execute_script("arguments[0].setAttribute('value','')", self.driver.find_element(By.ID,"cmndEditCMND"))
        self.driver.execute_script("arguments[0].setAttribute('value','Đồng Nai')", self.driver.find_element(By.ID,"cmndnoicapEditCMND"))
        self.driver.execute_script("arguments[0].setAttribute('value','2021')", self.driver.find_element(By.ID,"cmndngaycapEditCMND"))
        self.driver.find_element(By.ID,"btn_save_cmnd").click()

        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME,"disabled")

    def test_3(self): 
        self.driver.get('https://sso.hcmut.edu.vn/cas/login?service=http%3A%2F%2Fmybk.hcmut.edu.vn%2Fstinfo%2F')

        self.driver.find_element(By.NAME,"username").send_keys("hoang.nguyen")
        self.driver.find_element(By.NAME,"password").send_keys("123456")
        self.driver.find_element(By.NAME,"submit").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/a').click()
        time.sleep(10)

        self.driver.find_element(By.ID, "menu-cmnd-edit").click()
        time.sleep(10)
        
        self.driver.execute_script("arguments[0].setAttribute('value','202001888')", self.driver.find_element(By.ID,"cmndEditCMND"))
        self.driver.execute_script("arguments[0].setAttribute('value','')", self.driver.find_element(By.ID,"cmndnoicapEditCMND"))
        self.driver.execute_script("arguments[0].setAttribute('value','2021')", self.driver.find_element(By.ID,"cmndngaycapEditCMND"))
        self.driver.find_element(By.ID,"btn_save_cmnd").click()

        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME,"disabled")
    
    def test_4(self): 
        self.driver.get('https://sso.hcmut.edu.vn/cas/login?service=http%3A%2F%2Fmybk.hcmut.edu.vn%2Fstinfo%2F')

        self.driver.find_element(By.NAME,"username").send_keys("hoang.nguyen")
        self.driver.find_element(By.NAME,"password").send_keys("123456")
        self.driver.find_element(By.NAME,"submit").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/a').click()
        time.sleep(10)

        self.driver.find_element(By.ID, "menu-cmnd-edit").click()
        time.sleep(10)
        
        self.driver.execute_script("arguments[0].setAttribute('value','202001888')", self.driver.find_element(By.ID,"cmndEditCMND"))
        self.driver.execute_script("arguments[0].setAttribute('value','Đồng Nai')", self.driver.find_element(By.ID,"cmndnoicapEditCMND"))
        self.driver.execute_script("arguments[0].setAttribute('value','')", self.driver.find_element(By.ID,"cmndngaycapEditCMND"))
        self.driver.find_element(By.ID,"btn_save_cmnd").click()

        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME,"disabled")

    def test_5(self): 
        self.driver.get('https://sso.hcmut.edu.vn/cas/login?service=http%3A%2F%2Fmybk.hcmut.edu.vn%2Fstinfo%2F')

        self.driver.find_element(By.NAME,"username").send_keys("hoang.nguyen")
        self.driver.find_element(By.NAME,"password").send_keys("123456")
        self.driver.find_element(By.NAME,"submit").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/a').click()
        time.sleep(10)

        self.driver.find_element(By.ID, "menu-cmnd-edit").click()
        time.sleep(10)
        
        self.driver.execute_script("arguments[0].setAttribute('value','')", self.driver.find_element(By.ID,"cmndEditCMND"))
        self.driver.execute_script("arguments[0].setAttribute('value','')", self.driver.find_element(By.ID,"cmndnoicapEditCMND"))
        self.driver.execute_script("arguments[0].setAttribute('value','')", self.driver.find_element(By.ID,"cmndngaycapEditCMND"))
        self.driver.find_element(By.ID,"btn_save_cmnd").click()

        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME,"disabled")
    
        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
