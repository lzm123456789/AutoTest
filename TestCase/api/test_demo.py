# coding=utf-8
import unittest
from Common import my_assert
from ddt import ddt, file_data
from Common.my_unittest import Api

myassert = my_assert.Assert()


class Demo(Api):
    def test_demo(self):
        request = self.request
        url = self.pc_host + '/test/'
        cookies = {}
        data = {'name': 'xxx', 'sex': '男'}
        response = request.get(url=url, cookies=cookies, data=data)
        myassert.assert_code(response[0])
        myassert.assert_equal(response[1]['age'], '30')


@ddt
class TestTDD(Api):

    @file_data('../../TestData/user.yaml')
    def test_tdd(self, **kwargs):
        print(kwargs)
        print('执行')
        print('断言')


class TestSkip(Api):

    @unittest.skipIf(1 == 1, '跳过')
    def test_skip1(self):
        myassert.assert_equal(1, 2)

    @unittest.expectedFailure
    def test_skip2(self):
        print('期望失败')
        myassert.assert_equal(1, 2)


if __name__ == '__main__':
    testsuite = unittest.TestSuite()
    testrunner = unittest.TextTestRunner()
    # testsuite.addTests(unittest.makeSuite(TestTDD))
    testsuite.addTest(TestSkip('test_skip1'))
    testrunner.run(testsuite)
