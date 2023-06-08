import os

from selenium.webdriver.common.by import By
import pytest
import sbase
from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)
class LoadProxy(BaseCase):
    def test_load_proxy(self):
        self.open("https://dashboard.zzdb.cc")
        self.maximize_window()
        self.type('#name','otto@mail2.dev.fs77.net')
        self.type('#password','qq2000')
        self.click('//*[@id="formLogin"]/div[3]/div/div/span/button/span')
        self.click('//*[@id="app"]/section/aside/div/ul/li[4]/div/span/span')
        self.wait_for_element('//*[@id="app"]/section/aside/div/ul/li[4]/div/span/span')
        self.click_link('子账户')
        self.type('input[placeholder="邮箱"]','136')
        self.click('#app > section > section > main > div > div > div > div.ant-pro-grid-content > div > div > div > div.table-page-search-wrapper > form > div > div:nth-child(2) > button > span')
        self.click('//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/div/div[2]/a/button/span')
        self.type('#email','123456')
        self.type('#pass', '123456')
        self.type('#phone', '123456')
        self.type('#firstName', '1')
        self.type('#lastName', '1')
        self.click('//*[@id="localeName"]/div/div/div[contains(@style, "block")]')
        self.click('//li[text()="简体中文"]')
        self.click('//*[@id="timezoneName"]/div/div/div[@style="display: block; user-select: none;"]')
        self.click('//ul[@role="listbox"]/li[@role="option"][5]')
        self.type('//input[@id="remarks"]','测试')
        self.click('//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/div/div/div/form/div[8]/div/div/span/button/span')
        self.wait(3)

