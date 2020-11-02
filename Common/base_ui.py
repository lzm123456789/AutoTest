# coding=utf-8
from Log import log
from Config import config as my_config
import time
import os
from functools import wraps
from selenium import webdriver as web_driver
from appium import webdriver as app_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.mobilecommand import MobileCommand

log = log.MyLog()


def shot(func):
    @wraps(func)
    def function(*args, **kwargs):
        i = 1
        while i <= 3:
            try:
                ret = func(*args, **kwargs)
                break
            except:
                if i == 3:
                    curr_path = os.path.dirname(os.path.realpath(__file__))
                    image_name = os.path.join(
                        os.path.dirname(curr_path),
                        'TestReport',
                        'image',
                        time.strftime("%Y_%m_%d_%H_%M_%S") + '.jpg'
                    )
                    log.error('operation failed, screenshots can be found through logs by time~')
                    args[0].driver.get_screenshot_as_file(image_name)
                    raise
                i += 1
        return ret

    return function


@shot
def chorme_driver():
    driver = web_driver.Chrome()
    driver.maximize_window()
    return driver


def android_app_driver(appPackage, appActivity):
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
        # 'app': r'D:\app\BoYuStaff_Android_2.7.5_2019-10-18_14-43.apk'
        # 'newCommandTimeout': '70'
    }
    return app_driver.Remote('http://127.0.0.1:4723/wd/hub', app_parameters)


class PCBaseUI:
    url = ''
    config = my_config.MyConfig()
    pc_host = config.get_conf('web_ui', 'pc_host')

    def __init__(self, driver, pc_host=pc_host):
        self.pc_host = pc_host
        self.driver = driver
        self.timeout = 30

    def local_element(self, loc):
        time.sleep(0.5)
        return WebDriverWait(self.driver, 25).until(EC.presence_of_element_located(loc))

    @shot
    def open(self):
        self.driver.get(self.pc_host + self.url)

    @shot
    def click(self, loc):
        self.local_element(loc).click()

    @shot
    def clear(self, loc):
        self.local_element(loc).clear()

    @shot
    def input(self, loc, text):
        self.local_element(loc).send_keys(text)

    @shot
    def get_attribute(self, loc, attribute):
        return self.local_element(loc).get_attribute(attribute)

    @shot
    def get_text(self, loc):
        return self.local_element(loc).text

    @shot
    def get_title(self):
        return self.driver.title

    @shot
    def switch_to_frame(self, loc):
        self.driver.switch_to.frame(self.local_element(loc))

    @shot
    def switch_to_content(self):
        self.driver.switch_to.default_content()

    @shot
    def js(self, js):
        self.driver.excute_script(js)

    @shot
    def right_click(self, loc):
        ActionChains(self.driver).context_click(self.local_element(loc)).perform()

    @shot
    def move_to_element(self, loc):
        ActionChains(self.driver).move_to_element(self.local_element(loc)).perform()

    @shot
    def drag_and_drop(self, loc1, loc2):
        element1 = self.local_element(loc1)
        element2 = self.local_element(loc2)
        ActionChains(self.driver).drag_and_drop(element1, element2).perform()

    @shot
    def switch_to_windows_by_title(self, title):
        '''
        切换到名字为title的窗口
        :param title: 窗口标题
        :return: 当前窗口的句柄
        '''

        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to_window(handle)
            if (self.driver.title.__contains__(title)):
                break

    @shot
    def forward(self):
        self.driver.forward()

    @shot
    def back(self):
        self.driver.back()

    @shot
    def refresh(self):
        self.driver.refresh()

    @shot
    def is_element_exist(self, loc):
        try:
            self.driver.find_element(*loc)
            return True
        except:
            return False

    @shot
    def close(self):
        self.driver.close()

    @shot
    def quit(self):
        self.driver.quit()


class APPBaseUI:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def local_element(self, loc):
        time.sleep(0.5)
        return WebDriverWait(self.driver, 25).until(EC.presence_of_element_located(loc))

    def click(self, loc):
        self.local_element(loc).click()

    def clear(self, loc):
        self.local_element(loc).clear()

    def input(self, loc, text):
        self.local_element(loc).send_keys(text)

    def is_element_exist(self, loc):
        try:
            self.driver.find_element(*loc)
            return True
        except:
            return False

    def click_coordinates(self, location_x, location_y):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        x1 = int(x * location_x)
        y1 = int(y * location_y)
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
