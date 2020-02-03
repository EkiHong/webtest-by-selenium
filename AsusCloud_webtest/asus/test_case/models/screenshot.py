from selenium import webdriver
import datetime
import time
import os

def insert_image(driver):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/test_case')[0]
    file_name = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
    file_path = base + '/test_report/image/' + file_name + '.png'  # 這行有問題
    driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    insert_image()