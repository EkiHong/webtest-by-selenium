from selenium.webdriver import Remote
from selenium import webdriver

def browser():
    #driver = webdriver.Chrome()
    localhost = "127.0.0.1:4444"
    dc = {'browserName':'chrome'}
    driver = webdriver.Remote(command_executor='http://' + localhost + '/wd/hub', desired_capabilities= dc)
    return driver

if __name__ == '__main__':
    dr = browser()
    dr.get("https://www.asuswebstorage.com/navigate/a/#/login")
    dr.quit()