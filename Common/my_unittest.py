# coding=utf-8
import unittest
from Common import base_ui
from Common import base_api
from Config import config as my_config


# WEB UI层自动化测试用
class WebUI(unittest.TestCase):
    def setUp(self):
        self.driver = base_ui.chorme_driver()

    def tearDown(self):
        self.driver.quit()


# 安卓APP UI层自动化测试
class AndroidAppUI(unittest.TestCase):

    def setUp(self):
        config = my_config.MyConfig()
        app_package = config.get_conf('android_app_ui', 'app_package')
        app_activity = config.get_conf('android_app_ui', 'app_activity')
        self.driver = base_ui.android_app_driver(app_package, app_activity)

    def tearDown(self):
        self.driver.quit()


# 接口层自动化测试
class Api(unittest.TestCase):
    def setUp(self):
        config = my_config.MyConfig()
        self.pc_host = config.get_conf('api', 'pc_host')
        self.contract_id = config.get_conf('api', 'contract_id')
        self.request = base_api.MyRequest()

    def tearDown(self):
        pass
