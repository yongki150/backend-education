from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def login(user_id, user_pw):
    dirver.get("https://leetcode.com/accounts/login/")
    dirver.find_element_by_class_name("link__Mcl7").click() #ok
    print("되고있는거가?  ", dirver)
    dirver.find_element_by_xpath('//input[@type="email"]').send_keys(user_id)
    dirver.find_element_by_xpath('//*[@id="identifierNext"]').click()
    dirver.find_element_by_xpath('//input[@type="password"]').send_keys(user_pw)
    dirver.find_element_by_xpath('//*[@id="passwordNext"]').click()




user_id = input()
user_pw = input()
dirver = webdriver.Chrome("C:\\Users\\kooki\\Desktop\\bot\\backend-education\\tasks\\task02\\dirvers\\chromedriver.exe")
dirver.implicitly_wait(3)
login(user_id, user_pw)
time.sleep(50)