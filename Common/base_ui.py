# coding=utf-8
import os
import time
from Log import log
from functools import wraps
from Config import config as my_config
from appium import webdriver as app_driver
from selenium import webdriver as web_driver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.mobilecommand import MobileCommand
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

log = log.MyLog
config = my_config.MyConfig()


def executionlog(func):
    # 执行UI层自动化测试的时候 报错，重试3次，如果还是报错 则截图和记录日志

    @wraps(func)
    def function(*args, **kwargs):
        i = 1
        while i <= 3:
            try:
                # 给对浏览器的每个操作加上日志记录
                if func.__name__ == 'chrome_driver':
                    log.info('启动谷歌浏览器并最大化窗口')
                elif func.__name__ == 'open':
                    log.info('打开 ' + (args[0].url)[1] + ' 页面')
                elif func.__name__ == 'wait':
                    log.info('等待 ' + str(args[1]) + ' 秒')
                elif func.__name__ == 'input':
                    log.info('在 ' + args[1][1] + ' 输入：' + args[2])
                elif func.__name__ == 'click':
                    log.info('点击 ' + args[1][1])
                elif func.__name__ == 'get_text':
                    log.info('获取 ' + args[1][1] + ' 的文本属性')
                elif func.__name__ == 'clear':
                    log.info('清空 ' + args[1][1] + ' 的字符')
                elif func.__name__ == 'get_attribute':
                    log.info('获取 ' + args[1][1] + ' 的属性：' + args[2] + '的值')
                elif func.__name__ == 'get_title':
                    log.info('获取页面的标题')
                elif func.__name__ == 'switch_to_frame':
                    log.info('切换到 ' + args[1][1])
                elif func.__name__ == 'switch_to_content':
                    log.info('退出frame，回到页面')
                elif func.__name__ == 'js':
                    log.info('执行js: ' + args[1][1])
                elif func.__name__ == 'right_click':
                    log.info('模拟鼠标右击 ' + args[1][1])
                elif func.__name__ == 'double_click':
                    log.info('模拟鼠标双击 ' + args[1][1])
                elif func.__name__ == 'move_to_element':
                    log.info('模拟鼠标悬停在 ' + args[1][1])
                elif func.__name__ == 'drag_and_drop':
                    log.info('模拟鼠标把元素 ' + args[1][1] + ' 拖拽到 ' + args[2][1])
                elif func.__name__ == 'switch_to_windows_by_title':
                    log.info('浏览器窗口切换到 ' + args[1][1])
                elif func.__name__ == 'forward':
                    log.info('浏览器前进')
                elif func.__name__ == 'back':
                    log.info('浏览器后退')
                elif func.__name__ == 'refresh':
                    log.info('刷新当前页面')
                elif func.__name__ == 'close':
                    log.info('关闭当前窗口')
                elif func.__name__ == 'is_element_exist':
                    log.info('判断元素 ' + args[1][1] + ' 是否存在')
                elif func.__name__ == 'quit':
                    log.info('退出浏览器')
                else:
                    log.error('未知操作')

                ret = func(*args, **kwargs)
                break
            except:
                log.warning('操作失败%s次' % i)
                if i == 3:
                    curr_path = os.path.dirname(os.path.realpath(__file__))
                    image_name = os.path.join(os.path.dirname(curr_path),
                                              'TestReport',
                                              'images',
                                              time.strftime("%Y_%m_%d_%H_%M_%S") + '.jpg')
                    log.error('不再重试，可通过记录日志的时间找到对应的截图～')
                    args[0].driver.get_screenshot_as_file(image_name)
                    raise
                i += 1
        return ret

    return function


@executionlog
def chrome_driver():
    # 启动谷歌浏览器

    driver = web_driver.Chrome('/usr/local/bin/chromedriver')
    driver.maximize_window()
    return driver


@executionlog
def quit(driver):
    # 退出浏览器

    driver.quit()


def android_app_driver(appPackage, appActivity):
    # 启动app

    app_parameters = {
        'platformName': 'Android',
        'deviceName': 'MEIZU MX5',
        'platformVersion': '5.1',
        'appPackage': appPackage,
        'appActivity': appActivity,
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'noReset': True,
        'noSign': True,
        # 'app': r'D:\app\test.apk'
        # 'newCommandTimeout': '70'
    }
    return app_driver.Remote('http://127.0.0.1:4723/wd/hub', app_parameters)


