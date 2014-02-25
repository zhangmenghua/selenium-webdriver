#coding=utf-8
#设置浏览器大小
from selenium import webdriver
import time

dr=webdriver.Chrome()

dr.set_window_size(240,320)
dr.get('http://www.3g.qq.com')

time.sleep(2)
dr.quit()