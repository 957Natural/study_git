import random
import string
from time import sleep


def read_random():
    random_list = [random.randint(1, 100)]
    random_list2 = []
    random_list3 = []
    for i in random_list:
        o = str(i)
        o += '@mail2.dev.fs77.net'
        random_list2.append(o)
        random_list2.append('qq2000')
        random_list3.append(random_list2)
    return random_list3


def generate_random_code(length):
    datas = []
    datas2 = []
    all_chars = string.ascii_letters + string.digits
    code = ''.join(random.choices(all_chars, k=length))
    code += '@mail2.dev.fs77.net'
    datas.append(code)
    datas.append('qq2000')
    datas.append('user@mail2.dev.fs77.net')
    datas.append('kD%4Pi3EtAdbvF')
    datas2.append(datas)
    return datas2

# 创建角色成功
def add_role_random(length):
    datas = ['public@mail2.dev.fs77.net', 'qq2000']
    datas2 = []
    all_chars = string.ascii_letters + string.digits
    code = ''.join(random.choices(all_chars, k=length))
    code2 = ''.join(random.choices(all_chars, k=length))
    code3 = ''.join(random.choices(all_chars, k=length))
    code3 += '@mail2.dev.fs77.net'
    datas.append(code)
    datas.append(code2)
    datas.append(code3)
    datas.append(str(random.randint(1, 10)))
    datas.append(str(random.randint(1, 10)))
    datas.append(str(random.randint(1, 10)))
    datas2.append(datas)
    return datas2


# 创建子账户成功
def add_account_success_random(length):
    datas = []
    all_chars = string.ascii_letters + string.digits
    code = ''.join(random.choices(all_chars, k=length))
    code8 = ''.join(random.choices(all_chars, k=length))
    code8 += '.net'
    code += f'@{code8}'
    code2 = ''.join(random.choices(all_chars, k=6))
    code3 = ''.join(random.choices(all_chars, k=length))
    code4 = ''.join(random.choices(all_chars, k=length))
    code5 = ''.join(random.choices(all_chars, k=length))
    datas.append(code)
    datas.append(code2)
    datas.append(code3)
    datas.append(code4)
    datas.append(code5)
    datas2 = [datas]
    return datas2

# 创建子账户失败(邮箱格式错误)
def add_account_false_ramdom(length):
    datas = []
    all_chars = string.ascii_letters + string.digits
    code = ''.join(random.choices(all_chars, k=length))
    code2 = ''.join(random.choices(all_chars, k=length))
    code3 = ''.join(random.choices(all_chars, k=length))
    code4 = ''.join(random.choices(all_chars, k=length))
    code5 = ''.join(random.choices(all_chars, k=6))
    datas.append(code)
    datas.append(code5)
    datas.append(code2)
    datas.append(code3)
    datas.append(code4)
    datas2 = [datas]
    return datas2

# 登录失败(邮箱格式错误)
def login_false(length):
    datas = []
    all_chars = string.ascii_letters + string.digits
    code = ''.join(random.choices(all_chars, k=length))
    datas.append(code)
    datas.append('qq2000')
    datas2 = [datas]
    return datas2
# 登录失败(密码不足6位字符)
def login_false2(length):
    datas = ['cypher@mail2.dev.fs77.net']
    all_chars = string.ascii_letters + string.digits
    code = ''.join(random.choices(all_chars, k=length))
    datas.append(code)
    datas2 = [datas]
    return datas2

# 复杂场景if条件判断
def isElementExist(self, element):
    flag = True
    try:
        self.driver.find_element(element)
        return flag
    except:
        flag = False
        return flag




