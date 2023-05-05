import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select


class TestPrintTranscript(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mybk.hcmut.edu.vn/my/logoutSSO.action")
        self.driver.get('https://sso.hcmut.edu.vn/cas/login?service=https://mybk.hcmut.edu.vn/my/homeSSO.action')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")  
        submitBtn = self.driver.find_element(By.NAME,"submit")  
        
        username.send_keys("dat.luongmason")
        password.send_keys("123456789")
        submitBtn.click()


    def get_element_wait(self, element_id, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
        except TimeoutException:
            err = 'Element with id {} could not be found!'
            raise Exception(err.format(element_id))

    def test_a(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        time.sleep(2)

        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        selectDest.select_by_value("CS2")
        time.sleep(2)

        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        
        confirmInp = self.driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$chk_allow")
        confirmInp.click()
        time.sleep(2)

        submitBtn = self.driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$bnt_xacnhan")
        submitBtn.click()
        time.sleep(2)
        
        notification = self.driver.find_element(By.CSS_SELECTOR,'.msgBoxContent span')
        assert  "Nhập số lượng" == notification.text

    def test_b(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        selectDest.select_by_value("CS2")
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        quantityInp.send_keys("0")
        
        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        
        submitBtn = self.driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$bnt_xacnhan")
        assert not submitBtn.is_enabled()


    def test_c(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        quantityInp.send_keys("0")

        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        
        submitBtn = self.driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$bnt_xacnhan")
        assert not submitBtn.is_enabled()
        

    def test_d(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        selectDest.select_by_value("CS2")
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        
        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        
        submitBtn = self.driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$bnt_xacnhan")
        assert not submitBtn.is_enabled()

    def test_e(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        
        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        
        submitBtn = self.driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$bnt_xacnhan")
        assert not submitBtn.is_enabled()
        

    def test_f(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        selectDest.select_by_value("CS2")
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        quantityInp.send_keys("1")
        
        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        confirmInp.click()
        
        submitBtn = self.driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$bnt_xacnhan")
        submitBtn.click()
        time.sleep(2)
        
        cancelPrint = self.driver.find_element(By.NAME,'ctl00$ContentPlaceHolder1$lst_dsphieu$ctl00$bnt_huyphieu')
        cancelPrint.click()

    def test_g(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        selectDest.select_by_value("CS2")
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        quantityInp.send_keys("2")

        
        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        
        submitBtn = self.driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$bnt_xacnhan")
        assert not submitBtn.is_enabled()
        

    def test_h(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        quantityInp.send_keys("2")

        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        
        submitBtn = self.driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$bnt_xacnhan")
        assert not submitBtn.is_enabled()

    def test_i(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        selectDest.select_by_value("CS2")
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        quantityInp.send_keys("0")

        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        confirmInp.click()
        
        submitBtn = self.driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$bnt_xacnhan")
        submitBtn.click()
        time.sleep(2)
        
        notification = self.driver.find_element(By.CSS_SELECTOR,'.msgBoxContent span')
        assert notification.text == "Số lượng in tối thiểu 1 và tối đa 9"
        

    def test_k(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        
        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        confirmInp.click()
        
        submitBtn = self.driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$bnt_xacnhan")
        submitBtn.click()
        time.sleep(2)
        
        notification = self.driver.find_element(By.CSS_SELECTOR,'.msgBoxContent span')
        assert notification.text == "Chọn nơi nhận kết quả"
        
    def test_j(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        quantityInp.send_keys("0")
        
        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        confirmInp.click()
        
        submitBtn = self.driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$bnt_xacnhan")
        submitBtn.click()
        time.sleep(2)
        
        notification = self.driver.find_element(By.CSS_SELECTOR,'.msgBoxContent span')
        assert notification.text == "Chọn nơi nhận kết quả"
        

    def test_l(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        quantityInp.send_keys("2")
        
        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        confirmInp.click()
        
        submitBtn = self.driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$bnt_xacnhan")
        submitBtn.click()
        time.sleep(2)
        
        notification = self.driver.find_element(By.CSS_SELECTOR,'.msgBoxContent span')
        assert notification.text == "Chọn nơi nhận kết quả"

    def test_m(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        selectDest.select_by_value("CS2")
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        quantityInp.send_keys("a")
        
        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        confirmInp.click()
        
        submitBtn = self.driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$bnt_xacnhan")
        submitBtn.click()
        time.sleep(2)
        
        notification = self.driver.find_element(By.CSS_SELECTOR,'.msgBoxContent span')
        assert notification.text == "Nhập số lượng"
        

    def test_n(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        selectDest.select_by_value("CS2")
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        quantityInp.send_keys("1")

        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        
        submitBtn = self.driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$bnt_xacnhan")
        assert not submitBtn.is_enabled()
        


    def tearDown(self):
        self.driver.get("https://mybk.hcmut.edu.vn/my/homeSSO.action")
        logoutBtn = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/a[1]")
        logoutBtn.click()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()