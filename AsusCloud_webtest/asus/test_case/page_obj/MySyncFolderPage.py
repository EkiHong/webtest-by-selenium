from asus.test_case.page_obj.BasePage import Page
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from asus.test_case.page_obj.loginPage import login
import os
import pyautogui
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MySyncPage(Page):
    '''
        MySyncFolder 頁面元素定位
    '''

    # "新增"、"新增資料夾"、"上傳檔案"、"上傳資料夾"、"下載"，可持續新增
    '''
        新增鈕
        新增資料夾
        新增資料夾_請輸入資料夾名稱
        新增資料夾_確定
        新增資料夾_取消
        上傳檔案
        上傳資料夾
        所有檔案、資料夾的總數
        所有檔案、資料夾的名稱
        下載鈕
        下載命名
        下載命名_確定鈕
        刪除鈕
        刪除鈕_確定鈕
        指定"test_add_newfolder"資料夾
        指定"test_add_file_2"檔案
        指定"test_folder"資料夾
            '''
    add_butn_loc = (By.XPATH, '//*[@id="breadcrumb"]/ul[2]/li[4]/a/img')
    add_newfolder_loc = (By.XPATH, '//ul[@class="dropdown-menu tool-other"]//img[@src="assets/img/icon/30px/svg/icon_folder_add-38011ba944.svg"]')
    add_newfolder_name_loc = (By.XPATH, '//*[@id="page-top"]/bs-modal[1]/div/div/bs-modal-body/div/input')
    add_newfolder_determine_loc = (By.XPATH, '//*[@id="page-top"]/bs-modal[1]/div/div/bs-modal-footer/div/button[2]')
    add_newfolder_cancel_loc = (By.XPATH, '//bs-modal[@class="fade modal in"]//div[@class="modal-content"]//div[@class="modal-footer"]/button[@_ngcontent-c12][@class="btn no-padding no-margin bg-grey btn-modal-l"]')
    upload_file_loc = (By.XPATH, '//ul[@class="dropdown-menu tool-other"]//li[3]/label/span')
    upload_folder_loc = (By.XPATH, '//ul[@class="dropdown-menu tool-other"]//li[4]/label/span')

    all_of_checkbox_loc = (By.XPATH, '//*[@id="responsivetable"]/tbody/tr/td[1]/label')
    all_of_file_folder_name_loc = (By.XPATH, '//*[@id="responsivetable"]/tbody/tr/td[3]/span/a')
    # random_of_checkbox_loc = (By.XPATH, '//*[@id="responsivetable"]/tbody/tr[' + str(self.random_select()) + ']/td[1]/label')
    download_btn_loc = (By.XPATH, '//div[@id="breadcrumb"]/ul[@class="tool col-xs-5"]/li[6]/a')
    downloadpackage_name_btn_loc = (By.XPATH, '//*[@id="page-top"]/bs-modal[13]/div/div/bs-modal-body/div/input')
    downloadpackage_determine_loc = (By.XPATH, '//*[@id="page-top"]/bs-modal[13]/div/div/bs-modal-footer/div/button[2]')
    delete_btn_loc = (By.XPATH, '//*[@id="breadcrumb"]/ul[2]/li[7]/a')
    delete_determine_loc = (By.XPATH, '//*[@id="page-top"]/bs-modal[9]/div/div/bs-modal-footer/div/button[2]')
    assign_addnewfolder_loc = (By.XPATH, '//td[@class="text"]/span/a[contains(text(),"newfolder")]/../../..//label')
    assign_file_loc = (By.XPATH, '//td[@class="text"]/span/a[contains(text(),"test_add_file_2")]/../../..//label')
    assign_folder_loc = (By.XPATH, '//td[@class="text"]/span/a[contains(text(),"test_add_newfolder")]/../../..//label')
    multiple_butn_loc = (By.XPATH, '//*[@id="breadcrumb"]/ul[2]/li[5]/a')
    rename_butn_loc = (By.XPATH, '//*[@id="breadcrumb"]/ul[2]/li[5]/ul/li[6]/a')
    rename_box_loc = (By.XPATH, '//*[@id="page-top"]/bs-modal[2]/div/div/bs-modal-body/div/input')
    rename_determine_loc = (By.XPATH, '//*[@id="page-top"]/bs-modal[2]/div/div/bs-modal-footer/div/button[2]')

    def add_butn(self):
        self.find_element(*self.add_butn_loc).click()

    def add_newfolder(self, newfolder_name):
        self.find_element(*self.add_newfolder_loc).click()
        sleep(1)
        self.find_element(*self.add_newfolder_name_loc).clear()
        self.find_element(*self.add_newfolder_name_loc).send_keys(newfolder_name)
        self.find_element(*self.add_newfolder_determine_loc).click()

    def upload_file(self, uploadfile):
        self.find_element(*self.upload_file_loc).click()
        sleep(1)
        os.system('D:\\AsusCloud_webtest\\autoit_exe\\upload_file.exe %s' % uploadfile)

    def upload_folder(self, uploadfolder):
        self.find_element(*self.upload_folder_loc).click()
        sleep(1)
        os.system('D:\\AsusCloud_webtest\\autoit_exe\\upload_folder.exe %s' % uploadfolder)
        pyautogui.FAILSAFE = False
        sleep(0.5)
        pyautogui.press('left')
        sleep(0.5)
        pyautogui.press('enter')


    # 指定選取資料夾 ex: "test_add_newfolder"
    def assign_addnewfolder(self):
        self.find_element(*self.assign_addnewfolder_loc).click()

    def assign_file(self):
        self.find_element(*self.assign_file_loc).click()

    def assign_folder(self):
        self.find_element(*self.assign_folder_loc).click()

    # 下載(包含打包下載)
    def downloand_butn(self):
        try:
            self.find_element(*self.download_btn_loc).click()
            self.find_element(*self.downloadpackage_name_btn_loc).is_displayed()
            self.find_element(*self.downloadpackage_name_btn_loc).clear()
            self.find_element(*self.downloadpackage_name_btn_loc).send_keys("Test")
            self.find_element(*self.downloadpackage_determine_loc).click()
            print("正在進行打包下載")
        except:
            print("正在進行一般下載")
            pass

    def delete_butn(self):
        self.find_element(*self.delete_btn_loc).click()
        sleep(1.5)
        self.find_element(*self.delete_determine_loc).click()

    def multiple_click(self):
        self.find_element(*self.multiple_butn_loc).click()

    def rename_butn(self, rename):
        self.find_element(*self.rename_butn_loc).click()
        self.find_element(*self.rename_box_loc).clear()
        self.find_element(*self.rename_box_loc).send_keys(rename)
        self.find_element(*self.rename_determine_loc).click()



if __name__ == '__main__':
    driver = webdriver.Chrome()
    # base_url = 'https://www.asuswebstorage.com'
    username = "username"
    passwoed = "password"

    Login = login(driver)
    Login.open()
    Login.user_login(username, passwoed)

    MySync = MySyncPage(driver)
    sleep(1)
    MySync.add_butn()
    sleep(1)
    # MySync.upload_file(uploadfile='D:\\AsusCloud_webtest\\upload_data\\test_file\\test_add_file_2')
    # sleep(1)
    MySync.upload_folder(uploadfolder='D:\\AsusCloud_webtest\\upload_data\\test_folder')
