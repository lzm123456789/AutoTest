# coding=utf-8
from Common.base_ui import PCBaseUI
from selenium.webdriver.common.by import By


class Baidu(PCBaseUI):
    url = 'https://www.baidu.com/'
    keyword_input_box = (By.ID, 'kw')
    query_button = (By.ID, 'su')
    query_result = (By.XPATH, "//span[@class='nums_text111']")
