from Common.base_ui import PCBaseUI
from selenium.webdriver.common.by import By


class Baidu(PCBaseUI):
    url = ['https://www.baidu.com/', '百度']

    keyword_input_box = [(By.ID, 'kw'), '查询关键字输入框']

    query_button = [(By.ID, 'su'), '百度一下按钮']

    query_result = [(By.XPATH, "//span[@class='nums_text111']"), '查询结果标签']
