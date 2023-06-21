class AddAccount:
    account = '//div/ul[@role="menu"]/li[4]/div/span/span/span[text()="账户"]'
    link = '//ul/li/a/span[text()="子账户"]'
    account_add  = '//main/div/div/div/div[2]/div/div/div/div[2]/a[@href="/setting/subAccountMgr/add"]/button'
    account_email = '#email'
    account_pwd = '#pass'
    account_phone = '#phone'
    account_firstname = '#firstName'
    account_lastname = '#lastName'
    account_language = '#localeName'
    account_zh_cn = '//div/ul[@role="listbox"]/li[1][text()="简体中文"]'
    account_timezone = '#timezoneName'
    account_time = '//div[@tabindex="-1"]/ul[@role="listbox"]/li[4][text()="UTC -09:00"]'
    click_submit = '//div/span/button/span[text()="确 定"]'
    account_notes = '#remarks'

    #邮箱格式错误
    alert = '//div/div/div/div[text()="必填项，请填写"]'
    #密码不足6位
    alert2 = '//div/div/div/div[text()="至少6位密码，区分大小写"]'