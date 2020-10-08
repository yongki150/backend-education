import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def _init_():
    user_id = input('ID: ')
    user_pw = input('PW: ')

    return user_id, user_pw


def login(user_data):
    dirver = webdriver.Chrome('./drivers/chromedriver.exe')
    dirver.get('https://leetcode.com/accounts/login/')
    print(user_data)
    dirver.find_element_by_class_name('link__Mcl7').send_keys(Keys.ENTER)
    dirver.find_element_by_xpath('//input[@type="email"]').send_keys(user_data[0])
    dirver.find_element_by_xpath('//button[@jsname="LgbsSe"]').send_keys(Keys.ENTER)
    dirver.implicitly_wait(5)
    dirver.find_element_by_xpath('//input[@name="password"]').send_keys(user_data[1])
    dirver.find_element_by_xpath('//button[@jsname="LgbsSe"]').send_keys(Keys.ENTER)
    time.sleep(500)


user_data = _init_()
login(user_data)



