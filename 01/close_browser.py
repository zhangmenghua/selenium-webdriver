#coding=utf-8
#关闭浏览器
from selenium import webdriver
import time

dr=webdriver.Chrome()
time.sleep(2)
print 'brower will be closed'

dr.quit()
print 'brower is closed'

