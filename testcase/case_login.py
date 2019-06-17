import time
import unittest

import Model
from Model import BaseMethod
from Page.LoginPage import Login
from common.Mylog import my_log

model = Model.estar.Common()


# model.estar.aaa.click_button(self)

class CaseLogin(Login, unittest.TestCase):
    def test_login_success(self):
        """正常登录"""
        try:
            time.sleep(2)
            BaseMethod.click_button(self.DUT, Model.Basic.BaseBtn.tool_bar)
            BaseMethod.click_button_by_partial_text(self.DUT, '交易登录')
            BaseMethod.click_button(self.DUT, Model.accountLogin.inputbar.loginCompany)
            # self.touch_tap(700, 70)
            # self.touch_tap(500, 150)
            BaseMethod.click_button(self.DUT, Model.accountLogin.BaseBtn.localFuture)
            BaseMethod.click_button(self.DUT, Model.accountLogin.BaseBtn.informalTrade)
            while BaseMethod.find_element_by_partial_text(self.DUT, '启明星（测试）', exception=True, timeout=2) is None:
                BaseMethod.swipe_windows(self.DUT, direction='down')
            BaseMethod.click_button_by_partial_text(self.DUT, '启明星（测试）')
            BaseMethod.input(self.DUT, Model.accountLogin.inputbar.loginAccount, 'Q1223871051')
            BaseMethod.input(self.DUT, Model.accountLogin.inputbar.loginPwd, '123456')
            BaseMethod.click_button(self.DUT, Model.accountLogin.BaseBtn.confirmBtn)

        except Exception as e:
            my_log.error(e)
            BaseMethod.get_screenshots(self.DUT, )


if __name__ == '__main__':
    unittest.main()
