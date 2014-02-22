#coding=utf-8
#获取测试对象的属性及内容
from selenium import webdriver
from time import sleep
import os

dr=webdriver.Chrome()
file_path="file:///"+os.path.abspath('attribute.html')
dr.get(file_path)

link=dr.find_element_by_id('tooltip')
print link.get_attribute('data-original-title')
print link.text
dr.quit()
