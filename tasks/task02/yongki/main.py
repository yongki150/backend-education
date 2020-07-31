# Selenium은 webdriver api를 통해 브라우저를 제어
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
import os.path

filename = os.path.join(os.path.dirname(__file__), './drivers/chromedriver.exe')

# webdriver 객체생성
driver = webdriver.Chrome(filename)

# url에 접근
driver.get('https://leetcode.com/accounts/login/')

# google계정들어가기
def login(user_id, user_pw):
    driver.find_element_by_xpath("//a[@data-icon='google-c']").send_keys(Keys.ENTER)

    # login창 뚫기
    driver.find_element_by_id('identifierId').send_keys(user_id)
    driver.find_element_by_xpath("//button[@jsname='LgbsSe']").send_keys((Keys.ENTER))

    # passwd창 뚫기
    driver.implicitly_wait(3) # 웹자원들이 로드될때까지 시간조정 3초
    driver.find_element_by_name('password').send_keys(user_pw)
    try:
        element = driver.find_element_by_xpath("//button[@jsname='LgbsSe']")
        element.send_keys((Keys.ENTER))
    except exceptions.StaleElementReferenceException as e:
        element = driver.find_element_by_xpath("//button[@jsname='LgbsSe']")
        element.send_keys((Keys.ENTER))