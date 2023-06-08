from _pytest.pytester import pytester


class EleSite:
    url = 'https://dashboard.rootdevx.com'
    email = '#name'
    password = '#password'
    login_button = '//*[@id="formLogin"]/div[3]/div/div/span/button/span'
    site = '//div/span/span/span[text()="站点"]'
    site_add = '//*[@id="app"]/section/aside/div/ul/li[3]/ul/li[2]/a/span'
    taocan = '//div[@id="planId"]'
    default = '//div/ul[@role="listbox"]/li[@role="option"][text()="默认套餐 "]'
    domain_name = '#domain'
    return_address = '#originServer'
    return_address2 = '//div/form/div[5]/div[2]/div/span/textarea[@id="originServer"]'
    site_determine = '//div/span/button/span[text()="确 定"]'
    move_exit = '//section/section/div/header[2]/div/div/span[1]/span[2][text()="otto@mail2.dev.fs77.net"]'
    user_exit2 = '//div/ul/li/i[@class="anticon anticon-logout"]'
    exit_massage = '//span[text()="消息"]'
    exit_button = '/html/body/div[7]/div/div[2]/div/div[2]/div/div/div[2]/button[@class="ant-btn ant-btn-primary"]/span'
    exit_button2 = 'button.ant-btn:nth-child(2)'
    input = '//input[@placeholder="域名"]'
    site_select = '//section/section/main/div/div/div/div[2]/div/div/div/div[1]/form/div/div[2]/button/span[text()="搜索"]'
    site_xiangqing = '//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[1]'
    site_default = '//form/div/div[3]/div/div[2]/div/span/div/div/span'
    site_modify = '//div/div/div/ul/li[2][text()="测试暂停套餐 "]'
    site_yes = '//form/div[13]/div/div/span/button'
    site_faild = '//span[@class="ant-alert-message"][text()="提示！"]'

