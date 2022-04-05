# coding=utf-8
from Log import log


class Assert:
    """封装断言类"""

    def __init__(self):
        self.log = log.MyLog

    def assert_equal(self, actual_value, expect_value):
        """
        断言实际得到的值是否等于预期值
        :param actual_value:自动化测试最后得到的实际值
        :param expect_value:预期值
        :return:测试通过或者抛异常测试不通过
        """
        try:
            assert actual_value == expect_value
            self.log.info('Test passed')
            return True
        except:
            self.log.error(
                "actual_value != expect_value, actual_value is %s, expect_value is %s" % (actual_value, expect_value))
            raise

    def assert_exist(self, obj):
        """
        断言对象是否存在
        :param obj: 自动化测试最后得到的元素
        :return: 测试通过或者抛异常测试不通过
        """
        try:
            assert obj
            self.log.info('Test passed')
            return True
        except:
            self.log.error("element does not exist, not meeting expectations")
            raise

    def assert_code(self, actual_code, expect_code=200):
        """
        断言请求接口返回的状态码是否等于预期
        :param actual_code: 请求接口返回的状态码
        :param expect_code: 预期返回的状态码
        :return: 测试通过或者抛异常测试不通过
        """
        try:
            assert actual_code == expect_code
            return True
        except:
            self.log.error("statusCode error, statusCode is %s, expectedCode is %s " % (actual_code, expect_code))
            raise
