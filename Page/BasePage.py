# -*- coding:utf-8 -*-
# @Time   : 2018-11-01 19:24
# @Author : YangWeiMin

import os
import unittest

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from config.Read_caps import my_caps

cur_path = os.path.dirname(os.path.realpath(__file__))
screenshot_path = os.path.join(os.path.dirname(cur_path), 'screenshots')
if not os.path.exists(screenshot_path): os.mkdir(screenshot_path)


class Action(unittest.TestCase):
    """Base封装公用的方法"""

    def setUp(self):
        print('------开始执行用例------')

    def tearDown(self):
        print('------用例测试结束------')

    @classmethod
    def setUpClass(cls):
        data = my_caps
        desired_caps = {}
        desired_caps['platformName'] = data['platformName']
        desired_caps['platformVersion'] = data['platformVersion']
        desired_caps['deviceName'] = data['deviceName']
        desired_caps['appPackage'] = data['appPackage']
        desired_caps['appActivity'] = data['appActivity']
        desired_caps['noSign'] = data['noSign']
        desired_caps['noReset'] = data['noReset']
        desired_caps['automationName'] = data['automationName']
        cls.DUT = webdriver.Remote('http://' + data['ip'] + ':' + str(data['port']) + '/wd/hub', desired_caps)
        print(cls.DUT)

    def find_element(self, loc, exception=False, timeout=15):
        """
        查找元素方法基础方法
        :param loc: tuple，[0]为定位方式  [1]为定位地址
        :param exception: 找不到元素后是否抛出异常，默认为是
        :param timeout: 定位元素等待时间
        :return: None
        """
        try:
            WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except Exception as e:
            print('%s 页面中未能找到%s 元素' % (self, loc))
            if not exception:
                raise e
            else:
                return None
    #
    # def find_element_by_text(self, text, exception=False, timeout=15):
    #     text = f"""//*[@text="{text}"]"""
    #     loc = ('xpath', text)
    #     return self.find_element(loc, exception, timeout)
    #
    # def find_element_by_partial_text(self, text, exception=False, timeout=15):
    #     text = f"""//*[contains(@text,'{text}')] """
    #     loc = ('xpath', text)
    #     return self.find_element(loc, exception, timeout)
    #
    # def touch_tap(self, x, y, duration=100):  # 点击坐标  ,x1,x2,y1,y2,duration
    #     """
    #     method explain:点击坐标
    #     parameter explain：【x,y】坐标值,【duration】:给的值决定了点击的速度
    #     Usage:
    #         device.touch_coordinate(277,431)      #277.431为点击某个元素的x与y值
    #     """
    #     screen_width = self.driver.get_window_size()['width']  # 获取当前屏幕的宽
    #     screen_height = self.driver.get_window_size()['height']  # 获取当前屏幕的高
    #     a = (float(x) / screen_width) * screen_width
    #     x1 = int(a)
    #     b = (float(y) / screen_height) * screen_height
    #     y1 = int(b)
    #     self.driver.tap([(x1, y1), (x1, y1)], duration)
    #
    # def clear_key(self, loc):
    #     """重写清空文本输入法"""
    #     time.sleep(1)
    #     self.find_element(loc).clear()
    #
    # def send_keys(self, loc, value):
    #     """重写在文本框中输入内容的方法"""
    #     self.find_element(loc).send_keys(value)
    #
    # def click_button(self, loc):
    #     """重写点击按钮的方法"""
    #     self.find_element(loc).click()
    #
    # def click_button_by_text(self, text):
    #     """重写点击按钮的方法"""
    #     self.find_element_by_text(text).click()
    #
    # def click_button_by_partial_text(self, text):
    #     """重写点击按钮的方法"""
    #     self.find_element_by_partial_text(text).click()
    #
    # def getScreenShot(self):
    #     """重写截图方法"""
    #     self.sh_file = os.path.join(screenshot_path, '%s.png' % time.strftime('%Y_%m_%d'))
    #     self.driver.get_screenshot_as_file(self.sh_file)
    #
    # def get_windows_size(self):
    #     """获取屏幕大小"""
    #     windows_size = self.driver.get_window_size()
    #     return windows_size
    #
    # def swipe_windows(self, direction='down', speed=500):
    #     """滑动屏幕"""
    #     windows_size = self.driver.get_window_size()
    #     direction = direction.lower()
    #     width = windows_size['width']
    #     height = windows_size['height']
    #     if direction == 'down':
    #         self.driver.swipe(start_x=0.5 * width, start_y=0.75 * height,
    #                           end_x=0.5 * width, end_y=0.25 * height, duration=speed)
    #     elif direction == 'up':
    #         self.driver.swipe(start_x=0.5 * width, start_y=0.25 * height,
    #                           end_x=0.5 * width, end_y=0.75 * height, duration=speed)
    #     elif direction == 'left':
    #         self.driver.swipe(start_x=0.75 * width, start_y=0.5 * height,
    #                           end_x=0.25 * width, end_y=0.5 * height, duration=speed)
    #     elif direction == 'right':
    #         self.driver.swipe(start_x=0.25 * width, start_y=0.5 * height,
    #                           end_x=0.75 * width, end_y=0.5 * height, duration=speed)
    #
    # def input(self, loc, content, ifclear=True):
    #     self.click_button(loc)
    #     if ifclear:
    #         self.clear_key(loc)
    #     self.send_keys(loc, content)
