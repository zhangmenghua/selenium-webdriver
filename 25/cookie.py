#coding=utf-8
from selenium import webdriver
from time import sleep

dr=webdriver.Chrome()
url='http://www.baidu.com'
dr.get(url)
print dr.get_cookies()

dr.delete_all_cookies()

dr.add_cookie({'name':'zhang','value':'123456'})
dr.get(url)
sleep(5)
dr.quit()
