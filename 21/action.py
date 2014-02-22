#coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
elment=wd.find_element_by_link_text('xxxxx')
hov=ActionChains(wd).move_to_element(elment)
hov.perform()
