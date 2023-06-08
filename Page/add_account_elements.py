class AddAccount:
    account = '//div/span/span/span[text()="账户"]'
    link = '//ul/li/a/span[text()="子账户"]'
    account_add  = '//div/a/button/span[text()="添加"]'
    account_email = '#email'
    account_pwd = '#pass'
    account_phone = '#phone'
    account_firstname = '#firstName'
    account_lastname = '#lastName'
    account_language = '//div[@role="combobox"]/div/div[text()="语言"]'
    account_zh_cn = '//div/ul[@role="listbox"]/li[text()="简体中文"]'
    account_timezone = '//div[@role="combobox"]/div/div[text()="时区"]'
    account_time = '//div[@tabindex="-1"]/ul[@role="listbox"]/li[text()="UTC -09:00"]'
    click_submit = '//div/span/button/span[text()="确 定"]'
    account_notes = '#remarks'

    #邮箱格式错误
    alert = '//div/div/div/div[text()="必填项，请填写"]'
    #密码不足6位
    alert2 = '//div/div/div/div[text()="至少6位密码，区分大小写"]'