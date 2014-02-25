#coding=utf-8
#前进和后退
from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()
first_url = 'http://www.baidu.com'
print "now access %s" %(first_url)

dr.get(first_url)
sleep(1)
second_url = 'http://www.news.baidu.com'
print "now access %s" %(second_url)
dr.get(second_url)
sleep(1)

print "back to %s" %(first_url)
dr.back()
sleep(1)
print "forward to %s" %(second_url)
dr.forward()
sleep(1)
dr.quit()