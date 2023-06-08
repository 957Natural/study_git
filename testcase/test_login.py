from parameterized import parameterized
from utils.ele_login import *
from seleniumbase import BaseCase
from utils.read_random import *
import allure
@allure.feature('Loadproxy用户测试')
@allure.story('用户登录模块')
class LoadProxyLogin(BaseCase):
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

    @parameterized.expand([[('hozalute@mail2.dev.fs77.net', 'qq2000')],
                           [('otto@mail2.dev.fs77.net', 'qq2000')],
                           [('public@mail2.dev.fs77.net', 'qq2000')]])
    @allure.title('用户登录成功')
    def test_login(self, datas):
        with allure.step(f'输入测试数据: 用户邮箱:{datas[0]}, 用户密码:{datas[1]}'):
            self.wait_for_element(EleLogin.email)
            self.type(EleLogin.email, datas[0])
            self.assert_text(datas[0], EleLogin.email)
            self.type(EleLogin.password, datas[1])
            self.assert_text(datas[1], EleLogin.password)
        with allure.step('点击登录按钮'):
            self.click(EleLogin.login_button)
            self.wait_for_element(f'//div[@id="app"]/section/section/div/header[2]/div[@class="ant-pro-global-header"]/div/span/span[2][text()="{datas[0]}"]')
            self.hover_on_element(f'//div[@id="app"]/section/section/div/header[2]/div[@class="ant-pro-global-header"]/div/span/span[2][text()="{datas[0]}"]')
            self.assert_element_visible(f'//div[@id="app"]/section/section/div/header[2]/div[@class="ant-pro-global-header"]/div/span/span[2][text()="{datas[0]}"]')
        with allure.step('点击退出登录'):
            self.click(EleLogout.wait_logout)
        #     self.wait_for_element(EleLogout.wait_alert)
        # with allure.step('移动到退出登录弹框并点击确定'):
        #     self.hover_on_element(EleLogout.move_alert)
            self.wait_for_element('//div[@role="document"]/div[@class="ant-modal-content"]/div[@class="ant-modal-body"]/div/div[2]')
            self.hover_and_click('//div[@role="document"]/div[@class="ant-modal-content"]/div[@class="ant-modal-body"]/div/div[2]', EleLogout.hover_click_alert)

    @parameterized.expand([login_false2(5),
                           login_false2(4),
                           login_false2(3),
                           login_false2(2),
                           login_false2(1),
                           login_false2(0)])
    @allure.title('用户登录失败(密码不足6位字符)')
    def test_login2(self, datas):
        if datas[1] == '':
            with allure.step(f'输入测试数据: 用户邮箱:{datas[0]}, 用户密码:{datas[1]}'):
                self.open_new_window()
                self.switch_to_newest_window()
                self.open_url(EleLogin.url)
                self.type(EleLogin.email, datas[0])
                self.type(EleLogin.password, datas[1])
            with allure.step('点击登录按钮'):
                self.click(EleLogin.login_button)
                self.wait_for_element(EleLogin.login_password_none)
            with allure.step('输入密码为空时,系统提示请输入密码,断言请输入密码元素可见'):
                self.assert_element_visible(EleLogin.login_password_none)
        else:
            with allure.step(f'输入测试数据: 用户邮箱:{datas[0]}, 用户密码:{datas[1]}'):
                self.type(EleLogin.email, datas[0])
                self.assert_text(datas[0], EleLogin.email)
                self.type(EleLogin.password, datas[1])
                self.assert_text(datas[1], EleLogin.password)
            with allure.step('点击登录按钮'):
                self.click(EleLogin.login_button)
            with allure.step('输入密码错误时,系统提示用户名或密码错误,断言该元素可见'):
                self.assert_element_visible(EleLogin.login_password_faild)


    @parameterized.expand([login_false(10),
                           login_false(15),
                           login_false(18),
                           login_false(19),
                           login_false(17),
                           login_false(8)])
    @allure.title('用户登录失败(邮箱格式错误)')
    def test_login3(self, datas):
            with allure.step(f'输入测试数据: 用户邮箱:{datas[0]}, 用户密码:{datas[1]}'):
                self.type(EleLogin.email, datas[0])
                self.assert_text(datas[0], EleLogin.email)
                self.type(EleLogin.password, datas[1])
                self.assert_text(datas[1], EleLogin.password)
            with allure.step('点击登录按钮'):
                self.click(EleLogin.login_button)
            with allure.step('输入邮箱格式错误时,系统提示用户名或密码错误,断言该元素可见'):
                self.assert_element_visible(EleLogin.login_password_faild)