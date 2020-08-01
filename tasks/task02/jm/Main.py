from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('.\\drivers\\chromedriver.exe')
driver.get('https://accounts.google.com/')

def login(user_id, user_pw):
    sleep(1)
    driver.find_element_by_name('identifier').send_keys(user_id)
    driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
    sleep(3)
    driver.find_element_by_name('password').send_keys(user_pw)
    driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()

login('id', 'password')