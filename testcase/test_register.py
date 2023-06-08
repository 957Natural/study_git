import allure
from seleniumbase import BaseCase
from Page.register_elements import Register
from utils.ele_login import *
from parameterized import parameterized
from utils.read_random import *
@allure.feature('Loadproxy用户测试')
@allure.story('用户注册模块')
class UserRegister(BaseCase):
    @allure.title('打开LoadProxy官网选择语言为中文')
    def setUp(self):
        super().setUp()
        with allure.step('选择语言为中文避免测试失败'):
            self.open_url(EleLogin.url)
            self.maximize_window()
            # self.wait_for_element(EleLogin.language)
            self.hover_and_click(EleLogin.language, EleLogin.language)
            self.wait_for_element(EleLogin.click_language_en)
            self.hover_and_click(EleLogin.click_language_en, EleLogin.click_language_en)
            self.hover_and_click(EleLogin.language, EleLogin.language)
            self.wait_for_element(EleLogin.click_language_cn)
            self.hover_and_click(EleLogin.click_language_cn, EleLogin.click_language_cn)
        with allure.step('断言登录界面文本为中文'):
            self.wait_for_element(EleLogin.language_assert)
            self.assert_text('登录', EleLogin.language_assert)


    @parameterized.expand([generate_random_code(6),
                           generate_random_code(6),
                           generate_random_code(5),
                           generate_random_code(5),
                           generate_random_code(4),
                           generate_random_code(4),
                           generate_random_code(3),
                           generate_random_code(3),
                           generate_random_code(2),
                           generate_random_code(2),
                           generate_random_code(7),
                           generate_random_code(7),
                           generate_random_code(9),])
    @allure.title('注册成功(随机数邮箱长度)')
    def test_user_register(self, datas):
        with allure.step('点击注册'):
            self.wait_for_element(EleLogin.email)
            self.click_link_text('注册')
            self.wait_for_element(Register.register_email)
        with allure.step(f'输入随机数邮箱:{datas[0]}, 输入密码:{datas[1]}, 输入确认密码:{datas[1]}'):
            self.type(Register.register_email, datas[0])
            self.assert_text(datas[0], Register.register_email)
            self.type(Register.register_password, datas[1])
            self.assert_text(datas[1], Register.register_password)
            self.type(Register.register_yes_password, datas[1])
            self.assert_text(datas[1], Register.register_password)
        with allure.step('勾选我已阅读协议'):
            self.hover_and_click(Register.register_check_agreement, Register.register_check_agreement)
        with allure.step('点击确定注册'):
            self.wait_for_element(Register.register_click_button)
            self.click(Register.register_click_button)


