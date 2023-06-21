import jsonpath
from parameterized import parameterized
from data.site_datas import *
from seleniumbase import BaseCase
from Page.site_elements import *
from Page.site_configuration_elements import *
from utils.ele_login import *
import allure
import requests

@allure.feature('Loadproxy用户测试')
@allure.story('站点配置添加黑白名单')
class UserRegister(BaseCase):
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

    #
    # @parameterized.expand(SiteConfigBlackWhite.black_white_datas)
    # @allure.title('添加站点黑白名单并验证生效')
    # def test_site_config01(self, datas):
    #     with allure.step(f'输入用户邮箱:{datas[0]},以及密码{datas[1]}'):
    #         self.wait_for_element_visible(EleLogin.email)
    #         self.type(EleLogin.email, datas[0])
    #         self.type(EleLogin.password, datas[1])
    #         self.click_if_visible(EleLogin.login_button)
    #     with allure.step('点击创建站点'):
    #         self.assert_element_visible(EleSite.site)
    #         self.click(EleSite.site)
    #         self.click(EleSite.site_add)
    #         self.assert_element_visible(EleSite.site_add)
    #     with allure.step('选择套餐,输入所有正确信息'):
    #         self.click(EleSite.taocan)
    #         self.assert_element_visible(EleSite.taocan)
    #     with allure.step('点击确定'):
    #         self.click(EleSite.default)
    #         self.type(EleSite.domain_name, datas[2])
    #         self.type(EleSite.return_address, datas[3])
    #         self.click(EleSite.site_determine)
    #         self.wait_for_element_visible(EleSite.site_assert)
    #         self.hover_and_click(EleSite.site_assert, EleSite.site_assert)
    #     with allure.step(f'搜索框输入新添加的域名:{datas[2]}进行查询'):
    #         self.click_if_visible(EleSite.site_link)
    #         self.wait_for_element_visible(EleSite.input)
    #         self.type(EleSite.input, datas[2])
    #         self.click(EleSite.site_select)
    #     with allure.step('搜索到添加的站点后,点击详情'):
    #         self.wait_for_element_visible(EleSite.site_details)
    #         self.click_if_visible(EleSite.site_details)
    #         self.wait_for_element_visible(SiteConfigBlackAndWhite.site_request)
    #         self.click(SiteConfigBlackAndWhite.site_request)
    #     with allure.step('点击防盗链保护,点击激活按钮'):
    #         self.hover_and_click(SiteConfigBlackAndWhite.site_protect, SiteConfigBlackAndWhite.site_protect)
    #         self.hover_and_click(SiteConfigBlackAndWhite.site_activation, SiteConfigBlackAndWhite.site_activation)
    #     if datas[6] == '白名单':
    #         with allure.step('判断需要测试白名单时添加白名单Referer'):
    #             self.wait_for_element_visible(SiteConfigBlackAndWhite.site_white_name)
    #             self.click_if_visible(SiteConfigBlackAndWhite.site_white_name)
    #         with allure.step('点击白名单,添加白名单'):
    #             self.wait_for_element_visible(SiteConfigBlackAndWhite.site_domain_name)
    #         with allure.step(f'输入白名单规则域名:{datas[5]}'):
    #             self.type(SiteConfigBlackAndWhite.site_domain_name, datas[5])
    #         with allure.step('打开忽略Schema按钮'):
    #             self.hover_on_element(SiteConfigBlackAndWhite.site_schema)
    #             self.click_if_visible(SiteConfigBlackAndWhite.site_schema)
    #         with allure.step('点击确定按钮并断言白名单添加成功弹框存在'):
    #             self.hover_on_element(SiteConfigBlackAndWhite.site_config_button)
    #             self.click_if_visible(SiteConfigBlackAndWhite.site_config_button)
    #             self.wait_for_element_visible(SiteConfigBlackAndWhite.site_config_assert)
    #             self.assert_element_visible(SiteConfigBlackAndWhite.site_config_assert)
    #             # self.wait(10)
    #         with allure.step('等待10s后,使用浏览器发起请求验证防盗链保护黑名单生效'):
    #             se = requests.Session()
    #             res = se.get(url=datas[4], headers={'Referer': datas[5]})
    #         with allure.step('使用jsonpath获取到响应体的Referer数据和host地址'):
    #             site_config_domain_name = jsonpath.jsonpath(res.json(), '$..HTTP_REFERER')
    #             site_config_host = jsonpath.jsonpath(res.json(), '$..HTTP_HOST')
    #             try:
    #                 with allure.step(f'断言防盗链保护设置的Referer:{datas[5]}和响应体的Referer一致'):
    #                     assert datas[5] == ' '.join(site_config_domain_name)
    #                 with allure.step('断言设置黑名单后,响应码应为403'):
    #                     assert res.status_code == 200
    #                 with allure.step(f'断言站点域名地址:{datas[2]} 和响应体中的HTTP_HOST一致'):
    #                     assert datas[2] == ' '.join(site_config_host)
    #             except Exception:
    #                 self.wait_for_element_visible('#reload-button')
    #                 self.hover_on_element('#reload-button')
    #                 self.double_click('#reload-button')
    #                 assert datas[5] == ' '.join(site_config_domain_name)
    #                 assert res.status_code == 200
    #                 assert datas[2] == ' '.join(site_config_host)
    #
    #     else:
    #         with allure.step('点击黑名单,添加黑名单'):
    #             self.wait_for_element_visible(SiteConfigBlackAndWhite.site_domain_name)
    #         with allure.step(f'输入黑名单规则域名:{datas[5]}'):
    #             self.type(SiteConfigBlackAndWhite.site_domain_name, datas[5])
    #         with allure.step('打开忽略Schema按钮'):
    #             self.hover_on_element(SiteConfigBlackAndWhite.site_schema)
    #             self.click_if_visible(SiteConfigBlackAndWhite.site_schema)
    #         with allure.step('点击确定按钮并断言黑名单添加成功弹框存在'):
    #             self.hover_on_element(SiteConfigBlackAndWhite.site_config_button)
    #             self.click_if_visible(SiteConfigBlackAndWhite.site_config_button)
    #             self.wait_for_element_visible(SiteConfigBlackAndWhite.site_config_assert)
    #             self.assert_element_visible(SiteConfigBlackAndWhite.site_config_assert)
    #             self.wait(10)
    #         with allure.step('等待10s后,使用浏览器发起请求验证防盗链保护黑名单生效'):
    #             se = requests.Session()
    #             res = se.get(url=datas[4], headers={'Referer': datas[5]})
    #         with allure.step('使用jsonpath获取到响应体的Referer数据和host地址'):
    #             site_config_domain_name = jsonpath.jsonpath(res.json(), '$..HTTP_REFERER')
    #             site_config_host = jsonpath.jsonpath(res.json(), '$..HTTP_HOST')
    #             try:
    #                 with allure.step(f'断言防盗链保护设置的Referer:{datas[5]}和响应体的Referer一致'):
    #                     assert datas[5] == ' '.join(site_config_domain_name)
    #                 with allure.step('断言设置黑名单后,响应码应为403'):
    #                     assert res.status_code == 200
    #                 with allure.step(f'断言站点域名地址:{datas[2]} 和响应体中的HTTP_HOST一致'):
    #                     assert datas[2] == ' '.join(site_config_host)
    #             except Exception:
    #                 self.wait_for_element_visible('#reload-button')
    #                 self.hover_on_element('#reload-button')
    #                 self.double_click('#reload-button')
    #                 assert datas[5] == ' '.join(site_config_domain_name)
    #                 assert res.status_code == 200
    #                 assert datas[2] == ' '.join(site_config_host)


    @parameterized.expand(SiteConfigWAFFireWall.firewall_datas)
    @allure.title('添加站点黑白名单并验证生效')
    def test_site_config02(self, datas):
        with allure.step('输入用户邮箱以及密码'):
            self.wait_for_element_visible(EleLogin.email)
            self.type(EleLogin.email, datas[0])
            self.type(EleLogin.password, datas[1])
        with allure.step('点击登录'):
            self.click_if_visible(EleLogin.login_button)
        with allure.step('点击站点,点击列表'):
            self.wait_for_element_visible(SiteConfigWAFFireWall1.site)
            self.click(SiteConfigWAFFireWall1.site)
            self.wait_for_link_text_visible(SiteConfigWAFFireWall1.site_list)
            self.click_link_text(SiteConfigWAFFireWall1.site_list)
        with allure.step(f'选择搜索输入框,输入站点域名: {datas[2]}'):
            self.hover_on_element(SiteConfigWAFFireWall1.select_input)
            self.type(SiteConfigWAFFireWall1.select_input, datas[2])
        with allure.step('点击搜索,搜索到内容后,点击详情'):
            self.click_if_visible(SiteConfigWAFFireWall1.site_select)
            self.wait_for_element_visible(SiteConfigWAFFireWall1.site_details)
            self.hover_and_click(SiteConfigWAFFireWall1.site_details, SiteConfigWAFFireWall1.site_details)
        with allure.step('点击访问控制,点击WAF防火墙规则'):
            self.hover_and_click(SiteConfigWAFFireWall1.site_request, SiteConfigWAFFireWall1.site_request)
            self.hover_and_click(SiteConfigWAFFireWall1.site_waf, SiteConfigWAFFireWall1.site_waf)
        with allure.step(f'点击添加, 名字输入框输入规则名字: {datas[3]}'):
            self.hover_and_click(SiteConfigWAFFireWall1.add, SiteConfigWAFFireWall1.add)
            self.wait_for_element_visible(SiteConfigWAFFireWall1.waf_firewall_name)
            self.type(SiteConfigWAFFireWall1.waf_firewall_name, datas[3])
            self.hover_on_element(SiteConfigWAFFireWall1.waf_select)
            self.click_if_visible(SiteConfigWAFFireWall1.waf_select)
            if datas[6] == '请求方法':
                self.wait_for_element_visible(SiteConfigWAFFireWall1.waf_field1)
                self.hover_and_click(SiteConfigWAFFireWall1.waf_field1, SiteConfigWAFFireWall1.waf_field1)
                self.hover_and_click(SiteConfigWAFFireWall1.waf_types_of, SiteConfigWAFFireWall1.waf_types_of)
                if datas[7][0] == 'get':
                    self.hover_and_click(SiteConfigWAFFireWall1.request_method_get, SiteConfigWAFFireWall1.request_method_get)
                    self.hover_and_click(SiteConfigWAFFireWall1.select_operate,SiteConfigWAFFireWall1.select_operate)
                    if datas[8][0] == '允许':
                        self.hover_and_click(SiteConfigWAFFireWall1.waf_else1, SiteConfigWAFFireWall1.waf_else1)
                        self.hover_and_click(SiteConfigWAFFireWall1.waf_firewall_add_button, SiteConfigWAFFireWall1.waf_firewall_add_button)
                        # self.wait(10)
            elif datas[6] == 'HTTP版本':
                self.wait_for_element_visible(SiteConfigWAFFireWall1.waf_field2)
                self.hover_and_click(SiteConfigWAFFireWall1.waf_field2, SiteConfigWAFFireWall1.waf_field2)
                self.hover_and_click(SiteConfigWAFFireWall1.waf_types_of, SiteConfigWAFFireWall1.waf_types_of)
                self.hover_and_click(SiteConfigWAFFireWall1.waf_http_version, SiteConfigWAFFireWall1.waf_http_version)
                self.hover_and_click(SiteConfigWAFFireWall1.select_operate, SiteConfigWAFFireWall1.select_operate)
                if datas[8][0] == '允许':
                    self.hover_and_click(SiteConfigWAFFireWall1.waf_else1, SiteConfigWAFFireWall1.waf_else1)
                    self.hover_and_click(SiteConfigWAFFireWall1.waf_firewall_add_button,
                                         SiteConfigWAFFireWall1.waf_firewall_add_button)
                    # self.wait(10)


            elif datas[6][2] == 'HTTP请求头':
                self.wait_for_element_visible(SiteConfigWAFFireWall1.waf_field3)
                self.hover_and_click(SiteConfigWAFFireWall1.waf_field3, SiteConfigWAFFireWall1.waf_field3)
                self.hover_on_element(SiteConfigWAFFireWall1.request_header_name)
                self.type(SiteConfigWAFFireWall1.request_header_name, 'Content-Type')
                if datas[8][0] == 'application/json; charset=utf-8':
                    self.wait_for_element(SiteConfigWAFFireWall1.waf_types_of)
                    self.type(SiteConfigWAFFireWall1.waf_types_of, 'application/json')

            # elif datas[6][3] == 'URL':
            #     self.wait_for_element_visible(SiteConfigWAFFireWall1.waf_field4)
            #     self.hover_and_click(SiteConfigWAFFireWall1.waf_field4, SiteConfigWAFFireWall1.waf_field4)
            #     self.hover_and_click(SiteConfigWAFFireWall1.waf_types_of, SiteConfigWAFFireWall1.waf_types_of)
            # elif datas[6][4] == 'URL路径':
            #     self.wait_for_element_visible(SiteConfigWAFFireWall1.waf_field5)
            #     self.hover_and_click(SiteConfigWAFFireWall1.waf_field5, SiteConfigWAFFireWall1.waf_field5)
            #     self.hover_and_click(SiteConfigWAFFireWall1.waf_types_of, SiteConfigWAFFireWall1.waf_types_of)



























