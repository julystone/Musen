# encoding:utf8

# -----------------------------
# @File   :   estar.py
# @Author :   July401
# @Date   :   2019/6/17
# @Email  :   july401@qq.com
# -----------------------------
import os
import time

from selenium.webdriver.support.ui import WebDriverWait

cur_path = os.path.dirname(os.path.realpath(__file__))
screenshot_path = os.path.join(os.path.dirname(cur_path), 'screenshots')
if not os.path.exists(screenshot_path): os.mkdir(screenshot_path)


class Common:

    @staticmethod
    def find_element(DUT, loc, exception=False, timeout=15):
        """
        查找元素方法基础方法
        :param DUT: driver
        :param loc: tuple，[0]为定位方式  [1]为定位地址
        :param exception: 找不到元素后是否抛出异常，默认为是
        :param timeout: 定位元素等待时间
        :return: None
        """
        try:
            WebDriverWait(DUT, timeout).until(lambda DUT2: DUT2.find_element(*loc).is_displayed())
            return DUT.find_element(*loc)
        except Exception as e:
            print('页面中未能找到%s 元素' % loc)
            if not exception:
                raise e
            else:
                return None

    def find_element_by_text(self, DUT, text, exception=False, timeout=15):
        text = f"""//*[@text="{text}"]"""
        loc = ('xpath', text)
        return self.find_element(DUT, loc, exception, timeout)

    def find_element_by_partial_text(self, DUT, text, exception=False, timeout=15):
        text = rf"""//*[contains(@text, '{text}')] """
        loc = ('xpath', text)
        return self.find_element(DUT, loc, exception, timeout)

    @staticmethod
    def touch_tap(DUT, x, y, duration=100):  # 点击坐标  ,x1,x2,y1,y2,duration
        """
        method explain:点击坐标
        parameter explain：【x,y】坐标值,【duration】:给的值决定了点击的速度
        Usage:
            device.touch_coordinate(277,431)      #277.431为点击某个元素的x与y值
        """
        screen_width = DUT.get_window_size()['width']  # 获取当前屏幕的宽
        screen_height = DUT.get_window_size()['height']  # 获取当前屏幕的高
        a = (float(x) / screen_width) * screen_width
        x1 = int(a)
        b = (float(y) / screen_height) * screen_height
        y1 = int(b)
        DUT.tap([(x1, y1), (x1, y1)], duration)

    def clear_key(self, DUT, loc):
        """重写清空文本输入法"""
        time.sleep(1)
        self.find_element(DUT, loc).clear()

    def send_keys(self, DUT, loc, value):
        """重写在文本框中输入内容的方法"""
        self.find_element(DUT, loc).send_keys(value)

    def click_button(self, DUT, loc):
        """重写点击按钮的方法"""
        self.find_element(DUT, loc).click()

    def click_button_by_text(self, DUT, text):
        """重写点击按钮的方法"""
        self.find_element_by_text(DUT, text).click()

    def click_button_by_partial_text(self, DUT, text):
        """重写点击按钮的方法"""
        self.find_element_by_partial_text(DUT, text).click()

    @staticmethod
    def get_screenshots(DUT):
        """重写截图方法"""
        sh_file = os.path.join(screenshot_path, '%s.png' % time.strftime('%Y_%m_%d'))
        DUT.get_screenshot_as_file(sh_file)

    @staticmethod
    def get_windows_size(DUT):
        """获取屏幕大小"""
        windows_size = DUT.get_window_size()
        return windows_size

    @staticmethod
    def swipe_windows(DUT, direction='down', speed=500):
        """滑动屏幕"""
        windows_size = DUT.get_window_size()
        direction = direction.lower()
        width = windows_size['width']
        height = windows_size['height']
        if direction == 'down':
            DUT.swipe(start_x=0.5 * width, start_y=0.75 * height,
                      end_x=0.5 * width, end_y=0.25 * height, duration=speed)
        elif direction == 'up':
            DUT.swipe(start_x=0.5 * width, start_y=0.25 * height,
                      end_x=0.5 * width, end_y=0.75 * height, duration=speed)
        elif direction == 'left':
            DUT.swipe(start_x=0.75 * width, start_y=0.5 * height,
                      end_x=0.25 * width, end_y=0.5 * height, duration=speed)
        elif direction == 'right':
            DUT.swipe(start_x=0.25 * width, start_y=0.5 * height,
                      end_x=0.75 * width, end_y=0.5 * height, duration=speed)

    def input(self, DUT, loc, content, ifclear=True):
        self.click_button(DUT, loc)
        if ifclear:
            self.clear_key(DUT, loc)
        self.send_keys(DUT, loc, content)
