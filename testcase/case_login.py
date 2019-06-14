# -*- coding:utf-8 -*-
# @Time   : 2018-11-05 19:48
# @Author : YangWeiMin

import time
import unittest

from Page.LoginPage import Login
from common.Mylog import my_log


class CaseLogin(Login, unittest.TestCase):
    def test_login_success(self):
        """正常登录"""
        try:
            time.sleep(2)
            # self.swipe_windows()
            self.click_button(super().toolbar_right)
            self.click_button(super().right_login)
            super().input(super().account_input_loc, 'Q1223871051')
            super().input(super().password_input_loc, '123456')
            self.click_button(super().confirm_loc)

        except Exception as e:
            self.getScreenShot()
            my_log.error(e)


if __name__ == '__main__':
    unittest.main()
