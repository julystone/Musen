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
            self.swipe_windows()
            self.click_button(super().toolbar_right)
            self.click_button(super().right_login)

        except Exception as e:
            self.getScreenShot()
            my_log.error(e)


if __name__ == '__main__':
    unittest.main()
