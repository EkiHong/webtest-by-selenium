# -*- coding: utf-8 -*-

import sys
sys.path.append(r'D:\AsusCloud_webtest')
import unittest
from time import sleep
from selenium import webdriver
from asus.test_case.page_obj.BasePage import Page
from asus.test_case.models import screenshot
from asus.test_case.page_obj.MySyncFolderPage import MySyncPage
from asus.test_case.page_obj.loginPage import login
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from package import HTMLTestRunner
import os
from xmlrunner import xmlrunner


class MySyncFolderCase(unittest.TestCase):
    prefs = {'profile.default_content_setting_values': {'notifications': 2}}

    # def setUp(self):
    #     self.options = webdriver.ChromeOptions()
    #     self.options.add_experimental_option('prefs', self.prefs)
    #     self.driver = webdriver.Chrome(chrome_options=self.options)
    #     self.driver.get("https://www.asuswebstorage.com/navigate/a/#/login")
    #     self.driver.maximize_window()
    #     self.login()

    @classmethod
    def setUpClass(cls):
        cls.options = webdriver.ChromeOptions()
        cls.options.add_experimental_option('prefs', cls.prefs)
        cls.driver = webdriver.Chrome(chrome_options=cls.options)
        # cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.login()

        '''有需要測試的項目，開頭以test為開頭即可 '''
    @classmethod
    def login(cls):
        username = "username"
        password = "password"
        login_page = login(driver=cls.driver)
        login_page.user_login(username, password)


    def test_uploadfile(self):
        MySyncFolder = MySyncPage(driver=self.driver)
        MySyncFolder.add_butn()
        MySyncFolder.upload_file(uploadfile=r'D:\AsusCloud_webtest\upload_data\test_file\test_add_file_2')
        sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        file_text = WebDriverWait(self.driver, 70).until(EC.presence_of_element_located((By.XPATH, '//td[@class="text"]/span/a[contains(text(),"test_add_file_2.exe")]'))).text
        sleep(3)
        print(file_text)
        self.assertEqual(file_text, "test_add_file_2.exe")
        sleep(2)
        MySyncFolder.assign_file()
        MySyncFolder.delete_butn()
        sleep(1)
        self.driver.refresh()

    def test_uploadfolder(self):
        MySyncFolder = MySyncPage(driver=self.driver)
        MySyncFolder.add_butn()
        sleep(1)
        MySyncFolder.upload_folder(uploadfolder=r'D:\AsusCloud_webtest\upload_data\test_add_newfolder')
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="accordion"]/div/div[1]/div/span/i')))  # 等待上傳成功
        except:
            screenshot.insert_image(self.driver)
            print("folder upload over 90 secs")
        folder_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//td[@class="text"]/span/a[contains(text(),"test_add_newfolder")]'))).text
        self.assertEqual(folder_text, "test_add_newfolder")
        screenshot.insert_image(self.driver)
        sleep(1)
        MySyncFolder.assign_folder()
        MySyncFolder.delete_butn()
        sleep(1)
        self.driver.refresh()

    def test_addnewfolder(self):
        MySyncFolder = MySyncPage(driver=self.driver)
        MySyncFolder.add_butn()
        sleep(1)
        newfolder_name = "newfolder"
        MySyncFolder.add_newfolder(newfolder_name)
        newfolder_name_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//td[@class="text"]/span/a[contains(text(),"newfolder")]'))).text
        self.assertEqual(newfolder_name_text, "newfolder")
        screenshot.insert_image(self.driver)
        sleep(1)
        MySyncFolder.assign_addnewfolder()
        MySyncFolder.delete_butn()
        sleep(1)  # 出於檢查
        self.driver.refresh()
        # account = 0
        # for i in self.driver.find_elements_by_xpath('//*[@id="responsivetable"]/tbody/tr/td[1]/label'):
        #     account = account + 1
        # list = []
        # for index in range(1, account+1, 1):
        #     object = self.driver.find_element_by_xpath('//*[@id="responsivetable"]/tbody/tr[' + str(index) + ']/td[3]/span/a').text
        #     list.append(object)
        # self.assertNotIn("test_add_newfolder", list)

    def test_download_folder(self):
        MySyncFolder = MySyncPage(driver=self.driver)
        MySyncFolder.add_butn()
        # sleep(1)
        newfolder_name = "test_add_newfolder"
        MySyncFolder.add_newfolder(newfolder_name)
        newfolder_name_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//td[@class="text"]/span/a[contains(text(),"test_add_newfolder")]'))).text
        self.assertEqual(newfolder_name_text, "test_add_newfolder")
        # sleep(1)
        MySyncFolder.assign_folder()
        MySyncFolder.downloand_butn()
        check = 'download'
        times = 0
        download_dir = r"C:\Users\Eki\Downloads"
        files = os.listdir(download_dir)
        while check != 'finish':
            check_list = []
            for file in files:
                check_list.append(file)
            if 'Test.7z' in check_list:
                check = 'finish'
                print(files)
            else:
                times = times + 1
                print("下載%s秒", times)
        self.driver.refresh()
        MySyncFolder.assign_folder()
        MySyncFolder.delete_butn()
        sleep(2)
        # # check_folder_delete = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="responsivetable"]/tbody/tr/td[3]/span/a')))
        # list = []
        # for check in self.driver.find_elements_by_xpath('//*[@id="responsivetable"]/tbody/tr/td[3]/span/a'):  # 回傳值為list，不能直接獲取text，需用for迴圈將其text一一取出
        #     check = check.text
        #     list.append(check)
        # self.assertNotIn("test_add_newfolder", list)

    def test_delete_folder(self):
        MySyncFolder = MySyncPage(driver=self.driver)
        MySyncFolder.add_butn()
        newfolder_name = "test_add_newfolder"
        MySyncFolder.add_newfolder(newfolder_name)
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//td[@class="text"]/span/a[contains(text(),"test_add_newfolder")]'))).text
        sleep(1)
        MySyncFolder.assign_folder()
        sleep(1)
        MySyncFolder.delete_butn()
        sleep(1)
        list = []
        for check in self.driver.find_elements_by_xpath('//*[@id="responsivetable"]/tbody/tr/td[3]/span/a'):  # 回傳值為list，不能直接獲取text，需用for迴圈將其text一一取出
            check = check.text
            list.append(check)
        self.assertNotIn("test_add_newfolder", list)

    def test_rename_folder(self):
        MySyncFolder = MySyncPage(driver=self.driver)
        newfolder_name = "test_add_newfolder"
        MySyncFolder.add_butn()
        MySyncFolder.add_newfolder(newfolder_name)
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//td[@class="text"]/span/a[contains(text(),"test_add_newfolder")]'))).text
        MySyncFolder.assign_folder()
        MySyncFolder.multiple_click()
        rename = "test_rename"
        MySyncFolder.rename_butn(rename)
        sleep(1)
        list = []
        for check in self.driver.find_elements_by_xpath('//*[@id="responsivetable"]/tbody/tr/td[3]/span/a'):  # 回傳值為list，不能直接獲取text，需用for迴圈將其text一一取出
            check = check.text
            list.append(check)
        self.assertIn("test_rename", list)
        sleep(1)
        self.driver.find_element_by_xpath('//td[@class="text"]/span/a[contains(text(),"test_rename")]/../../..//label/input').click()
        MySyncFolder.delete_butn()


    # def tearDown(self):
    #     self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    # test_uploadfolder、test_addnewfolder ，需要優化 assign_folder 的 function

    suite = unittest.TestSuite()
    suite.addTest(MySyncFolderCase("test_download_folder"))
    suite.addTest(MySyncFolderCase("test_delete_folder"))
    suite.addTest(MySyncFolderCase("test_addnewfolder"))
    suite.addTest(MySyncFolderCase("test_uploadfile"))
    suite.addTest(MySyncFolderCase("test_rename_folder"))
    suite.addTest(MySyncFolderCase("test_uploadfolder")) # 使用jenkins時，會因為瀏覽器不是第一位的狀態，導致pyautogui無法正常操作

    # xml report output
    # xmlrunner.XMLTestRunner(output=r'D:\AsusCloud_webtest\asus\test_report').run(suite)
    # xmlrunner.XMLTestRunner(output=r'C:\Users\Eki\.jenkins\workspace\ASUSCLOUD_Navigate_Test\reports').run(suite) #xml報告存在jenkins目錄下，讓DashBoard可成功輸出


    # html report output
    file_path = r'D:\AsusCloud_webtest\asus\test_report\test_MySyncFolder_result.html'
    fp = open(file_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title="ASUSCLOUD Test Report",
        description="使用者案例執行情況:")
    runner.run(suite)
    fp.close()
