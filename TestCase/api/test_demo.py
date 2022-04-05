# coding=utf-8
from Common.my_unittest import Api
from Common import my_assert

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


if __name__ == '__main__':
    import unittest

    testsuite = unittest.TestSuite()
    testrunner = unittest.TextTestRunner()
    testsuite.addTest(Demo('test_demo'))
    testrunner.run(testsuite)
