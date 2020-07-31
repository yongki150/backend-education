"""
참고자료
https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/ selenium 전반적인 가이드
https://wkdtjsgur100.github.io/selenium-does-not-work-to-click/ click이슈 해결
https://stackoverflow.com/questions/18225997/stale-element-reference-element-is-not-attached-to-the-page-document
stale이유 해결
"""

# Selenium은 webdriver api를 통해 브라우저를 제어
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
import os.path

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, '/drivers/chromedriver.exe')

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

login('ygflove@bible.ac.kr', '@yg96247890')