class PCBaseUI:
    """WEB UI层自动化测试，基础页面对象类"""

    url = ''
    pc_host = config.get_conf('web_ui', 'pc_host')

    def __init__(self, driver, pc_host=pc_host):
        # 初始化host和driver

        self.pc_host = pc_host
        self.driver = driver
        self.timeout = 30

    def locate_element(self, loc):
        # 以显示等待的方式定位元素

        time.sleep(0.5)
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(loc[0]))

    @executionlog
    def open(self):
        # 打开页面

        self.driver.get(self.pc_host + self.url[0])

    @executionlog
    def click(self, loc):
        # 点击

        self.locate_element(loc).click()

    @executionlog
    def clear(self, loc):
        # 清空

        self.locate_element(loc).clear()

    @executionlog
    def input(self, loc, text):
        # 输入

        self.locate_element(loc).send_keys(text)

    @executionlog
    def wait(self, sec):
        # 等待

        time.sleep(sec)

    @executionlog
    def get_attribute(self, loc, attribute):
        # 获取元素属性的值

        return self.locate_element(loc).get_attribute(attribute)

    @executionlog
    def get_text(self, loc):
        # 获取元素的文本属性

        return self.locate_element(loc).text

    @executionlog
    def get_title(self):
        # 获取页面标题

        return self.driver.title

    @executionlog
    def switch_to_frame(self, loc):
        # 切换到页面里面的frame

        self.driver.switch_to.frame(self.locate_element(loc))

    @executionlog
    def switch_to_content(self):
        # 退出frame

        self.driver.switch_to.default_content()

    @executionlog
    def js(self, js):
        # 执行js

        self.driver.execute_script(js[0])

    @executionlog
    def right_click(self, loc):
        # 模拟鼠标右击

        ActionChains(self.driver).context_click(self.locate_element(loc)).perform()

    @executionlog
    def double_click(self, loc):
        # 模拟鼠标双击

        ActionChains(self.driver).double_click(self.locate_element(loc)).perform()

    @executionlog
    def move_to_element(self, loc):
        # 模拟鼠标悬停

        ActionChains(self.driver).move_to_element(self.locate_element(loc)).perform()

    @executionlog
    def drag_and_drop(self, loc1, loc2):
        # 模拟鼠标移动元素

        element1 = self.locate_element(loc1)
        element2 = self.locate_element(loc2)
        ActionChains(self.driver).drag_and_drop(element1, element2).perform()

    @executionlog
    def switch_to_windows_by_title(self, title):
        """
        切换到名字为title的窗口
        :param title: 窗口标题
        :return: 当前窗口的句柄
        """

        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to_window(handle)
            if (self.driver.title.__contains__(title)):
                break

    @executionlog
    def forward(self):
        # 前进

        self.driver.forward()

    @executionlog
    def back(self):
        # 后退

        self.driver.back()

    @executionlog
    def refresh(self):
        # 刷新页面

        self.driver.refresh()

    @executionlog
    def is_element_exist(self, loc):
        # 判断元素是否存在

        try:
            self.driver.find_element(*(loc[0]))
            return True
        except:
            return False

    @executionlog
    def close(self):
        # 关闭页面

        self.driver.close()


class APPBaseUI:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def locate_element(self, loc):
        time.sleep(0.5)
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(loc[0]))

    def click(self, loc):
        self.locate_element(loc).click()

    def clear(self, loc):
        self.locate_element(loc).clear()

    def input(self, loc, text):
        self.locate_element(loc).send_keys(text)

    def is_element_exist(self, loc):
        try:
            self.driver.find_element(*(loc[0]))
            return True
        except:
            return False

    def click_coordinates(self, locationx, locationy):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        x1 = int(x * locationx)
        y1 = int(y * locationy)
        self.driver.swipe(x1, y1, x1, y1, 500)

    def switch_h5(self, h5_name):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": h5_name})

    def switch_app(self):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})

    def enableMeizuIME(self):
        # command0 = 'adb shell ime list -s'
        # command1 = 'adb shell settings get secure default_input_method'
        # command2 = 'adb shell ime set com.meizu.flyme.input/com.meizu.input.MzInputService'
        # command3 = 'adb shell ime set io.appium.android.ime/.UnicodeIME'
        # command4 = 'adb shell ime set com.sohu.inputmethod.sogou/.SogouIME'
        # 列出系统现在所安装的所有输入法
        # os.system(command0)
        # 打印系统当前默认的输入法
        # os.system(command1)
        # 切换latin输入法为当前输入法
        # os.system(command2)
        # 切换appium输入法为当前输入法
        # os.system(command3)
        # 切换搜狗输入法为当前输入法
        # os.system(command4)

        os.system('adb shell ime set com.meizu.flyme.input/com.meizu.input.MzInputService')

    def enableAppiumUnicodeIME(self):
        os.system('adb shell ime set io.appium.android.ime/.UnicodeIME')

    def enableSogouIME(self):
        os.system('adb shell ime set com.sohu.inputmethod.sogou/.SogouIME')
