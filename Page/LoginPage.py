# -*- coding:utf-8 -*-
# @Time   : 2018-11-01 19:24
# @Author : YangWeiMin

from Page.BasePage import Action


class Login(Action):
    """登录页面"""
    # 用户同意
    agree_loc = ('id', 'esunny.test:id/es_login_state_confirm_activity_confirm')
    # 右侧展开栏
    toolbar_right = ('id', 'esunny.test:id/toolbar_right_first')
    # 左侧退出键
    toolbar_left_out = ('id', 'esunny.test:id/toolbar_left_first')
    # 交易登录
    right_login = ('xpath', '//*[@text="交易登录"]')
    select_co_button = ('id', 'esunny.test:id/ed_login_activity_rl_choose_site')
    QMX_loc = ('xpath', '//*[@text="易盛信息 启明星（测试）"]')
    account_input_loc = ('id', 'esunny.test:id/et_login_userno')
    password_input_loc = ('id', 'esunny.test:id/et_login_pwd')
    confirm_loc = ('id', 'esunny.test:id/tv_login_submit')
    aaa = ('id', 'esunny.test:id/et_login_company')
    gnqh = ('id', 'esunny.test:id/es_activity_company_tv_local_future')
    mnjy = ('id', 'esunny.test:id/es_activity_password_tv_informal_trade')
