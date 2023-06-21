
import allure
from seleniumbase import BaseCase
from utils.ele_login import *
from parameterized import parameterized
from utils.read_random import *
from Page.add_role_elements import *
from Page.add_account_elements import *


@allure.feature('Loadproxy用户测试')
@allure.story('用户创建角色模块')
class AddRoleGroup(BaseCase):
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


    @parameterized.expand([add_role_random(7),
                           add_role_random(10),
                           add_role_random(12),
                           add_role_random(15),
                           add_role_random02(6),
                           add_role_random02(4),
                           add_role_random02(20),
                           add_role_random02(11),
                           add_role_random02(13),
                           add_role_random02(9)])
    @allure.title('用户创建角色并使用搜索功能验证新创建的角色已存在')
    def test_add_role(self, datas):
        with allure.step(f'输入用户邮箱:{datas[0]}, 输入用户密码:{datas[1]}'):
            self.wait_for_element(EleLogin.email)
            self.type(EleLogin.email, datas[0])
            self.assert_text(datas[0], EleLogin.email)
            self.type(EleLogin.password, datas[1])
            self.assert_text(datas[1], EleLogin.password)
        with allure.step('点击登录'):
            self.click(EleLogin.login_button)
            self.wait_for_element_visible(AddRole.role_click)
            self.click(AddRole.role_click)
            self.wait_for_element(AddRole.role_role_group)
        with allure.step('点击账户,点击角色组,点击添加'):
            self.hover_and_click(AddRole.role_role_group, AddRole.role_role_group)
            self.hover_and_click(AddRole.role_add, AddRole.role_add)
        with allure.step(f'输入新添加角色的名字:{datas[2]}, 以及描述:{datas[3]}'):
            self.type(AddRole.role_name, datas[2])
            self.assert_text(datas[2], AddRole.role_name)
            self.type(AddRole.role_describe, datas[3])
            self.assert_text(datas[3], AddRole.role_describe)
        with allure.step('点击确定'):
            self.click(AddRole.role_submit)
            self.wait_for_element(AddRole.role_assert_alert)
        with allure.step('点击确定后,断言添加成功弹框元素已存在可见'):
            self.assert_element_visible(AddRole.role_assert_alert)
            self.hover_and_click(AddRole.role_role_group, AddRole.role_role_group)
        with allure.step(f'选择搜索框,名字搜索框输入:{datas[2]}'):
            self.type(AddRole.role_select_name, datas[2])
            self.assert_text(datas[2], AddRole.role_select_name)
        with allure.step(f'点击搜索按钮并断言搜索到的角色名字信息和{datas[2]}一致'):
            self.hover_and_click(AddRole.role_select_button, AddRole.role_select_button)
            self.wait_for_element(f'//div/div/div/div[2]/div/div/div/div[3]/div/div/div/div/div/table/tbody/tr/td[1][text()="{datas[2]}"]')
            self.assert_text(datas[2], f'//div/div/div/div[2]/div/div/div/div[3]/div/div/div/div/div/table/tbody/tr/td[1][text()="{datas[2]}"]')
        with allure.step('断言成功后将添加的角色删除,清空测试数据'):
            self.hover_and_click(AddRoleResources.role_delete, AddRoleResources.role_delete)
            self.wait_for_link_text_visible(AddRoleResources.role_clear_datas)
            self.hover_and_click(AddRoleResources.role_clear_datas, AddRoleResources.role_clear_datas)
        with allure.step('断言测试数据已清空'):
            self.wait_for_element_visible(AddRoleResources.role_clear_assert)
            self.assert_element_visible(AddRoleResources.role_clear_assert)


    @parameterized.expand([add_role_random(8),
                           add_role_random(5),
                           add_role_random(12),
                           add_role_random(13),
                           add_role_random(6),
                           add_role_random(9),
                           add_role_random(15),
                           add_role_random(7),
                           add_role_random(19),
                           add_role_random(5)])
    @allure.title('用户创建角色并验证创建成功后删除该角色成功')
    def test_add_role02(self, datas):
        with allure.step(f'输入用户邮箱:{datas[0]}, 输入用户密码:{datas[1]}'):
            self.wait_for_element(EleLogin.email)
            self.type(EleLogin.email, datas[0])
            self.assert_text(datas[0], EleLogin.email)
            self.type(EleLogin.password, datas[1])
            self.assert_text(datas[1], EleLogin.password)
        with allure.step('点击登录'):
            self.click(EleLogin.login_button)
            self.wait_for_element_visible(AddRole.role_click)
            self.click(AddRole.role_click)
        with allure.step('点击账户,点击角色组,点击添加'):
            self.wait_for_element(AddRole.role_role_group)
            self.hover_and_click(AddRole.role_role_group, AddRole.role_role_group)
            self.hover_and_click(AddRole.role_add, AddRole.role_add)
        with allure.step(f'输入新添加角色的名字:{datas[2]}, 以及描述:{datas[3]}'):
            self.type(AddRole.role_name, datas[2])
            self.assert_text(datas[2], AddRole.role_name)
            self.type(AddRole.role_describe, datas[3])
            self.assert_text(datas[3], AddRole.role_describe)
        with allure.step('点击确定'):
            self.click(AddRole.role_submit)
            self.wait_for_element(AddRole.role_assert_alert)
        with allure.step('点击确定后,断言添加成功弹框元素已存在可见'):
            self.assert_element_visible(AddRole.role_assert_alert)
            self.hover_and_click(AddRole.role_role_group, AddRole.role_role_group)
        with allure.step(f'选择搜索框,名字搜索框输入:{datas[2]}'):
            self.type(AddRole.role_select_name, datas[2])
            self.assert_text(datas[2], AddRole.role_select_name)
            self.hover_and_click(AddRole.role_select_button, AddRole.role_select_button)
        with allure.step(f'断言搜索到的角色名字信息和{datas[2]}一致'):
            self.wait_for_element(f'//div[@class="ant-table-wrapper"]/div/div/div/div/div[@class="ant-table-body"]/table/tbody/tr/td[1][text()="{datas[2]}"]')
            self.assert_text(datas[2], f'//div[@class="ant-table-wrapper"]/div/div/div/div/div[@class="ant-table-body"]/table/tbody/tr/td[1][text()="{datas[2]}"]')
        with allure.step('点击搜索按钮'):
            self.hover_and_click(AddRole.role_select_button, AddRole.role_select_button)
            self.wait_for_element(AddRole.rele_delect)
            self.hover_and_click(AddRole.rele_delect, AddRole.rele_delect)
            self.wait_for_element(AddRole.role_submit_alert)
        with allure.step('点击搜索到的角色右侧的删除按钮,等待弹框出现继续点击确定按钮'):
            self.assert_element_visible(AddRole.role_submit_alert)
            self.hover(AddRole.role_submit_alert)
            self.wait_for_element(AddRole.role_submit2)
        with allure.step('点击删除后,等待弹框出现后点击确定删除'):
            self.assert_element_visible(AddRole.role_submit2)
            self.hover_and_click(AddRole.role_submit2, AddRole.role_submit2)
            self.wait_for_element(AddRole.role_assert_alert2)
        with allure.step('断言删除角色后系统提示成功弹框元素存在可见'):
            self.assert_element_visible(AddRole.role_assert_alert2)

    @parameterized.expand([add_role_random02(7),
                           add_role_random02(6),
                           add_role_random02(12),
                           add_role_random02(16),
                           add_role_random02(4),
                           add_role_random02(11),
                           add_role_random02(13),
                           add_role_random02(8),
                           add_role_random02(5),
                           add_role_random02(4),
                           add_role_random02(10),
                           add_role_random02(9),
                           add_role_random02(18),
                           add_role_random02(19)])
    @allure.title('用户创建角色为角色添加所有资源后使用子账户添加角色并登录后可以使用用户的所有功能')
    def test_add_role03(self, datas):
        with allure.step(f'输入用户邮箱:{datas[0]}, 输入用户密码:{datas[1]}'):
            self.wait_for_element(EleLogin.email)
            self.type(EleLogin.email, datas[0])
            self.assert_text(datas[0], EleLogin.email)
            self.type(EleLogin.password, datas[1])
            self.assert_text(datas[1], EleLogin.password)
        with allure.step('点击登录'):
            self.click(EleLogin.login_button)
            self.wait_for_element_visible(AddRole.role_click)
            self.click(AddRole.role_click)
            self.wait_for_element(AddRole.role_role_group)
        with allure.step('点击账户,点击角色组,点击添加'):
            self.hover_and_click(AddRole.role_role_group, AddRole.role_role_group)
            self.hover_and_click(AddRole.role_add, AddRole.role_add)
        with allure.step(f'输入新添加角色的名字:{datas[2]}, 以及描述:{datas[3]}'):
            self.wait_for_element_visible(AddRole.role_name)
            self.type(AddRole.role_name, datas[2])
            self.assert_text(datas[2], AddRole.role_name)
            self.type(AddRole.role_describe, datas[3])
            self.assert_text(datas[3], AddRole.role_describe)
        with allure.step('点击确定'):
            self.click(AddRole.role_submit)
            self.wait_for_element(AddRole.role_assert_alert)
        with allure.step('点击确定后,断言添加成功弹框元素已存在可见'):
            self.assert_element_visible(AddRole.role_assert_alert)
            self.hover_and_click(AddRole.role_role_group, AddRole.role_role_group)
        with allure.step(f'选择搜索框,名字搜索框输入:{datas[2]}'):
            self.clear(AddRole.role_select_name)
            self.type(AddRole.role_select_name, datas[2])
            self.assert_text(datas[2], AddRole.role_select_name)
        with allure.step('点击搜索按钮'):
            self.hover_and_click(AddRole.role_select_button, AddRole.role_select_button)
            self.wait_for_element(AddRoleResources.role_click_message)
        with allure.step('点击新添加角色的资源,点击全选,点击确定'):
            self.hover_and_click(AddRoleResources.role_click_message, AddRoleResources.role_click_message)
            self.wait_for_element(AddRoleResources.role_resources_select_all)
            self.hover_and_click(AddRoleResources.role_resources_select_all, AddRoleResources.role_resources_select_all)
            self.click(AddRoleResources.role_resources_submit)
            self.wait_for_element(AddRoleResources.role_resources_assert)
        with allure.step('新角色绑定资源后系统提示绑定成功,断言该弹框已存在可见'):
            self.assert_text('绑定成功', AddRoleResources.role_resources_assert)
            self.assert_element_visible(AddRoleResources.role_resources_assert)

        with allure.step('点击子账户,点击添加,输入所有必填正确信息,点击确定'):
            self.click_link_text('子账户')
            self.click(AddAccount.account_add)
        with allure.step(f'输入测试数据: 子账户邮箱:{datas[4]}, 子账户密码:{datas[1]}, 子账户电话:{datas[5]},'
                         f'子账户姓:{datas[6]}, 子账户名:{datas[7]}'):
            self.type(AddAccount.account_email, datas[4])
            self.assert_text(datas[4], AddAccount.account_email)
            self.type(AddAccount.account_pwd, datas[1])
            self.assert_text(datas[1], AddAccount.account_pwd)
            self.type(AddAccount.account_phone, datas[5])
            self.assert_text(datas[5], AddAccount.account_phone)
            self.type(AddAccount.account_firstname, datas[6])
            self.assert_text(datas[6], AddAccount.account_firstname)
            self.type(AddAccount.account_lastname, datas[7])
            self.assert_text(datas[7], AddAccount.account_lastname)
        with allure.step(f'选择子账户语言,选择子账户时区,点击确定'):
            self.click(AddAccount.account_language)
            self.hover_and_click(AddAccount.account_zh_cn, AddAccount.account_zh_cn)
            self.click(AddAccount.account_timezone)
            self.wait_for_element_visible(AddAccount.account_time)
            self.hover_and_click(AddAccount.account_time, AddAccount.account_time)
            self.click(AddAccount.click_submit)
            self.wait_for_element(AddRoleResources.role_resources_account_assert)
            self.assert_element_visible(AddRoleResources.role_resources_account_assert)
        with allure.step('添加子账户后, 选择子账户添加角色'):
            self.click_link_text('子账户')
            self.type(AddRoleResources.role_account_select, datas[4])
            self.hover_and_click(AddRoleResources.role_select_submit, AddRoleResources.role_select_submit)
            self.wait_for_element(AddRoleResources.role_account_add_role)
        with allure.step('选择需要添加角色的子账户,点击角色,选择需要添加的角色'):
            self.hover_and_click(AddRoleResources.role_account_add_role, AddRoleResources.role_account_add_role)
            self.wait_for_element(AddRoleResources.role_click_input)
            self.click(AddRoleResources.role_click_input)
        with allure.step(f'选择角色的名字:{datas[2]}, 点击添加'):
            self.wait_for_element(f'//div/div/ul[@role="listbox"]/li[text()="{datas[2]}"]')
            self.hover_and_click(f'//div/div/ul[@role="listbox"]/li[text()="{datas[2]}"]',
                                 f'//div/div/ul[@role="listbox"]/li[text()="{datas[2]}"]')
            self.hover_and_click(AddRoleResources.role_click_alert, AddRoleResources.role_click_alert)
            self.wait_for_element(AddRoleResources.role_account_submit)
            self.hover_and_click(AddRoleResources.role_account_submit, AddRoleResources.role_account_submit)
            self.wait_for_element(AddRoleResources.role_assert_success)
        with allure.step('添加角色成功后,系统提示绑定成功,断言该弹框已存在可见'):
            self.assert_element_visible(AddRoleResources.role_assert_success)
            self.hover_and_click(AddRoleResources.role_account_back, AddRoleResources.role_account_back)

        with allure.step('移动到退出登录'):
            self.wait_for_element(
                f'//div[@id="app"]/section/section/div/header[2]/div[@class="ant-pro-global-header"]/div/span/span[2][text()="{datas[0]}"]')
            self.hover_on_element(
                f'//div[@id="app"]/section/section/div/header[2]/div[@class="ant-pro-global-header"]/div/span/span[2][text()="{datas[0]}"]')
        with allure.step('点击退出登录'):
            self.wait_for_element_visible(AddRole.role_logout)
            self.hover_and_click(AddRole.role_logout, AddRole.role_logout)
            self.wait_for_element_visible(EleLogout.logout_button)
            self.hover_and_click(EleLogout.logout_button, EleLogout.logout_button)
        with allure.step(f'退出到登录界面后,输入添加了角色的子账户邮箱:{datas[4]}, 密码:{datas[1]},点击登录'):
            self.wait_for_element_visible(EleLogin.email)
            self.type(EleLogin.email, datas[4])
            self.assert_text(datas[4], EleLogin.email)
            self.type(EleLogin.password, datas[1])
            self.assert_text(datas[1], EleLogin.password)
            self.click(EleLogin.login_button)
        with allure.step('验证子账户绑定了添加所有资源的角色后.登录可以正常使用左侧用户的所有功能'):
            self.wait_for_element(AddRoleResources.role_resources_assert_function1)
            self.click(AddRoleResources.role_resources_assert_function1)
            self.wait_for_element(AddRoleResources.role_resources_assert_function2)
            self.click(AddRoleResources.role_resources_assert_function2)
            self.wait_for_element(AddRoleResources.role_resources_assert_function3)
            self.click(AddRoleResources.role_resources_assert_function3)
            self.wait_for_element(
            f'//div[@id="app"]/section/section/div/header[2]/div[@class="ant-pro-global-header"]/div/span/span[2][text()="{datas[4]}"]')
            self.hover_on_element(
            f'//div[@id="app"]/section/section/div/header[2]/div[@class="ant-pro-global-header"]/div/span/span[2][text()="{datas[4]}"]')
        with allure.step('点击退出登录'):
            self.wait_for_element_visible(EleLogout.wait_logout)
            self.hover_and_click(EleLogout.wait_logout, EleLogout.wait_logout)
            self.wait_for_element_visible(EleLogout.logout_button)
            self.hover_and_click(EleLogout.logout_button, EleLogout.logout_button)
            self.wait_for_element_visible(EleLogin.email)
            self.type(EleLogin.email, datas[0])
            self.type(EleLogin.password, datas[1])
            self.click_if_visible(EleLogin.login_button)
        with allure.step('点击账户,点击角色组,点击添加'):
            self.wait_for_element_visible(AddRole.role_click)
            self.click(AddRole.role_click)
            self.wait_for_element(AddRole.role_role_group)
            self.hover_and_click(AddRole.role_role_group, AddRole.role_role_group)
        with allure.step(f'选择搜索框,名字搜索框输入:{datas[2]}'):
            self.clear(AddRole.role_select_name)
            self.type(AddRole.role_select_name, datas[2])
            self.assert_text(datas[2], AddRole.role_select_name)
        with allure.step('点击搜索按钮'):
            self.hover_and_click(AddRole.role_select_button, AddRole.role_select_button)
        with allure.step('测试完成后,删除角色,清空测试数据'):
            self.wait_for_element_visible(AddRoleResources.role_delete)
            self.hover_and_click(AddRoleResources.role_delete, AddRoleResources.role_delete)
            self.wait_for_link_text_visible(AddRoleResources.role_clear_datas)
            self.hover_and_click(AddRoleResources.role_clear_datas, AddRoleResources.role_clear_datas)
            self.wait_for_element_visible(AddRoleResources.role_clear_assert)
            self.assert_element_visible(AddRoleResources.role_clear_assert)
        with allure.step('测试完成后,删除子账户,清空测试数据'):
            self.click_link_text('子账户')
            self.hover_on_element(AddRoleResources.role_delete2)
            self.type(AddRoleResources.role_delete2, datas[4])
            self.hover_and_click(AddRoleResources.role_clear_select, AddRoleResources.role_clear_select)
            self.wait_for_element_visible(AddRoleResources.role_clear_datas2)
            self.hover_and_click(AddRoleResources.role_clear_datas2, AddRoleResources.role_clear_datas2)
            self.wait_for_element_visible(AddRoleResources.role_clear_button)
            self.hover_and_click(AddRoleResources.role_clear_button, AddRoleResources.role_clear_button)







