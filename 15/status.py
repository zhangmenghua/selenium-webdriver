#coding=utf-8
#获取测试对象的状态
from selenium import webdriver
from time import sleep
import os

dr=webdriver.Chrome()
file_path="file:///"+os.path.abspath('status.html')
dr.get(file_path)

text_field = dr.find_element_by_name('user')
print text_field.is_enabled()

dr.execute_script('$(arguments[0]).hide()', text_field)
print text_field.is_displayed()

radio = dr.find_element_by_name('radio')
radio.click()
print radio.is_selected()

# 判断元素是否存在
try:
    dr.find_element_by_id('none')
except: 
    print 'element does not exist'

dr.quit()