# -*- coding: utf-8 -*-
# @Time    : 2019/4/20 17:41
# @Author  : Amos.Li

from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:/Projects/software/chromedriver")
driver.get('https://www.baidu.com/')