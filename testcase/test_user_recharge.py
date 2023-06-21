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
        with allure.step('判断登录页面打开是否一直等待加载不出来'):
            try:
                self.open_url(EleLogin.url)
                self.maximize_window()
            except Exception:
                with allure.step('页面加载不出来时重新打开新窗口操作'):
                    self.open_new_window()
                    self.switch_to_newest_window()
                    self.open_url(EleLogin.url)
                try:
                    self.wait_for_element_visible(EleLogin.language)
                    self.hover_and_click(EleLogin.language, EleLogin.language)
                    self.wait_for_element(EleLogin.click_language_cn)
                    self.hover_and_click(EleLogin.click_language_cn, EleLogin.click_language_cn)
                    with allure.step('断言登录界面文本为中文'):
                        self.wait_for_element(EleLogin.language_assert)
                        self.assert_text('登录', EleLogin.language_assert)
                except Exception as e:
                    with allure.step('打开登录界面,出现加载超时等待不到元素出现,重新打开新窗口进行登录'):
                        self.open_new_window()
                        self.switch_to_newest_window()
                        self.open_url(EleLogin.url)
                        self.wait_for_element_visible(EleLogin.language)
                        self.hover_and_click(EleLogin.language, EleLogin.language)
                        self.wait_for_element(EleLogin.click_language_cn)
                        self.hover_and_click(EleLogin.click_language_cn, EleLogin.click_language_cn)
                    with allure.step('断言登录界面文本为中文'):
                        self.wait_for_element(EleLogin.language_assert)
                        self.assert_text('登录', EleLogin.language_assert)
            else:
                with allure.step('页面正常加载'):
                    try:
                        self.wait_for_element_visible(EleLogin.language)
                        self.hover_and_click(EleLogin.language, EleLogin.language)
                        self.wait_for_element(EleLogin.click_language_cn)
                        self.hover_and_click(EleLogin.click_language_cn, EleLogin.click_language_cn)
                        with allure.step('断言登录界面文本为中文'):
                            self.wait_for_element(EleLogin.language_assert)
                            self.assert_text('登录', EleLogin.language_assert)
                    except Exception:
                        self.open_new_window()
                        self.switch_to_newest_window()
                        self.open_url(EleLogin.url)
                        self.wait_for_element_visible(EleLogin.language)
                        self.hover_and_click(EleLogin.language, EleLogin.language)
                        self.wait_for_element(EleLogin.click_language_cn)
                        self.hover_and_click(EleLogin.click_language_cn, EleLogin.click_language_cn)
                        with allure.step('断言登录界面文本为中文'):
                            self.wait_for_element(EleLogin.language_assert)
                            self.assert_text('登录', EleLogin.language_assert)

    @parameterized.expand([[('monkey@mail2.dev.fs77.net', 'qq2000', '10', '4242 4242 4242 4242', '0923', '567')],
                           [('otto@mail2.dev.fs77.net', 'qq2000', '20', '4242 4242 4242 4242', '0923', '567')],
                           [('2407114348@mail2.dev.fs77.net', 'qq2000', '30', '4242 4242 4242 4242', '0923', '567')],
                           [('hey@mail2.dev.fs77.net', 'qq2000', '12', '4242 4242 4242 4242', '0923', '567')],
                           [('kahilu@mail2.dev.fs77.net', 'qq2000', '38', '4242 4242 4242 4242', '0923', '567')],
                           [('jynivavu@mail2.dev.fs77.net', 'qq2000', '38', '4242 4242 4242 4242', '0923', '567')],
                           [('moonight@mail2.dev.fs77.net', 'qq2000', '42', '4242 4242 4242 4242', '0923', '567')],
                           [('long@mail2.dev.fs77.net', 'qq2000', '26', '4242 4242 4242 4242', '0923', '567')],
                           [('ning@mail2.dev.fs77.net', 'qq2000', '88', '4242 4242 4242 4242', '0923', '567')]])
    @allure.title('用户使用信用卡方式充值成功')
    def test_user_recharge(self, datas):
        with allure.step(f'输入邮箱账号:{datas[0]}, 输入密码:{datas[1]}'):
            self.wait_for_element(EleLogin.email)
            self.type(EleLogin.email, datas[0])
            self.type(EleLogin.password, datas[1])
        with allure.step('点击登录'):
            self.click(EleLogin.login_button)
            self.click(UserMoney.recharge_charge)
            self.wait_for_link_text_visible(UserMoney.recharge_balance)
            self.click_link_text(UserMoney.recharge_balance)
        with allure.step(f'点击收费,点击余额,输入充值金额:{datas[2]}'):
            self.wait_for_element_visible(UserMoney.recharge_amount)
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
        with allure.step(
                '判断用户使用信用卡充值第一次需要输入卡号,到期日期,卡安全码(保存信用卡后无需输入卡号,选择保存的信用卡点击确定即可)'):
            if determine:
                try:
                    self.wait_for_element_visible('//iframe[@title="安全卡号输入框"]')
                    iframe = UserMoney.iframe_card_number
                    self.switch_to_frame(iframe)
                    self.wait_for_element_visible(UserMoney.input_card_number)
                    with allure.step(f'输入信用卡卡号:{datas[3]}'):
                        self.type(UserMoney.input_card_number, datas[3])
                        # self.assert_text('4242424242424242', UserMoney.input_card_number)
                        self.switch_to_default_content()
                        iframe2 = UserMoney.iframe_time
                        self.switch_to_frame(iframe2)
                        self.wait_for_element_visible(UserMoney.input_time)
                    with allure.step(f'输入信用卡密码:{datas[4]}'):
                        self.type(UserMoney.input_time, datas[4])
                        self.switch_to_default_content()
                        iframe3 = UserMoney.iframe_security_code
                        self.switch_to_frame(iframe3)
                        self.wait_for_element_visible(UserMoney.input_security_code)
                    with allure.step(f'输入信用卡安全码:{datas[5]}'):
                        self.type(UserMoney.input_security_code, datas[5])
                        self.switch_to_default_content()
                        self.assert_element_visible(UserMoney.recharge_assert_button)
                    with allure.step('点击确定提交'):
                        self.click(UserMoney.recharge_button)
                    with allure.step('断言信用卡支付成功'):
                        self.wait_for_element_visible(UserMoney.recharge_assert_success)
                        self.assert_element_visible(UserMoney.recharge_assert_success)
                except Exception:
                    with allure.step('用户已经保存信用卡,以后支付无需输入卡号和密码'):
                        self.wait_for_element_visible(UserMoney.recharge_why_button2)
                        self.assert_element_not_visible(UserMoney.recharge_button)
                        self.hover_on_element(UserMoney.recharge_why_button2)
                    with allure.step('用户已经保存信用卡,以后支付无需输入卡号和密码'):
                        self.click(UserMoney.recharge_why_button2)
                    with allure.step('断言信用卡支付成功'):
                        self.wait_for_element_visible(UserMoney.recharge_assert_success)
                        self.assert_element_visible(UserMoney.recharge_assert_success)

    @parameterized.expand(
        [[('monkey@mail2.dev.fs77.net', 'qq2000', '10', 'sb-mbjq14587653@business.example.com', 'VP@G8&b#')],
         [('public@mail2.dev.fs77.net', 'qq2000', '19', 'sb-mbjq14587653@business.example.com', 'VP@G8&b#')],
         [('freestyle@mail2.dev.fs77.net', 'qq2000', '20', 'sb-mbjq14587653@business.example.com', 'VP@G8&b#')],
         [('2407114348@mail2.dev.fs77.net', 'qq2000', '30', 'sb-mbjq14587653@business.example.com', 'VP@G8&b#')],
         [('hey@mail2.dev.fs77.net', 'qq2000', '12', 'sb-mbjq14587653@business.example.com', 'VP@G8&b#')],
         [('jynivavu@mail2.dev.fs77.net', 'qq2000', '38', 'sb-mbjq14587653@business.example.com', 'VP@G8&b#')],
         [('kahilu@mail2.dev.fs77.net', 'qq2000', '38', 'sb-mbjq14587653@business.example.com', 'VP@G8&b#')],
         [('moonight@mail2.dev.fs77.net', 'qq2000', '42', 'sb-mbjq14587653@business.example.com', 'VP@G8&b#')],
         [('long@mail2.dev.fs77.net', 'qq2000', '26', 'sb-mbjq14587653@business.example.com', 'VP@G8&b#')],
         [('ning@mail2.dev.fs77.net', 'qq2000', '88', 'sb-mbjq14587653@business.example.com', 'VP@G8&b#')]])
    @allure.title('用户使用Paypal方式充值成功')
    def test_user_recharge02(self, datas):
        with allure.step(f'输入邮箱账号:{datas[0]}, 输入密码:{datas[1]}'):
            self.wait_for_element(EleLogin.email)
            self.type(EleLogin.email, datas[0])
            self.type(EleLogin.password, datas[1])
        with allure.step('点击登录'):
            self.click(EleLogin.login_button)
            self.click(UserMoney.recharge_charge)
            self.wait_for_link_text_visible(UserMoney.recharge_balance)
            self.click_link_text(UserMoney.recharge_balance)
        with allure.step(f'点击收费,点击余额,输入充值金额:{datas[2]}'):
            self.wait_for_element_visible(UserMoney.recharge_amount)
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
            if ele:
                try:
                    with allure.step('判断第一次需要输入账号密码,点击我已有账号,点击登录'):
                        self.wait_for_element_visible(UserPayPal.Paypal_message)
                        self.click_if_visible(UserPayPal.Paypal_button)
                        self.wait_for_element_visible(UserPayPal.Paypal_email_if)
                        self.assert_element_visible(UserPayPal.Paypal_email_if)
                    with allure.step(f'输入Paypal账号:{datas[3]}'):
                        self.type(UserPayPal.Paypal_email, datas[3])
                        self.click_if_visible(UserPayPal.Paypal_btn_next)
                        self.wait_for_element_visible(UserPayPal.Paypal_password_if)
                        self.assert_element_visible(UserPayPal.Paypal_password_if)
                    with allure.step(f'输入Paypal密码:{datas[4]},点击提交'):
                        self.type(UserPayPal.Paypal_password, datas[4])
                        self.click_if_visible(UserPayPal.Paypal_login)
                        self.wait_for_element_visible(UserPayPal.Paypal_payment)
                        self.click_if_visible(UserPayPal.Paypal_payment_submit)
                    with allure.step('断言Paypal支付充值账单成功元素可见'):
                        self.wait_for_element_visible(UserPayPal.Paypal_assert_success)
                        self.assert_element_visible(UserPayPal.Paypal_assert_success)
                except Exception:
                    with allure.step('可能会出现不跳转到选择登录界面,会跳转到输入账号密码界面'):
                        self.wait_for_element_visible(UserPayPal.Paypal_email)
                        self.clear(UserPayPal.Paypal_email)
                    with allure.step(f'输入Paypal账号:{datas[3]}'):
                        self.type(UserPayPal.Paypal_email, datas[3])
                    with allure.step(f'输入Paypal密码:{datas[4]},点击提交'):
                        self.type(UserPayPal.Paypal_password, datas[4])
                        self.hover_and_click(UserPayPal.Paypal_login, UserPayPal.Paypal_login)
                        self.wait_for_element_visible(UserPayPal.Paypal_payment)
                        self.click_if_visible(UserPayPal.Paypal_payment_submit)
                    with allure.step('断言Paypal支付充值账单成功元素可见'):
                        self.wait_for_element_visible(UserPayPal.Paypal_assert_success)
                        self.assert_element_visible(UserPayPal.Paypal_assert_success)
    #
    @parameterized.expand([[('hpq@mail2.dev.fs77.net', 'qq2000', '10', 'forex_1482393299562@alitest.com', 'b111111')],
                           [('pdd@mail2.dev.fs77.net', 'qq2000', '19', 'forex_1482393299562@alitest.com', 'b111111')],
                           [('homi@mail2.dev.fs77.net', 'qq2000', '20', 'forex_1482393299562@alitest.com', 'b111111')],
                           [('jynivavu@mail2.dev.fs77.net', 'qq2000', '30', 'forex_1482393299562@alitest.com',
                             'b111111')]])
    @allure.title('用户使用支付宝方式充值成功')
    def test_user_recharge03(self, datas):
        with allure.step(f'输入邮箱账号:{datas[0]}, 输入密码:{datas[1]}'):
            self.wait_for_element(EleLogin.email)
            self.type(EleLogin.email, datas[0])
            self.type(EleLogin.password, datas[1])
        with allure.step('点击登录'):
            self.click(EleLogin.login_button)
            self.click(UserMoney.recharge_charge)
            self.wait_for_link_text_visible(UserMoney.recharge_balance)
            self.click_link_text(UserMoney.recharge_balance)
        with allure.step(f'点击收费,点击余额,输入充值金额:{datas[2]}'):
            self.wait_for_element_visible(UserMoney.recharge_amount)
            self.type(UserMoney.recharge_amount, datas[2])
        with allure.step('点击提交'):
            self.hover_and_click(UserMoney.recharge_submit, UserMoney.recharge_submit)
            self.wait_for_element_visible(UserMoney.recharge_move)
            self.hover_and_click(UserMoney.recharge_move, UserMoney.recharge_move)
        with allure.step('选择支付宝支付方式'):
            self.wait_for_element(UserMoney.recharge_Payment_method3)
            self.hover_and_click(UserMoney.recharge_Payment_method3, UserMoney.recharge_Payment_method3)
        with allure.step('点击充值'):
            self.click(UserMoney.recharge_submit2)
            alipay_ele = self.isElementExist(UserAlipay.Alipay_if)
        with allure.step('判断支付宝支付第一次是否需要输入支付宝账号密码'):
            if alipay_ele:
                try:
                    with allure.step('第一次需要输入账号密码,点击我已有账号,点击登录'):
                        self.wait_for_element_visible(UserAlipay.Alipay_if2)
                except Exception:
                    with allure.step('选择支付宝方式点击确定后出现异常404,重新打开新窗口进行充值'):
                        self.open_new_window()
                        self.switch_to_newest_window()
                        self.open_url(EleLogin.url)
                        self.click(UserMoney.recharge_charge)
                        self.wait_for_link_text_visible(UserMoney.recharge_balance)
                        self.click_link_text(UserMoney.recharge_balance)
                    with allure.step(f'点击收费,点击余额,输入充值金额:{datas[2]}'):
                        self.wait_for_element_visible(UserMoney.recharge_amount)
                        self.type(UserMoney.recharge_amount, datas[2])
                    with allure.step('点击提交'):
                        self.hover_and_click(UserMoney.recharge_submit, UserMoney.recharge_submit)
                        self.wait_for_element_visible(UserMoney.recharge_move)
                        self.hover_and_click(UserMoney.recharge_move, UserMoney.recharge_move)
                    with allure.step('选择支付宝支付方式,点击提交'):
                        self.wait_for_element(UserMoney.recharge_Payment_method3)
                        self.hover_and_click(UserMoney.recharge_Payment_method3, UserMoney.recharge_Payment_method3)
                        self.click(UserMoney.recharge_submit2)
                        self.wait_for_element_visible(UserAlipay.Alipay_username)
                    with allure.step(f'输入支付宝账号:{datas[3]}'):
                        self.type(UserAlipay.Alipay_username, datas[3])
                        self.assert_text(datas[3], UserAlipay.Alipay_username)
                        self.wait_for_element_visible(UserAlipay.Alipay_password)
                    with allure.step(f'输入支付宝密码:{datas[4]}, 点击下一步'):
                        self.type(UserAlipay.Alipay_password, datas[4])
                        self.assert_text(datas[4], UserAlipay.Alipay_password)
                        self.wait_for_element_visible(UserAlipay.Alipay_next_button)
                        self.hover_and_double_click(UserAlipay.Alipay_next_button, UserAlipay.Alipay_next_button)
                        self.send_keys(UserAlipay.Alipay_next_button, "\n")
                        try:
                            self.find_element('#payPassword_rsainput')
                            self.wait_for_element_visible(UserAlipay.Alipay_forget_password)
                        except Exception:
                            self.type('#payPassword_rsainput', datas[4])
                            self.wait_for_element_visible(UserAlipay.Alipay_confirm_password)
                            self.hover_and_double_click(UserAlipay.Alipay_confirm_password,
                                                        UserAlipay.Alipay_confirm_password)
                        else:
                            self.wait_for_element_visible(UserAlipay.Alipay_confirm_password)
                            self.hover_and_double_click(UserAlipay.Alipay_confirm_password,
                                                        UserAlipay.Alipay_confirm_password)

                else:
                    with allure.step(f'输入支付宝账号:{datas[3]}'):
                        self.wait_for_element_visible(UserAlipay.Alipay_username)
                        self.type(UserAlipay.Alipay_username, datas[3])
                        self.assert_text(datas[3], UserAlipay.Alipay_username)
                        self.wait_for_element_visible(UserAlipay.Alipay_password)
                    with allure.step(f'输入支付宝密码:{datas[4]}, 点击下一步'):
                        self.type(UserAlipay.Alipay_password, datas[4])
                        self.assert_text(datas[4], UserAlipay.Alipay_password)
                        self.wait_for_element_visible(UserAlipay.Alipay_next_button)
                        self.hover_and_double_click(UserAlipay.Alipay_next_button, UserAlipay.Alipay_next_button)
                        self.send_keys(UserAlipay.Alipay_next_button, "\n")
                    try:
                        self.find_element('#payPassword_rsainput')
                        self.wait_for_element_visible(UserAlipay.Alipay_forget_password)
                    except Exception as a:
                        self.wait_for_element_visible(UserAlipay.Alipay_confirm_password)
                        self.hover_and_double_click(UserAlipay.Alipay_confirm_password,
                                                    UserAlipay.Alipay_confirm_password)
                    else:
                        self.type('#payPassword_rsainput', datas[4])
                        self.wait_for_element_visible(UserAlipay.Alipay_confirm_password)
                        self.hover_and_double_click(UserAlipay.Alipay_confirm_password,
                                                    UserAlipay.Alipay_confirm_password)


    @parameterized.expand([[('hozalute@mail2.dev.fs77.net', 'qq2000', '10')],
                           [('otto@mail2.dev.fs77.net', 'qq2000', '8')],
                           [('2407114348@mail2.dev.fs77.net', 'qq2000', '21')],
                           [('public@mail2.dev.fs77.net', 'qq2000', '5')],
                           [('hey@mail2.dev.fs77.net', 'qq2000', '9')],
                           [('unicode@mail2.dev.fs77.net', 'qq2000', '12')],
                           [('moonight@mail2.dev.fs77.net', 'qq2000', '15')],
                           [('long@mail2.dev.fs77.net', 'qq2000', '4')],
                           [('ning@mail2.dev.fs77.net', 'qq2000', '17')]
                           ])
    @allure.title('用户设置余额提醒阈值成功')
    def test_user_recharge04(self, datas):
        with allure.step(f'输入邮箱账号:{datas[0]}, 输入密码:{datas[1]}'):
            self.wait_for_element(EleLogin.email)
            self.type(EleLogin.email, datas[0])
            self.assert_text(datas[0], EleLogin.email)
            self.type(EleLogin.password, datas[1])
            self.assert_text(datas[1], EleLogin.password)
        with allure.step('点击登录'):
            self.click(EleLogin.login_button)
            self.click(UserMoney.recharge_charge)
            self.wait_for_link_text_visible(UserMoney.recharge_balance)
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