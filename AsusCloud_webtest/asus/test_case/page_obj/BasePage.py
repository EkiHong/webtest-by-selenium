#-*- coding: utf-8 -*-

__author__ = "Eki"
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page():

    base_url = 'https://www.asuswebstorage.com'
    url = '/navigate/a/#/login'

    def __init__(self, driver, base_url=base_url, parent=None, index=None):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30
        self.parent = parent
        self.index = index
        self._type_equality_funcs = {} # 沒加入這行會報"AttributeError: 'login' object has no attribute '_type_equality_funcs'"的錯誤

    def _open(self, url):
        url = self.base_url + self.url
        self.driver.get(url)


    def open(self):
        self._open(self.url)

    # 單一元素顯性等待
    def find_element(self, *loc):
        try:
            return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(loc))
            # return self.driver.find_element(*loc)
        except:
            pass

    # 顯性等待
    def find_elements(self, *loc):
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(loc))
            # return self.driver.find_elements(*loc)
        except:
            pass
            # print("頁面未能找到指定元素")

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self, src):
        return self.driver.execute_script(src)


if __name__=='__main__':
    TestPage = Page(driver=webdriver.Chrome())
    TestPage.open()