#-*- coding: utf-8 -*-

from selenium import webdriver
from asus.test_case.page_obj.loginPage import login
import unittest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from package import HTMLTestRunner

class LoginCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    #確認網址是否跳轉至MySyncFolder的url
    def test_login1(self):
        url = "https://www.asuswebstorage.com/navigate/a/#/MySync"
        username = "username"
        password = "password"
        login_page = login(driver=self.driver)
        login_page.user_login(username, password)
        self.assertEqual(url, self.driver.current_url)
        time.sleep(3)

    #輸入 帳號為空 密碼正確
    def test_login2(self):
        username = ""
        password = "xxxxxx"
        login_page = login(driver=self.driver)
        login_page.user_login(username, password)
        account_error_icon = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-top"]/app-root/app-official-layout/app-login/section/div/div/div[2]/form/div[1]/span'))).is_displayed()
        self.assertTrue(account_error_icon)

    #輸入 帳號正確 密碼為空
    def test_login3(self):
        username = "xxxxxx"
        password = ""
        login_page = login(driver=self.driver)
        login_page.user_login(username, password)
        password_error_icon = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-top"]/app-root/app-official-layout/app-login/section/div/div/div[2]/form/div[2]/span'))).is_displayed()
        self.assertTrue(password_error_icon)

    #輸入 帳號為空 密碼為空
    def test_login4(self):
        username = ""
        password = ""
        login_page = login(driver=self.driver)
        login_page.user_login(username, password)
        account_error_icon = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-top"]/app-root/app-official-layout/app-login/section/div/div/div[2]/form/div[1]/span'))).is_displayed()
        password_error_icon = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-top"]/app-root/app-official-layout/app-login/section/div/div/div[2]/form/div[2]/span'))).is_displayed()
        self.assertTrue(account_error_icon)
        self.assertTrue(password_error_icon)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(LoginCase("test_login1"))
    suite.addTest(LoginCase("test_login3"))
    suite.addTest(LoginCase("test_login2"))
    suite.addTest(LoginCase("test_login4"))

    file_path = r'D:\AsusCloud_webtest\asus\test_report\test_login_result.html'
    fp = open(file_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title="ASUSCLOUD Test Report",
        description="使用者案例執行情況:")
    runner.run(suite)
    fp.close()


