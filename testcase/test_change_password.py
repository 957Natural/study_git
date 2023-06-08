import allure
from parameterized import parameterized

from seleniumbase import BaseCase
from utils.ele_login import *
from Page.change_password import ChangePassword
BaseCase.main(__name__, __file__)



@allure.feature('Loadproxy用户测试')
@allure.story('用户修改密码模块')
class ChangePassWord(BaseCase):
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

    @parameterized.expand(
        [[('13538506002@mail2.dev.fs77.net', 'qq2000', 'qq2000', 'qq200011','qq200011', 'qq200011')],
         [('veryry@mail2.dev.fs77.net', 'qq2000', 'qq2000', 'qq200022','qq200022', 'qq200022')],
         [('hang@mail2.dev.fs77.net', 'qq2000', 'qq2000', 'qq200033','qq200033', 'qq200033')],
         [('cong@mail2.dev.fs77.net', 'qq2000', 'qq2000', 'qq200044','qq200044', 'qq200044')]])
    @allure.title('修改密码成功,验证修改后的密码正常登录')
    def test_change_password(self, datas):
        with allure.step(f'输入测试数据, 邮箱:{datas[0]}, 密码:{datas[1]}'):
            self.wait_for_element(EleLogin.email)
            self.type(EleLogin.email, datas[0])
            self.type(EleLogin.password, datas[1])
        with allure.step('点击登录'):
            self.click(EleLogin.login_button)
        with allure.step('点击账户,点击修改密码'):
            self.wait_for_element(ChangePassword.click_account)
            self.click(ChangePassword.click_account)
            self.click_link_text('修改密码')
        with allure.step(f'输入原密码:{datas[2]}, 新密码:{datas[3]}, 确认新密码:{datas[4]}'):
            self.type(ChangePassword.original, datas[2])
            self.type(ChangePassword.new_password, datas[3])
            self.type(ChangePassword.confirm_password, datas[4])
        with allure.step('点击确定'):
            self.click(ChangePassword.submit)
            self.wait_for_element(ChangePassword.password_alert)
        with allure.step('点击确定修改密码后,系统会弹出修改成功的弹框,断言该弹框存在并可见'):
            self.assert_element_visible(ChangePassword.password_alert)
        with allure.step('退出登录'):
            self.wait_for_element(f'//div/header[2]/div/div/span[1]/span[2][text()="{datas[0]}"]')
            self.hover_on_element(f'//div/header[2]/div/div/span[1]/span[2][text()="{datas[0]}"]')
            self.wait_for_element_clickable(EleLogout.wait_logout)
            self.assert_element_visible(EleLogout.wait_logout)
            self.click(EleLogout.click_logout)
            self.wait_for_element(EleLogout.wait_alert)
            self.hover_on_element(EleLogout.move_alert)
            self.wait_for_element(EleLogout.hover_click_alert)
            self.hover_and_click(EleLogout.hover_click_alert, EleLogout.hover_click_alert)
        with allure.step(f'重新登录,输入邮箱:{datas[0]}, 输入修改后的密码:{datas[5]}'):
            self.wait_for_element(EleLogin.email)
            self.type(EleLogin.email, datas[0])
            self.type(EleLogin.password, datas[5])
        with allure.step('点击登录,验证修改后的密码可以正常登录'):
            self.click(EleLogin.login_button)
            self.wait_for_element(f'//div/header[2]/div/div/span[1]/span[2][text()="{datas[0]}"]')
            self.assert_element_visible(f'//div/header[2]/div/div/span[1]/span[2][text()="{datas[0]}"]')


