import sys
import io
import requests , json
from bs4 import BeautifulSoup
import urllib
from selenium import webdriver
import time

#Rest : POST, GET, PUT-업데이트, 대체하는 성격(FETCH: 업데이트 수정), DELETE

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

driver = webdriver.Chrome("c:/section3/webdriver/chrome/chromedriver")

driver.implicitly_wait(5)

driver.get('https://everytime.kr/login')

driver.find_element_by_name('userid').send_keys('wnshdl')
driver.find_element_by_name('password').send_keys('784512')
driver.find_element_by_xpath('//*[@id="container"]/form/p[3]/input').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="menu"]/li[3]/a').click()

driver.find_element_by_name('keyword').send_keys('박재홍')
time.sleep(3)

driver.find_element_by_xpath('//*[@id="container"]/form/input[2]').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="container"]/div/a[5]/h3/p[1]').click()
time.sleep(3)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

text = soup.select('#container > div.side.article > div.articles > article')

for i in text:
    print(i.select_one('p.text').text)
