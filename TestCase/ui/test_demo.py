# coding=utf-8
from Pages.demo import Baidu
from Common import my_assert
from Common import my_unittest

myassert = my_assert.Assert()


class Demo(my_unittest.WebUI):

    def test_success_demo(self):
        """断言成功的场景"""

        driver = self.driver
        baidu = Baidu(driver, pc_host='')
        baidu.open()
        baidu.wait(3)
        title = baidu.get_title()
        myassert.assert_equal(title, '百度一下，你就知道1')

    def test_fail_demo(self):
        """断言失败的场景"""

        driver = self.driver
        baidu = Baidu(driver, pc_host='')
        baidu.open()
        baidu.wait(3)
        title = baidu.get_title()
        myassert.assert_equal(title, '百度一下，你就知道2')

    def test_shot_demo(self):
        """操作失败的场景"""

        driver = self.driver
        baidu = Baidu(driver, pc_host='')
        baidu.open()
        baidu.input(baidu.keyword_input_box, 'xxx')
        baidu.click(baidu.query_button)
        baidu.wait(3)
        temp = baidu.get_text(baidu.query_result)
        actual_result = len(temp[11:-1])
        if actual_result >= 1:
            assert True
        else:
            assert False


if __name__ == '__main__':
    import unittest

    testsuite = unittest.TestSuite()
    testrunner = unittest.TextTestRunner()
    testsuite.addTest(Demo('test_success_demo'))
    testrunner.run(testsuite)
