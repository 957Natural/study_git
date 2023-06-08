import os

import allure
import pytest
from parameterized import parameterized

from Page.site_elements import EleSite
from seleniumbase import BaseCase

from utils.ele_login import EleLogin
class SiteAddPage:
    def site_add01(self, sb, email, password, domainname, returnaddress, ipaddress, url):
        with allure.step(f'输入用户邮箱以及密码'):
            sb.wait_for_element(EleLogin.email)
            sb.type(EleSite.email, email)
            sb.is_element_visible(EleSite.email)
            sb.type(EleSite.password, password)
            sb.is_element_visible(EleSite.password)
        with allure.step('点击登录'):
            sb.click(EleSite.login_button)
        with allure.step('点击站点,点击创建'):
            sb.wait_for_element(EleSite.site)
            sb.click(EleSite.site)
            sb.assert_element_visible(EleSite.site)
            sb.click(EleSite.site_add)
            sb.assert_element_visible(EleSite.site_add)
        with allure.step('选择套餐,输入所有正确信息'):
            sb.click(EleSite.taocan)
            sb.assert_element_visible(EleSite.taocan)
        with allure.step('点击确定'):
            sb.click(EleSite.default)
            sb.type(EleSite.domain_name, domainname)
            sb.type(EleSite.return_address, returnaddress)
            sb.click(EleSite.site_determine)
        with allure.step('搜索框输入新添加的域名进行查询'):
            sb.click_link('列表')
            sb.type(EleSite.input, ipaddress)
            sb.click(EleSite.site_select)
            sb.click_link('详情')
            sb.wait_for_element(EleSite.return_address2)
            sb.clear(EleSite.return_address2)
            sb.type(EleSite.return_address2, '45.65.44.28')
            # sb.click(EleSite.site_default)
            # sb.click(EleSite.site_modify)
            sb.hover_and_click(EleSite.site_yes, EleSite.site_yes)
        with allure.step('等待60秒后,等待系统定时任务更新以便验证站点生效'):
            sb.wait(60)
            sb.open_new_window()
            sb.switch_to_newest_window()
            sb.wait(10)
        with allure.step('打开浏览器,输入新添加的域名访问,验证生效'):
            sb.open_url(url)

    def site_add02(self, sb, email, password, domain_name, return_address):
        with allure.step(f'输入用户邮箱以及密码'):
            sb.wait_for_element(EleLogin.email)
            sb.type(EleSite.email, email)
            sb.is_element_visible(EleSite.email)
            sb.type(EleSite.password, password)
            sb.is_element_visible(EleSite.password)
        with allure.step('点击登录'):
            sb.click(EleSite.login_button)
        with allure.step('点击站点,点击创建'):
            sb.wait_for_element(EleSite.site)
            sb.click(EleSite.site)
            sb.assert_element_visible(EleSite.site)
            sb.click(EleSite.site_add)
            sb.assert_element_visible(EleSite.site_add)
        with allure.step('选择套餐,输入错误域名格式+其他正确'):
            sb.click(EleSite.taocan)
            sb.assert_element_visible(EleSite.taocan)
            sb.click(EleSite.default)
            sb.type(EleSite.domain_name, domain_name)
            sb.type(EleSite.return_address, return_address)
        with allure.step('点击确定'):
            sb.click(EleSite.site_determine)
        with allure.step('点击确定后,系统跳出弹框,提示域名格式错误,断言该弹框存在可见'):
            sb.wait_for_element(EleSite.site_faild)
            sb.hover_on_element(EleSite.site_faild)
            sb.assert_element_visible(EleSite.site_faild)


@allure.feature('Loadproxy用户测试')
@allure.story('用户站点模块')
class TestSite(BaseCase):
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

    @parameterized.expand([[('otto@mail2.dev.fs77.net', 'qq2000', '089.cdn.dev.fs77.net', '45.65.44.28', '089.cdn.dev.fs77.net','http://089.cdn.dev.fs77.net/')],
                           [('otto@mail2.dev.fs77.net', 'qq2000', '088.cdn.dev.fs77.net', '45.65.44.28', '088.cdn.dev.fs77.net','http://088.cdn.dev.fs77.net/')],
                           ])
    @allure.title('用户创建站点成功并验证站点生效')
    def test_site_add01(self,datas):
        SiteAddPage().site_add01(self, datas[0],datas[1],datas[2],datas[3],datas[4],datas[5])

    @parameterized.expand(
        [[('otto@mail2.dev.fs77.net', 'qq2000', '123456789', '45.65.44.31')],
         [('otto@mail2.dev.fs77.net', 'qq2000', 'qwertyui', '45.65.44.31')],
         [('otto@mail2.dev.fs77.net', 'qq2000', '192.168.1.1', '45.65.44.28')],
         [('otto@mail2.dev.fs77.net', 'qq2000', '192.168.2.2', '45.65.44.28')],
         [('otto@mail2.dev.fs77.net', 'qq2000', '123456qwert', '45.65.44.28')],
         [('otto@mail2.dev.fs77.net', 'qq2000', '12345!#$', '45.65.44.28')],
         [('otto@mail2.dev.fs77.net', 'qq2000', '12345qwe!#$', '45.65.44.28')]])
    @allure.title('用户创建站点失败(域名格式错误)')
    def test_site_add02(self, datas):
        SiteAddPage().site_add02(self, datas[0], datas[1], datas[2], datas[3])