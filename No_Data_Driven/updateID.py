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

baseUrl = "https://mybk.hcmut.edu.vn/stinfo/"


class TestUpdateID(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # dang nhap
        self.driver.get("https://mybk.hcmut.edu.vn/my/logoutSSO.action")
        self.driver.get(
            'https://sso.hcmut.edu.vn/cas/login?service=https://mybk.hcmut.edu.vn/my/homeSSO.action')
        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")
        submitBtn = self.driver.find_element(By.NAME, "submit")
        # ----Submit---#
        username.send_keys("tan.lamcs1001")
        password.send_keys("lnt@H1720")
        submitBtn.click()

    def get_element_wait(self, element_id, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
        except TimeoutException:
            err = 'Element with id {} could not be found!'
            raise Exception(err.format(element_id))

    def test_1(self):
        self.driver.get(baseUrl)

        self.driver.find_element(
            By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div[1]/a').click()
        time.sleep(7)

        self.get_element_wait("menu-cmnd-edit", 10)

        # time.sleep(7)
        self.driver.execute_script(
            "arguments[0].setAttribute('value','')", self.driver.find_element(By.ID, "cmndEditCMND"))
        self.driver.execute_script(
            "arguments[0].setAttribute('value','Đồng Nai')", self.driver.find_element(By.ID, "cmndnoicapEditCMND"))
        self.driver.execute_script("arguments[0].setAttribute('value','2021')", self.driver.find_element(
            By.ID, "cmndngaycapEditCMND"))
        self.driver.find_element(By.ID, "btn_save_cmnd").click()
        time.sleep(10)

        assert self.driver.find_element(
            By.CLASS_NAME, 'bootbox-body').text == "Thông tin cmnd của sinh viên đã được lưu!"

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
