import pytest
import os

from parameterized import parameterized

from seleniumbase import BaseCase
from utils.ele_login import EleLogin
from Page.add_account_elements import AddAccount
from utils.read_random import *

BaseCase.main(__name__, __file__)
import allure
@allure.feature('Loadproxy用户测试')
@allure.story('子账户模块')
class SubAccount(BaseCase):
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


    @parameterized.expand([add_account_success_random(7), add_account_success_random(6),
                           add_account_success_random(5), add_account_success_random(4),
                           add_account_success_random(12)])
    @allure.title('创建子账户成功')
    def test_add_account(self, datas):
        with allure.step('输入用户邮箱密码,点击登录'):
            self.wait_for_element(EleLogin.email)
            self.type(EleLogin.email, 'otto@mail2.dev.fs77.net')
            self.type(EleLogin.password, 'qq2000')
            self.click(EleLogin.login_button)
            self.wait_for_element(AddAccount.account)
        with allure.step('点击账户,点击子账户,点击添加,输入所有必填正确信息,点击确定'):
            self.click(AddAccount.account)
            self.click_link_text('子账户')
            self.click(AddAccount.account_add)
        with allure.step(f'输入测试数据: 子账户邮箱:{datas[0]}, 子账户密码:{datas[1]}'):
            self.type(AddAccount.account_email, datas[0])
            self.type(AddAccount.account_pwd, datas[1])
            self.type(AddAccount.account_phone, datas[2])
            self.type(AddAccount.account_firstname, datas[3])
            self.type(AddAccount.account_lastname, datas[4])
            self.click(AddAccount.account_language)
            self.hover_and_click(AddAccount.account_zh_cn, AddAccount.account_zh_cn)
            self.click(AddAccount.account_timezone)
            self.hover_and_click(AddAccount.account_timezone,AddAccount.account_time)
            self.click(AddAccount.click_submit)


    @parameterized.expand([add_account_false_ramdom(9), add_account_false_ramdom(7), add_account_false_ramdom(4),add_account_false_ramdom(3), add_account_false_ramdom(8), add_account_false_ramdom(10)])
    @allure.title('创建子账户失败,邮箱格式错误')
    def test_add_account02(self, datas):
        with allure.step('输入用户邮箱密码,点击登录'):
            self.wait_for_element(EleLogin.email)
            self.type(EleLogin.email, 'public@mail2.dev.fs77.net')
            self.type(EleLogin.password, 'qq2000')
            self.click(EleLogin.login_button)
        with allure.step('点击账户,点击子账户,点击添加,输入错误邮箱格式+所有必填正确信息,点击确定'):
            self.wait_for_element(AddAccount.account)
            self.click(AddAccount.account)
            self.click_link_text('子账户')
            self.click(AddAccount.account_add)
        with allure.step(f'输入测试数据: 子账户邮箱:{datas[0]}, 子账户密码:{datas[1]}'):
            self.type(AddAccount.account_email, datas[0])
            self.type(AddAccount.account_pwd, datas[1])
            self.type(AddAccount.account_phone, datas[2])
            self.type(AddAccount.account_firstname, datas[3])
            self.type(AddAccount.account_lastname, datas[4])
            self.click(AddAccount.account_language)
            self.hover_and_click(AddAccount.account_zh_cn, AddAccount.account_zh_cn)
            self.click(AddAccount.account_timezone)
            self.hover_and_click(AddAccount.account_timezone,AddAccount.account_time)
            self.click(AddAccount.click_submit)
            self.wait_for_element(AddAccount.alert)
        with allure.step('输入错误邮箱后,断言系统提示邮箱为必填项,请填写'):
            self.assert_element_visible(AddAccount.alert)



    @parameterized.expand([[('qq200')],
                           [('time')],
                           [('try')],
                           [('sb')],
                           [('1')],
                           [('123')]])
    @allure.title('创建子账户失败,密码不足6位')
    def test_add_account03(self, datas):
        with allure.step('输入用户邮箱密码,点击登录'):
            self.wait_for_element(EleLogin.email)
            self.type(EleLogin.email, 'public@mail2.dev.fs77.net')
            self.type(EleLogin.password, 'qq2000')
            self.click(EleLogin.login_button)
        with allure.step('点击账户,点击子账户,点击添加,输入错误邮箱格式+所有必填正确信息,点击确定'):
            self.wait_for_element(AddAccount.account)
            self.click(AddAccount.account)
            self.click_link_text('子账户')
            self.click(AddAccount.account_add)
            self.type(AddAccount.account_email, '12345@qq.com')
        with allure.step(f'输入测试数据: 子账户不足6位字符的密码:{datas[0]}'):
            self.type(AddAccount.account_pwd, datas[0])
            self.type(AddAccount.account_phone, '1')
            self.type(AddAccount.account_firstname,'1')
            self.type(AddAccount.account_lastname,'1')
            self.click(AddAccount.account_language)
            self.hover_and_click(AddAccount.account_zh_cn, AddAccount.account_zh_cn)
            self.click(AddAccount.account_timezone)
            self.hover_and_click(AddAccount.account_timezone,AddAccount.account_time)
            self.click(AddAccount.click_submit)
            self.wait_for_element(AddAccount.alert2)
        with allure.step('输入密码不足6位字符后,断言系统提示密码为必填项,请填写'):
            self.assert_element_visible(AddAccount.alert2)



    @parameterized.expand([[('cba@qq.com', 'qq2000', '你好')],
                           [('yyl@qq.com', 'qq2000', '测试')],
                           [('17171@qq.com', '123456', '测试666')],
                           [('72772@qq.com', '654321', 'hello')],
                           [('ewrwerwe@qq.com', '789654', '早晨')],
                           [('rhtr@qq.com', '789123', '晚安')]])
    @allure.title('创建子账户成功(填写备注信息)')
    def test_add_account04(self, datas):
        with allure.step('输入用户邮箱密码,点击登录'):
            self.wait_for_element(EleLogin.email)
            self.type(EleLogin.email, 'otto@mail2.dev.fs77.net')
            self.type(EleLogin.password, 'qq2000')
            self.click(EleLogin.login_button)
        with allure.step('点击账户,点击子账户,点击添加,输入正确邮箱格式+所有必填正确信息,点击确定'):
            self.wait_for_element(AddAccount.account)
            self.click(AddAccount.account)
            self.click_link_text('子账户')
            self.click(AddAccount.account_add)
        with allure.step(f'输入测试数据: 子账户邮箱:{datas[0]}, 子账户密码:{datas[1]}'):
            self.type(AddAccount.account_email, datas[0])
            self.type(AddAccount.account_pwd, datas[1])
            self.type(AddAccount.account_phone, '1')
            self.type(AddAccount.account_firstname,'1')
            self.type(AddAccount.account_lastname,'1')
            self.click(AddAccount.account_language)
            self.hover_and_click(AddAccount.account_zh_cn, AddAccount.account_zh_cn)
            self.click(AddAccount.account_timezone)
            self.hover_and_click(AddAccount.account_timezone,AddAccount.account_time)
        with allure.step(f'输入测试数据: 子账户备注信息:{datas[2]}'):
            self.type(AddAccount.account_notes, datas[2])
        with allure.step('断言创建子账户备注信息和页面元素中一致'):
            self.assert_text(datas[2], AddAccount.account_notes)
            self.click(AddAccount.click_submit)


