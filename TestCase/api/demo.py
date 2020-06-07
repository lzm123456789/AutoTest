# coding=utf-8
from Common.my_unittest import Api
from Common import my_assert

my_assert = my_assert.Assert()


class Demo(Api):
    def test_demo(self):
        my_request = self.request
        url = self.pc_host + '/test/'
        cookies = {}
        data = {
            'name': 'xxx',
            'sex': '男'
        }
        response = my_request.get(url=url, cookies=cookies, data=data)
        my_assert.assert_code(response[0], 200)
        my_assert.assert_equal(response[1]['age'], '30')


if __name__ == '__main__':
    import unittest

    test_suite = unittest.TestSuite()
    test_runner = unittest.TextTestRunner()
    test_suite.addTest(Demo('test_demo'))
    test_runner.run(test_runner)
