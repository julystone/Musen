# -*- coding:utf-8 -*-
# @Time   : 2018-11-01 19:24
# @Author : YangWeiMin

from Page.BasePage import Action


class Login(Action):
    """登录页面"""
    # 用户名
    username_loc = ('id', 'com.ali.user.mobile.security.ui:id/content')
    # 密码
    pwd_loc = ('xpath', '//android.widget.RelativeLayout[2]/android.widget.EditText')
    # 登录
    login_button_loc = ('id', 'com.ali.user.mobile.security.ui:id/loginButton')
    # 登录成功后的菜单首页
    login_success_loc = ('id', 'com.alipay.android.phone.discovery.o2ohome:id/tab_description')
    # 用户同意
    agree_loc = ('id', 'esunny.test:id/es_login_state_confirm_activity_confirm')
    # 右侧展开栏
    toolbar_right = ('id', 'esunny.test:id/toolbar_right_first')
    # 左侧退出键
    toolbar_left_out = ('id', 'esunny.test:id/toolbar_left_first')
    # 交易登录
    right_login = ('text', 'esunny.test:text/交易登录')


    def click_agree(self):
        """点击同意按钮"""
        self.click_button(self.agree_loc)


    def input_username(self):
        """输入用户名"""
        self.click_button(self.username_loc)
        self.clear_key(self.username_loc)
        self.send_keys(self.username_loc, '13770873187')

    def input_pwd(self):
        """输入密码"""
        self.click_button(self.pwd_loc)
        self.clear_key(self.pwd_loc)
        self.send_keys(self.pwd_loc, '57876975yang')

    def click_login(self):
        """点击登录按钮"""
        self.click_button(self.login_button_loc)

    def login_success(self):
        """判断登录是否成功"""
        # login_success = self.driver.find_element_by_id('com.alipay.android.phone.discovery.o2ohome:id/tab_description').text
        login_success = self.find_element(self.login_success_loc).text
        return login_success
