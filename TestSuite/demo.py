# coding=utf-8
import os
import time
import unittest
from Config import config
from TestCase.ui import test_demo
# from TestCase.api import test_demo
from Common.Tools import send_mail
from Common.Tools import HTMLTestRunner_cn

# 获取邮件发送测试报告相关的配置信息
# config = config.MyConfig()
# email_server = config.get_conf('report', 'email_server')
# sender_login_user = config.get_conf('report', 'sender_login_user')
# sender_login_password = config.get_conf('report', 'sender_login_password')
# sender = config.get_conf('report', 'sender')
# receiver = config.get_conf('report', 'receiver')

# 实例化测试套件对象，添加测试用例
testsuite = unittest.TestSuite()
testcases = [
    test_demo.Demo('test_success_demo'),
    test_demo.Demo('test_fail_demo'),
    test_demo.Demo('test_shot_demo')
]
testsuite.addTests(testcases)

# 定义测试报告路径和名称
currpath = os.path.dirname(os.path.realpath(__file__))
trname = os.path.join(os.path.dirname(currpath),
                      'TestReport',
                      time.strftime('%Y-%m-%d-%H_%M_%S') + '_autotest_report.html')

# 创建空的测试报告对象，传给HTMLTestRunner执行测试套件生成测试报告
with open(trname, 'wb') as testreport:
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=testreport,
                                              title="自动化测试报告",
                                              description="测试详情：",
                                              verbosity=2,
                                              retry=0,
                                              save_last_try=True)
    runner.run(testsuite)

# 获取测试报告所在目录
repopath = os.path.join(os.path.dirname(currpath), 'TestReport')

# 邮件发送最新的测试报告
# sm = send_mail.SendMail(email_server,
#                         sender_login_user,
#                         sender_login_password,
#                         sender,
#                         receiver,
#                         "自动化回归测试报告",
#                         repopath)
# sm.send_mail()
