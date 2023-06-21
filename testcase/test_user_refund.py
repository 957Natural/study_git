
import allure
from seleniumbase import BaseCase
from utils.ele_login import *
from parameterized import parameterized
from utils.read_random import *
from Page.user_refund_elements import *

@allure.feature('Loadproxy用户测试')
@allure.story('用户退款模块')
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

    @parameterized.expand(
        [[('monkey@mail2.dev.fs77.net', 'qq2000', 'test',)],
         [('public@mail2.dev.fs77.net', 'qq2000', 'test',)],
         [('freestyle@mail2.dev.fs77.net', 'qq2000', 'test',)],
         [('2407114348@mail2.dev.fs77.net', 'qq2000', 'test',)],
         [('hey@mail2.dev.fs77.net', 'qq2000', 'test')],
         [('jynivavu@mail2.dev.fs77.net', 'qq2000', 'test')],
         [('kahilu@mail2.dev.fs77.net', 'qq2000', 'test')]])
    @allure.title('用户退款成功')
    def test_user_refund110(self, datas):
        with allure.step('输入用户邮箱密码,点击登录'):
            self.wait_for_element(EleLogin.email)
            self.type(EleLogin.email, datas[0])
            self.type(EleLogin.password, datas[1])
            self.click(EleLogin.login_button)
        with allure.step('点击账单,选择需要退款的账单,点击详情,点击退款'):
            self.wait_for_element_visible(UserRefund.recharge)
            self.click(UserRefund.recharge)
            self.hover_and_click(UserRefund.bill, UserRefund.bill)
            self.hover_on_element(UserRefund.details)
            self.click_if_visible(UserRefund.details)
            self.wait_for_element_visible(UserRefund.refund_assert)
        with allure.step('断言退款的订单状态为服务成功'):
            self.assert_text('服务成功', UserRefund.refund_assert)
            self.hover_on_element(UserRefund.refund_button)
            self.click_if_visible(UserRefund.refund_button)
            self.wait_for_element_visible(UserRefund.refund_path)
            self.assert_element_visible(UserRefund.refund_path)
            self.type(UserRefund.refund_message, datas[2])
            self.hover_on_element(UserRefund.refund_determine)
        with allure.step('点击确认退款'):
            self.click_if_visible(UserRefund.refund_determine)
            self.hover_and_click(UserRefund.refund_determine2, UserRefund.refund_determine2)
            self.hover_on_element(UserRefund.refund_back2)
            self.click_if_visible(UserRefund.refund_back2)
            self.hover_on_element(UserRefund.refund_back)
            self.click_if_visible(UserRefund.refund_back)
        with allure.step('断情确认退款后,新增的退款申请状态为等待'):
            self.wait_for_element_visible(UserRefund.refund_wait)
            self.assert_element_visible(UserRefund.refund_wait)
            self.assert_text('等待', UserRefund.refund_wait)

