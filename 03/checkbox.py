#coding=utf-8
#定位一组对象
from selenium import webdriver
from time import sleep
import os

dr=webdriver.Chrome()
file_path='file:///'+os.path.abspath('checkbox.html')
dr.get(file_path)
# 选择所有的checkbox并全部勾上
checkboxs=dr.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxs:
	checkbox.click()
sleep(1)
dr.refresh()
sleep(2)

# 打印当前页面上有多少个checkbox
print len(dr.find_elements_by_css_selector('input[type=checkbox]'))

# 选择页面上所有的input，然后从中过滤出所有的checkbox并勾选之
inputs=dr.find_elements_by_tag_name('input')
for input in inputs:
	if input.get_attribute('type')=='checkbox':
		input.click()
sleep(1)
# 把页面上最后1个checkbox的勾给去掉
dr.find_elements_by_css_selector('input[type=checkbox]').pop().click()
sleep(2)
dr.quit()
