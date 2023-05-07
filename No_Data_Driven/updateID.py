import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.common.exceptions import NoSuchElementException

baseUrl = "https://mybk.hcmut.edu.vn/stinfo/"
id = "352611458"
place = "Tỉnh An Giang"
date = "06/12/2016"


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

    def teardown_method(self):
        self.driver.quit()

    # def get_element_wait(self, NameOfObject):
    #     try:
    #         item = WebDriverWait(self.driver, 15).until(
    #             EC.presence_of_element_located((By.ID, NameOfObject)))
    #         item.click()
    #     except TimeoutException as e:
    #         print("Couldn't Click by name on: " + str(NameOfObject))
    #         pass

    def test_1(self):
        self.driver.get(baseUrl)

        self.driver.find_element(
            By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div[1]/a').click()
        time.sleep(7)

        # self.get_element_wait("menu-cmnd-edit")

        # id_in = self.driver.find_element(By.ID, "cmndEditCMND")
        # place_in = self.driver.find_element(By.ID, "cmndnoicapEditCMND")
        # date_in = self.driver.find_element(By.ID, "cmndngaycapEditCMND")

        # id_in.send_keys(id)
        # place_in.send_keys(place)
        # date_in.send_keys(date)
        idObj = self.driver.find_element(By.ID, "cmndEditCMND")
        placeObj = self.driver.find_element(By.ID, "cmndnoicapEditCMND")
        dateObj = self.driver.find_element(By.ID, "cmndngaycapEditCMND")
        self.driver.execute_script(
            f"arguments[0].setAttribute('value',{id})", idObj)
        self.driver.execute_script(
            "arguments[0].setAttribute('value',{place})", placeObj)
        self.driver.execute_script(
            f"arguments[0].setAttribute('value',{date})", dateObj)

        self.driver.find_element(By.ID, "btn_save_cmnd").click()

        self.get_element_wait("btn_save_cmnd")

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
