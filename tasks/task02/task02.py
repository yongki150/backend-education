import time
import os.path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def _init_():
    user_id = input('ID: ')
    user_pw = input('PW: ')

    return user_id, user_pw


def login(user_data):
    this_path = os.path.dirname( os.path.abspath( __file__ ) )
    path = os.path.join(this_path, 'dirvers')
    dirver = webdriver.Chrome(path + '\\chromedriver.exe')
    dirver.get('https://leetcode.com/accounts/login/')
    print(user_data)
    dirver.find_element_by_class_name('link__Mcl7').send_keys(Keys.ENTER)
    dirver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(user_data[0])
    dirver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').send_keys(Keys.ENTER)
    dirver.implicitly_wait(5)
    dirver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(user_data[1])
    dirver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').send_keys(Keys.ENTER)
    time.sleep(500)


user_data = _init_()
login(user_data)



