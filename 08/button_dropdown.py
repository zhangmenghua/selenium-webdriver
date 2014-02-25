#coding=utf-8
#处理button dropdown
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import selenium.webdriver.support.ui as ui
dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('button_dropdown.html')
dr.get(file_path)
sleep(1)

dr.find_element_by_link_text('Info').click()
wait=ui.WebDriverWait(dr,10)
wait.until(lambda dr:dr.find_element_by_class_name('dropdown-menu').is_displayed())
# 通过ul再层级定位
dr.find_element_by_class_name('dropdown-menu').find_element_by_link_text('watir-webdriver').click()

sleep(1)
dr.quit()