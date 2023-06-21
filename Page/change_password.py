class ChangePassword:
    click_account = '//div/span/span/span[text()="账户"]'
    change_password = '//section/aside/div/ul/li[4]/ul/li[4]/a/span[text()="修改密码"]'
    original = '//input[@placeholder="原密码"]'
    new_password = '//input[@placeholder="至少6位密码，区分大小写"]'
    confirm_password = '//input[@placeholder="确认密码"]'
    submit = '//div[@class="ant-row"]/div/form/div[5]/div/div/span/button'
    password_alert = '//div[@data-show="true"]/span[text()="修改成功"]'
