#coding=utf-8
#操作测试对象
from selenium import webdriver
from time import sleep
import os
dr=webdriver.Chrome()
file_path="file:///"+os.path.abspath('operate_element.html')
dr.get(file_path)

dr.find_element_by_link_text('Link1').click()
sleep(1)
dr.find_element_by_link_text('Link1').click()
sleep(1)
element=dr.find_element_by_name('q')
element.send_keys('something')
sleep(1)
element.clear()
dr.quit()

