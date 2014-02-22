#coding=utf-8
#浏览器最大化
from selenium import webdriver
import time

dr=webdriver.Chrome()
time.sleep(2)
print 'maximize browser'

dr.maximize_window()

time.sleep(2)
dr.quit()
print 'close browser'