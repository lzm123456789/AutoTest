# coding=utf-8
"""
封装config方法
"""
from configparser import ConfigParser
import os


class MyConfig:
    def __init__(self):
        curr_path = os.path.dirname(os.path.realpath(__file__))
        self.conf_path = os.path.join(curr_path, 'config.ini')
        self.config = ConfigParser()
        self.config.read(self.conf_path, encoding='utf-8')

    def get_conf(self, title, value):
        """配置文件读取"""
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """配置文件修改"""
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """配置文件添加"""
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)


if __name__ == '__main__':
    MyConfig().add_conf('title1')
    MyConfig().set_conf('title1', 'value1', 'text1')
    text = MyConfig().get_conf('title1', 'value1')
    print(text)
