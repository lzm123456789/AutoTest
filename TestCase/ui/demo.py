# coding=utf-8
from Common import my_unittest
from Common import my_assert
from Pages.demo import Baidu
import time

my_assert = my_assert.Assert()


class Demo(my_unittest.WebUI):
    def test_success_demo(self):
        driver = self.driver
        baidu = Baidu(driver, pc_host='')
        baidu.open()
        time.sleep(3)
        title = baidu.get_title()
        my_assert.assert_equal(title, '百度一下，你就知道')

    def test_fail_demo(self):
        driver = self.driver
        baidu = Baidu(driver, pc_host='')
        baidu.open()
        time.sleep(3)
        title = baidu.get_title()
        my_assert.assert_equal(title, '百度一下，你就知道1')

    def test_shot_demo(self):
        driver = self.driver
        baidu = Baidu(driver, pc_host='')
        baidu.open()
        baidu.input(Baidu.keyword_input_box, 'xxx')
        baidu.click(Baidu.query_button)
        time.sleep(3)
        temp = baidu.get_text(Baidu.query_result)
        actual_result = len(temp[11:-1])
        if actual_result >= 1:
            assert True
        else:
            assert False


if __name__ == '__main__':
    import unittest

    test_suite = unittest.TestSuite()
    test_runner = unittest.TextTestRunner()
    test_suite.addTest(Demo('test_shot_demo'))
    test_runner.run(test_runner)
