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
    right_login = ('xpath', '//*[@text="交易登录"]')
    select_co_button = ('id', 'esunny.test:id/ed_login_activity_rl_choose_site')
    QMX_loc = ('xpath', '//*[@text="易盛内盘 启明星（V3仿真）"]')
    account_input_loc = ('id', 'esunny.test:id/et_login_userno')
    password_input_loc = ('id', 'esunny.test:id/et_login_pwd')
    confirm_loc = ('id', 'esunny.test:id/tv_login_submit')

    def input(self, loc, content):
        """输入密码"""
        self.click_button(loc)
        self.clear_key(loc)
        self.send_keys(loc, content)

    def click_login(self):
        """点击登录按钮"""
        self.click_button(self.login_button_loc)

    def login_success(self):
        """判断登录是否成功"""
        # login_success = self.driver.find_element_by_id('com.alipay.android.phone.discovery.o2ohome:id/tab_description').text
        login_success = self.find_element(self.login_success_loc).text
        return login_success
