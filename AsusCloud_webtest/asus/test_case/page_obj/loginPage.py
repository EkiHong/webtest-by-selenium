from asus.test_case.page_obj.BasePage import Page
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class login(Page):

    '''
       使用者登入頁面
       '''

    #帳號、密碼、登入按鈕 元素定位
    login_username_loc = (By.XPATH, '/html/body/app-root/app-official-layout/app-login/section/div/div/div[2]/form/div[1]/input')
    login_password_loc = (By.XPATH, '//*[@id="page-top"]/app-root/app-official-layout/app-login/section/div/div/div[2]/form/div[2]/input')
    login_button_loc = (By.XPATH, '//div[@class="text-center mt-30 mb-20"]/button[@gtm="loginpage_btn_login"]')


    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    def user_login(self, username, password):
        self.open()
        sleep(1)
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    url = 'https://www.asuswebstorage.com/navigate/a/#/login'
    username = "username"
    password = "password"

    Login = login(driver)
    Login.open()
    Login.user_login(username, password)
    sleep(1)
    driver.close()



