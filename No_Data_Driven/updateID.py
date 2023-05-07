import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

loginURL = "https://sso.hcmut.edu.vn/cas/login?service=http%3A%2F%2Fmybk.hcmut.edu.vn%2Fstinfo%2F"
username = "tan.lamcs1001"
password = "lnt@H1720"


class TestUpdateID(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def get_element_wait(self, element_id, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(
                # EC.presence_of_element_located((By.ID, element_id))
            )
        except TimeoutException:
            err = 'Element with id {} could not be found!'
            raise Exception(err.format(element_id))

    def test_1(self):
        self.driver.get(loginURL)

        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(5)

        self.driver.find_element(
            By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div[1]/a').click()
        time.sleep(7)

        edit = self.driver.find_element(By.ID, "menu-cmnd-edit")
        time.sleep(1)
        edit.click()
        time.sleep(7)

        self.driver.find_element(By.ID, "cmndEditCMND").send_keys("352611458")
        self.driver.find_element(By.ID,
                                 "cmndnoicapEditCMND").send_keys("Tỉnh An Giang")
        self.driver.find_element(By.ID,
                                 "cmndngaycapEditCMND").send_keys("06/12/2016")

        # self.driver.execute_script(
        #     "arguments[0].setAttribute('value','352611458')", )
        # self.driver.execute_script(
        #     "arguments[0].setAttribute('value','Tỉnh An Giang')", self.driver.find_element(By.ID, "cmndnoicapEditCMND"))
        # self.driver.execute_script("arguments[0].setAttribute('value','06/12/2016')", self.driver.find_element(
        #     By.ID, "cmndngaycapEditCMND"))

        self.driver.find_element(By.ID, "btn_save_cmnd").click()
        time.sleep(10)

        assert self.driver.find_element(
            By.CLASS_NAME, 'bootbox-body') == "Thông tin cmnd của sinh viên đã được lưu!"

    # def test_2(self):
    #     self.driver.get(
    #         'https://sso.hcmut.edu.vn/cas/login?service=http%3A%2F%2Fmybk.hcmut.edu.vn%2Fstinfo%2F')

    #     self.driver.find_element(By.NAME, "username").send_keys(username)
    #     self.driver.find_element(By.NAME, "password").send_keys(password)
    #     self.driver.find_element(By.NAME, "submit").click()
    #     time.sleep(1)

    #     self.driver.find_element(
    #         By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/a').click()
    #     time.sleep(10)

    #     self.driver.find_element(By.ID, "menu-cmnd-edit").click()
    #     time.sleep(10)

    #     self.driver.execute_script(
    #         "arguments[0].setAttribute('value','')", self.driver.find_element(By.ID, "cmndEditCMND"))
    #     self.driver.execute_script(
    #         "arguments[0].setAttribute('value','Đồng Nai')", self.driver.find_element(By.ID, "cmndnoicapEditCMND"))
    #     self.driver.execute_script("arguments[0].setAttribute('value','2021')", self.driver.find_element(
    #         By.ID, "cmndngaycapEditCMND"))
    #     self.driver.find_element(By.ID, "btn_save_cmnd").click()

    #     time.sleep(1)
    #     self.driver.find_element(By.CLASS_NAME, "disabled")

    # def test_3(self):
    #     self.driver.get(
    #         'https://sso.hcmut.edu.vn/cas/login?service=http%3A%2F%2Fmybk.hcmut.edu.vn%2Fstinfo%2F')

    #     self.driver.find_element(By.NAME, "username").send_keys(username)
    #     self.driver.find_element(By.NAME, "password").send_keys(password)
    #     self.driver.find_element(By.NAME, "submit").click()
    #     time.sleep(1)

    #     self.driver.find_element(
    #         By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/a').click()
    #     time.sleep(10)

    #     self.driver.find_element(By.ID, "menu-cmnd-edit").click()
    #     time.sleep(10)

    #     self.driver.execute_script(
    #         "arguments[0].setAttribute('value','202001888')", self.driver.find_element(By.ID, "cmndEditCMND"))
    #     self.driver.execute_script(
    #         "arguments[0].setAttribute('value','')", self.driver.find_element(By.ID, "cmndnoicapEditCMND"))
    #     self.driver.execute_script("arguments[0].setAttribute('value','2021')", self.driver.find_element(
    #         By.ID, "cmndngaycapEditCMND"))
    #     self.driver.find_element(By.ID, "btn_save_cmnd").click()

    #     time.sleep(1)
    #     self.driver.find_element(By.CLASS_NAME, "disabled")

    # def test_4(self):
    #     self.driver.get(
    #         'https://sso.hcmut.edu.vn/cas/login?service=http%3A%2F%2Fmybk.hcmut.edu.vn%2Fstinfo%2F')

    #     self.driver.find_element(By.NAME, "username").send_keys(username)
    #     self.driver.find_element(By.NAME, "password").send_keys(password)
    #     self.driver.find_element(By.NAME, "submit").click()
    #     time.sleep(1)

    #     self.driver.find_element(
    #         By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/a').click()
    #     time.sleep(10)

    #     self.driver.find_element(By.ID, "menu-cmnd-edit").click()
    #     time.sleep(10)

    #     self.driver.execute_script(
    #         "arguments[0].setAttribute('value','202001888')", self.driver.find_element(By.ID, "cmndEditCMND"))
    #     self.driver.execute_script(
    #         "arguments[0].setAttribute('value','Đồng Nai')", self.driver.find_element(By.ID, "cmndnoicapEditCMND"))
    #     self.driver.execute_script("arguments[0].setAttribute('value','')", self.driver.find_element(
    #         By.ID, "cmndngaycapEditCMND"))
    #     self.driver.find_element(By.ID, "btn_save_cmnd").click()

    #     time.sleep(1)
    #     self.driver.find_element(By.CLASS_NAME, "disabled")

    # def test_5(self):
    #     self.driver.get(
    #         'https://sso.hcmut.edu.vn/cas/login?service=http%3A%2F%2Fmybk.hcmut.edu.vn%2Fstinfo%2F')

    #     self.driver.find_element(By.NAME, "username").send_keys(username)
    #     self.driver.find_element(By.NAME, "password").send_keys(password)
    #     self.driver.find_element(By.NAME, "submit").click()
    #     time.sleep(1)

    #     self.driver.find_element(
    #         By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/a').click()
    #     time.sleep(10)

    #     self.driver.find_element(By.ID, "menu-cmnd-edit").click()
    #     time.sleep(10)

    #     self.driver.execute_script(
    #         "arguments[0].setAttribute('value','')", self.driver.find_element(By.ID, "cmndEditCMND"))
    #     self.driver.execute_script(
    #         "arguments[0].setAttribute('value','')", self.driver.find_element(By.ID, "cmndnoicapEditCMND"))
    #     self.driver.execute_script("arguments[0].setAttribute('value','')", self.driver.find_element(
    #         By.ID, "cmndngaycapEditCMND"))
    #     self.driver.find_element(By.ID, "btn_save_cmnd").click()

    #     time.sleep(1)
    #     self.driver.find_element(By.CLASS_NAME, "disabled")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
