from Page.site_configuration_elements import *
from utils.read_random import *
import allure

from parameterized import parameterized

from Page.site_elements import EleSite
from seleniumbase import BaseCase

from utils.ele_login import EleLogin
@allure.feature('Loadproxy用户测试')
@allure.story('用户站点模块')
class SiteAddPage(BaseCase):
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


    @parameterized.expand([add_site(5), add_site(4), add_site(7), add_site(6), add_site(9), add_site(12)])
    @allure.title('用户创建站点成功并验证站点生效')
    def site_add01(self, datas):
        with allure.step(f'输入用户邮箱{datas[0]},以及密码:{datas[1]}'):
            self.wait_for_element(EleLogin.email)
            self.type(EleSite.email, datas[0])
            self.is_element_visible(EleSite.email)
            self.type(EleSite.password, datas[1])
            self.is_element_visible(EleSite.password)
        with allure.step('点击登录'):
            self.click(EleSite.login_button)
        with allure.step('点击站点,点击创建'):
            try:
                with allure.step('点击登录按钮后可能一直等待无法进入到用户界面,打开新窗口重新操作'):
                    self.wait_for_element(EleSite.site)
                    self.click(EleSite.site)
            except Exception:
                with allure.step('点击登录按钮后出现异常一直等待无法进入到用户界面,打开新窗口重新操作'):
                    self.open_new_window()
                    self.switch_to_newest_window()
                    self.open_url(EleLogin.url)
                with allure.step(f'输入用户邮箱以及密码'):
                    self.wait_for_element(EleLogin.email)
                    self.type(EleSite.email, datas[0])
                    self.is_element_visible(EleSite.email)
                    self.type(EleSite.password, datas[1])
                    self.is_element_visible(EleSite.password)
                with allure.step('点击登录'):
                    self.click(EleSite.login_button)
                    with allure.step('点击创建站点'):
                        self.assert_element_visible(EleSite.site)
                        self.click(EleSite.site_add)
                        self.assert_element_visible(EleSite.site_add)
                    with allure.step('选择套餐,输入所有正确信息'):
                        self.click(EleSite.taocan)
                        self.assert_element_visible(EleSite.taocan)
                    with allure.step('点击确定'):
                        self.click(EleSite.default)
                        self.type(EleSite.domain_name, datas[2])
                        self.type(EleSite.return_address, datas[3])
                        self.click(EleSite.site_determine)
                        self.wait_for_element_visible(EleSite.site_assert)
                        self.hover_and_click(EleSite.site_assert, EleSite.site_assert)
                    with allure.step('搜索框输入新添加的域名进行查询'):
                        self.click_if_visible(EleSite.site_link)
                        self.wait_for_element_visible(EleSite.input)
                        self.type(EleSite.input, datas[2])
                        self.click(EleSite.site_select)
                        self.wait_for_element_visible(EleSite.site_details)
                        self.click_if_visible(EleSite.site_details)
                        self.wait_for_element(EleSite.return_address2)
                        self.clear(EleSite.return_address2)
                        self.type(EleSite.return_address2, '45.65.44.28')
                        self.hover_and_click(EleSite.site_yes, EleSite.site_yes)
                    with allure.step('等待120秒后,等待系统定时任务更新以便验证站点生效'):
                        self.wait(90)
                    with allure.step('打开浏览器,输入新添加的域名访问,验证生效'):
                        self.open_url(datas[4])
                        self.wait_for_element_visible('//html/body/pre')
                        self.assert_element_visible('//html/body/pre')
                        self.go_back()
                    with allure.step('验证站点正常访问后,重新返回站点设置界面,将站点数据删除,,点击创建'):
                        self.wait_for_element_visible(EleSite.site_link)
                        self.click_if_visible(EleSite.site_link)
                        self.wait_for_element_visible(EleSite.input)
                        self.type(EleSite.input, datas[2])
                        self.click(EleSite.site_select)
                        self.wait_for_element_visible(EleSite.site_clear)
                        self.hover_and_click(EleSite.site_clear, EleSite.site_clear)
                        self.wait_for_element(EleSite.site_clear_button)
                        self.hover_and_click(EleSite.site_clear_button, EleSite.site_clear_button)
                        self.wait_for_element_visible(EleSite.site_assert_success)
                        self.assert_element_visible(EleSite.site_assert_success)


            else:
                with allure.step('点击登录按钮后未出现异常,继续创建站点'):
                    self.assert_element_visible(EleSite.site)
                    self.click(EleSite.site_add)
                    self.assert_element_visible(EleSite.site_add)
                with allure.step('选择套餐,输入所有正确信息'):
                    self.click(EleSite.taocan)
                    self.assert_element_visible(EleSite.taocan)
                with allure.step('点击确定'):
                    self.click(EleSite.default)
                    self.type(EleSite.domain_name, datas[2])
                    self.type(EleSite.return_address, datas[3])
                    self.click(EleSite.site_determine)
                    self.wait_for_element_visible(EleSite.site_assert)
                    self.hover_and_click(EleSite.site_assert, EleSite.site_assert)
                with allure.step('搜索框输入新添加的域名进行查询'):
                    self.click_if_visible(EleSite.site_link)
                    self.wait_for_element_visible(EleSite.input)
                    self.type(EleSite.input, datas[2])
                    self.click(EleSite.site_select)
                    self.wait_for_element_visible(EleSite.site_details)
                    self.click_if_visible(EleSite.site_details)
                    self.wait_for_element(EleSite.return_address2)
                    self.clear(EleSite.return_address2)
                    self.type(EleSite.return_address2, '45.65.44.28')
                    self.hover_and_click(EleSite.site_yes, EleSite.site_yes)
                with allure.step('等待60秒后,等待系统定时任务更新以便验证站点生效'):
                    self.wait(90)
                with allure.step('打开浏览器,输入新添加的域名访问,验证生效'):
                    self.open_url(datas[4])
                    self.wait_for_element_visible('//html/body/pre')
                    self.assert_element_visible('//html/body/pre')
                    self.go_back()
                # with allure.step('验证站点生效后,为站点添加黑白名单'):


                with allure.step('验证站点正常访问后,重新返回站点设置界面,将站点数据删除'):
                    self.wait_for_element_visible(EleSite.site_link)
                    self.click_if_visible(EleSite.site_link)
                    self.wait_for_element_visible(EleSite.input)
                    self.type(EleSite.input, datas[2])
                    self.click(EleSite.site_select)
                    self.wait_for_element_visible(EleSite.site_clear)
                    self.hover_and_click(EleSite.site_clear, EleSite.site_clear)
                    self.wait_for_element(EleSite.site_clear_button)
                    self.hover_and_click(EleSite.site_clear_button, EleSite.site_clear_button)
                    self.wait_for_element_visible(EleSite.site_assert_success)
                    self.assert_element_visible(EleSite.site_assert_success)


    @parameterized.expand(
        [[('otto@mail2.dev.fs77.net', 'qq2000', '123456789', '45.65.44.31')],
         [('otto@mail2.dev.fs77.net', 'qq2000', 'qwertyui', '45.65.44.31')],
         [('freestyle@mail2.dev.fs77.net', 'qq2000', '192.168.1.1', '45.65.44.28')],
         [('otto@mail2.dev.fs77.net', 'qq2000', '192.168.2.2', '45.65.44.28')],
         [('cypher@mail2.dev.fs77.net', 'qq2000', '123456qwert', '45.65.44.28')],
         [('ning@mail2.dev.fs77.net', 'qq2000', '12345qwe!#$', '45.65.44.28')]])
    @allure.title('创建站点失败')
    def test_site_add02(self, datas):
        with allure.step(f'输入用户邮箱:{datas[0]}以及密码:{datas[1]}'):
            self.wait_for_element(EleLogin.email)
            self.type(EleSite.email, datas[0])
            self.assert_text(datas[0], EleSite.email)
            self.type(EleSite.password, datas[1])
            self.assert_text(datas[1], EleSite.password)
        with allure.step('点击登录'):
            self.click(EleSite.login_button)
        with allure.step('点击站点,点击创建'):
            self.wait_for_element(EleSite.site)
            self.click(EleSite.site)
            self.assert_element_visible(EleSite.site)
            self.click(EleSite.site_add)
            self.assert_element_visible(EleSite.site_add)
        with allure.step(f'选择套餐,输入错误域名:{datas[2]}+其他正确'):
            self.wait_for_element_visible(EleSite.taocan)
            self.click(EleSite.taocan)
            self.assert_element_visible(EleSite.taocan)
            # sb.click(EleSite.default)
            self.type(EleSite.domain_name, datas[2])
        with allure.step(f'选择套餐,输入回源地址:{datas[3]}+其他正确'):
            self.type(EleSite.return_address, datas[3])
        with allure.step('点击确定'):
            self.click(EleSite.site_determine)
        with allure.step('点击确定后,系统跳出弹框,提示域名格式错误,断言该弹框存在可见'):
            self.wait_for_element(EleSite.site_faild)
            self.hover_on_element(EleSite.site_faild)
            self.assert_element_visible(EleSite.site_faild)