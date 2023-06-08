from time import sleep

import allure
from seleniumbase import BaseCase
from utils.ele_login import *
from parameterized import parameterized
from utils.read_random import *
from Page.user_recharge_elements import *

@allure.feature('Loadproxy用户测试')
@allure.story('用户充值模块')
class UserRecharge(BaseCase):
    def isElementExist(self, element):
        flag = True
        try:
            self.is_element_visible(element)
            return flag
        except:
            flag = False
            return flag
    @allure.title('打开LoadProxy官网选择语言为中文')
    def setUp(self):
        super().setUp()
        with allure.step('选择语言为中文避免测试失败'):
            self.open_url(EleLogin.url)
            self.maximize_window()
            self.wait_for_element(EleLogin.language)
            self.hover_and_click(EleLogin.language, EleLogin.language)
            self.wait_for_element(EleLogin.click_language_en)
            self.hover_and_click(EleLogin.click_language_en, EleLogin.click_language_en)
            self.hover_and_click(EleLogin.language, EleLogin.language)
            self.wait_for_element(EleLogin.click_language_cn)
            self.hover_and_click(EleLogin.click_language_cn, EleLogin.click_language_cn)
        with allure.step('断言登录界面文本为中文'):
            self.wait_for_element(EleLogin.language_assert)
            self.assert_text('登录', EleLogin.language_assert)


    @parameterized.expand([[('monkey@mail2.dev.fs77.net', 'qq2000', '10')],
                           [('otto@mail2.dev.fs77.net', 'qq2000', '20')],
                           [('2407114348@mail2.dev.fs77.net', 'qq2000', '30')],
                           [('hey@mail2.dev.fs77.net', 'qq2000', '12')],
                           [('kahilu@mail2.dev.fs77.net', 'qq2000', '38')],
                           [('jynivavu@mail2.dev.fs77.net', 'qq2000', '38')]])
    @allure.title('用户使用信用卡方式充值成功')
    def test_user_Recharge(self, datas):
        with allure.step(f'输入邮箱账号:{datas[0]}, 输入密码:{datas[1]}'):
            self.wait_for_element(EleLogin.email)
            self.type(EleLogin.email, datas[0])
            self.type(EleLogin.password, datas[1])
        with allure.step('点击登录'):
            self.click(EleLogin.login_button)
            self.click(UserMoney.recharge_charge)
            self.click_link_text(UserMoney.recharge_balance)
        with allure.step(f'点击收费,点击余额,输入充值金额:{datas[2]}'):
            self.type(UserMoney.recharge_amount, datas[2])
        with allure.step('点击提交'):
            self.hover_and_click(UserMoney.recharge_submit, UserMoney.recharge_submit)
            self.wait_for_element_visible(UserMoney.recharge_move)
            self.hover_and_click(UserMoney.recharge_move, UserMoney.recharge_move)
        with allure.step('选择信用卡支付方式'):
            self.wait_for_element(UserMoney.recharge_Payment_method)
            self.hover_and_click(UserMoney.recharge_Payment_method, UserMoney.recharge_Payment_method)
        with allure.step('点击充值'):
            self.click(UserMoney.recharge_submit2)
            sleep(2)
            determine = self.isElementExist('//iframe[@title="安全卡号输入框"]')
        with allure.step('判断用户使用信用卡充值第一次需要输入卡号,到期日期,卡安全码(保存信用卡后无需输入卡号,选择保存的信用卡点击确定即可)'):
            if determine:
                try:
                    self.wait_for_element_visible('//iframe[@title="安全卡号输入框"]')
                    iframe = UserMoney.iframe_card_number
                    self.switch_to_frame(iframe)
                    self.wait_for_element_visible(UserMoney.input_card_number)
                    self.type(UserMoney.input_card_number, '4242 4242 4242 4242')
                    # self.assert_text('4242424242424242', UserMoney.input_card_number)
                    self.switch_to_default_content()
                    iframe2 = UserMoney.iframe_time
                    self.switch_to_frame(iframe2)
                    self.wait_for_element_visible(UserMoney.input_time)
                    self.type(UserMoney.input_time, '0923')
                    # self.assert_text('0923', UserMoney.input_time)
                    self.switch_to_default_content()
                    iframe3 = UserMoney.iframe_security_code
                    self.switch_to_frame(iframe3)
                    self.wait_for_element_visible(UserMoney.input_security_code)
                    self.type(UserMoney.input_security_code, '567')
                # self.assert_text('567', UserMoney.input_security_code)
                    self.switch_to_default_content()
                    sleep(2)
                    self.assert_element_visible(UserMoney.recharge_assert_button)
                    self.click(UserMoney.recharge_button)
                    self.wait_for_element_visible(
                        '//main/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div[2][text()="支付成功"]')
                    self.assert_text('支付成功',
                                     '//main/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div[2][text()="支付成功"]')
                except Exception:
                    self.wait_for_element_visible(UserMoney.recharge_why_button2)
                    self.assert_element_not_visible(UserMoney.recharge_button)
                    self.hover_on_element(UserMoney.recharge_why_button2)
                    self.click(UserMoney.recharge_why_button2)

    @parameterized.expand([[('monkey@mail2.dev.fs77.net', 'qq2000', '10')],
                           [('public@mail2.dev.fs77.net', 'qq2000', '19')],
                           [('freestyle@mail2.dev.fs77.net', 'qq2000', '20')],
                           [('2407114348@mail2.dev.fs77.net', 'qq2000', '30')],
                           [('hey@mail2.dev.fs77.net', 'qq2000', '12')],
                           [('jynivavu@mail2.dev.fs77.net', 'qq2000', '38')],
                           [('kahilu@mail2.dev.fs77.net', 'qq2000', '38')]])
    @allure.title('用户使用Paypal方式充值成功')
    def test_user_Recharge02(self, datas):
        with allure.step(f'输入邮箱账号:{datas[0]}, 输入密码:{datas[1]}'):
            self.wait_for_element(EleLogin.email)
            self.type(EleLogin.email, datas[0])
            self.type(EleLogin.password, datas[1])
        with allure.step('点击登录'):
            self.click(EleLogin.login_button)
            self.click(UserMoney.recharge_charge)
            self.click_link_text(UserMoney.recharge_balance)
        with allure.step(f'点击收费,点击余额,输入充值金额:{datas[2]}'):
            self.type(UserMoney.recharge_amount, datas[2])
        with allure.step('点击提交'):
            self.hover_and_click(UserMoney.recharge_submit, UserMoney.recharge_submit)
            self.wait_for_element_visible(UserMoney.recharge_move)
            self.hover_and_click(UserMoney.recharge_move, UserMoney.recharge_move)
        with allure.step('选择Paypal支付方式'):
            self.wait_for_element(UserMoney.recharge_Payment_method2)
            self.hover_and_click(UserMoney.recharge_Payment_method2, UserMoney.recharge_Payment_method2)
        with allure.step('点击充值'):
            self.click(UserMoney.recharge_submit2)
            sleep(2)
            ele = self.isElementExist(UserPayPal.Paypal_message)
        with allure.step('判断Paypal支付第一次是否需要输入Paypal账号密码'):
            if ele:
                with allure.step('第一次需要输入账号密码,点击我已有账号,点击登录'):
                    self.wait_for_element_visible(UserPayPal.Paypal_message)
                    self.click_if_visible(UserPayPal.Paypal_button)
                    self.wait_for_element_visible(UserPayPal.Paypal_email_if)
                    self.assert_element_visible(UserPayPal.Paypal_email_if)
                with allure.step('输入Paypal账号,点击下一步'):
                    self.type(UserPayPal.Paypal_email, 'sb-mbjq14587653@business.example.com')
                    self.click_if_visible(UserPayPal.Paypal_btn_next)
                    self.wait_for_element_visible(UserPayPal.Paypal_password_if)
                    self.assert_element_visible(UserPayPal.Paypal_password_if)
                with allure.step('输入Paypal密码,点击提交'):
                    self.type(UserPayPal.Paypal_password, 'VP@G8&b#')
                    self.click_if_visible(UserPayPal.Paypal_login)
                    self.wait_for_element_visible(UserPayPal.Paypal_payment)
                    self.click_if_visible(UserPayPal.Paypal_payment_submit)
                with allure.step('断言Paypal支付充值账单成功元素可见'):
                    self.wait_for_element_visible(UserPayPal.Paypal_assert_success)
                    self.assert_element_visible(UserPayPal.Paypal_assert_success)


    @parameterized.expand([[('monkey@mail2.dev.fs77.net', 'qq2000', '10')],
                           [('public@mail2.dev.fs77.net', 'qq2000', '19')],
                           [('freestyle@mail2.dev.fs77.net', 'qq2000', '20')],
                           [('2407114348@mail2.dev.fs77.net', 'qq2000', '30')],
                           [('hey@mail2.dev.fs77.net', 'qq2000', '12')],
                           [('jynivavu@mail2.dev.fs77.net', 'qq2000', '38')],
                           [('kahilu@mail2.dev.fs77.net', 'qq2000', '38')]])
    @allure.title('用户使用支付宝方式充值成功')
    def test_user_Recharge02(self, datas):
        with allure.step(f'输入邮箱账号:{datas[0]}, 输入密码:{datas[1]}'):
            self.wait_for_element(EleLogin.email)
            self.type(EleLogin.email, datas[0])
            self.type(EleLogin.password, datas[1])
        with allure.step('点击登录'):
            self.click(EleLogin.login_button)
            self.click(UserMoney.recharge_charge)
            self.click_link_text(UserMoney.recharge_balance)
        with allure.step(f'点击收费,点击余额,输入充值金额:{datas[2]}'):
            self.type(UserMoney.recharge_amount, datas[2])
        with allure.step('点击提交'):
            self.hover_and_click(UserMoney.recharge_submit, UserMoney.recharge_submit)
            self.wait_for_element_visible(UserMoney.recharge_move)
            self.hover_and_click(UserMoney.recharge_move, UserMoney.recharge_move)
        with allure.step('选择Paypal支付方式'):
            self.wait_for_element(UserMoney.recharge_Payment_method3)
            self.hover_and_click(UserMoney.recharge_Payment_method3, UserMoney.recharge_Payment_method3)
        with allure.step('点击充值'):
            self.click(UserMoney.recharge_submit2)
            sleep(2)
            alipay_ele = self.isElementExist(UserAlipay.Alipay_if)
        with allure.step('判断Paypal支付第一次是否需要输入Paypal账号密码'):
            if alipay_ele:
                with allure.step('第一次需要输入账号密码,点击我已有账号,点击登录'):
                    self.wait_for_element_visible(UserAlipay.Alipay_if2)
                with allure.step('输入支付宝账号'):
                    self.type(UserAlipay.Alipay_username, 'forex_1482393299562@alitest.com')
                    self.wait_for_element_visible(UserAlipay.Alipay_password)
                with allure.step('输入支付宝密码,点击下一步'):
                    self.type(UserAlipay.Alipay_password, 'b111111')
                    self.wait_for_element_visible('#J_foreAgreement')
                    self.hover_and_double_click('#J_foreAgreement', '#J_foreAgreement')
                    self.send_keys('#J_foreAgreement', "\n")
                try:
                    self.wait_for_element_visible(UserAlipay.Alipay_forget_password)
                    self.is_element_visible(UserAlipay.Alipay_forget_password)
                except Exception:
                    self.wait_for_element_visible(UserAlipay.Alipay_confirm_password)
                    self.hover_and_double_click(UserAlipay.Alipay_confirm_password, UserAlipay.Alipay_confirm_password)
                else:
                    self.type('#payPassword_rsainput', 'b111111')
                    self.wait_for_element_visible(UserAlipay.Alipay_confirm_password)
                    self.hover_and_double_click(UserAlipay.Alipay_confirm_password, UserAlipay.Alipay_confirm_password)






    @parameterized.expand([[('hozalute@mail2.dev.fs77.net', 'qq2000', '10')],
                           [('otto@mail2.dev.fs77.net', 'qq2000', '20')],
                           [('2407114348@mail2.dev.fs77.net', 'qq2000', '30')],
                           [('public@mail2.dev.fs77.net', 'qq2000', '5')],
                           [('hey@mail2.dev.fs77.net', 'qq2000', '9')],
                           [('unicode@mail2.dev.fs77.net', 'qq2000', '12')],
                           ])
    @allure.title('用户设置余额提醒阈值成功')
    def test_user_recharge03(self, datas):
        with allure.step(f'输入邮箱账号:{datas[0]}, 输入密码:{datas[1]}'):
            self.wait_for_element(EleLogin.email)
            self.type(EleLogin.email, datas[0])
            self.assert_text(datas[0], EleLogin.email)
            self.type(EleLogin.password, datas[1])
            self.assert_text(datas[1], EleLogin.password)
        with allure.step('点击登录'):
            self.click(EleLogin.login_button)
            self.click(UserMoney.recharge_charge)
            self.click_link_text(UserMoney.recharge_balance)
        with allure.step('点击收费,点击余额,断言余额不足提醒阈值元素存在可见'):
            self.wait_for_element(UserBalanceRemind.recharge_remind)
            self.assert_element_visible(UserBalanceRemind.recharge_remind)
        with allure.step(f'清空余额不足提醒阈值输入框的值,重新输入提醒金额:{datas[2]}'):
            self.clear(UserBalanceRemind.recharge_input)
            self.type(UserBalanceRemind.recharge_input, datas[2])
            self.assert_text(datas[2], UserBalanceRemind.recharge_input)
        with allure.step('点击确定,断言设置成功后,成功弹框已存在'):
            self.click(UserBalanceRemind.recharge_remind_submit)
            self.wait_for_element(UserBalanceRemind.recharge_assert_submit)
            self.assert_element_visible(UserBalanceRemind.recharge_assert_submit)