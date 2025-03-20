import random

"""
0001. 生成随机激活码：
    1. 生成一个长度为10的随机字符串，字符串由字母和数字组成
    2. 生成200个去重后的激活码

"""

def gen_random_str(lenth):
    str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    random_code =  random.choices(str, k=lenth)
    random_code_str = ''.join(random_code)
    return random_code_str

def gen_code_list(code_num=200):
    code_list = []
    for i in range(code_num):
        activation_code = gen_random_str(16)
        code_list.append(activation_code)
    code_list = list(set(code_list))
    return code_list


if __name__ == '__main__':
    s_list = []
    for i in range(200):
        a = gen_random_str(10)
        s_list.append(a)
        s_list = list(set(s_list))


    print(s_list)
