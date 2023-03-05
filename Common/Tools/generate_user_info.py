from Common.Tools.generate_address import generate_address
from Common.Tools.generate_id_number import generate_id_number
from Common.Tools.generate_name import generate_name
from Common.Tools.generate_phone_number import generate_phone_number


def generate_user_info():
    id_num = generate_id_number()
    info_dic = {"身份证号": id_num}
    sex = ''
    if int(id_num[14:-1]) % 2 == 0:
        sex = '女'
    else:
        sex = '男'
    info_dic['性别'] = sex
    info_dic['手机号'] = generate_phone_number()
    info_dic['地址'] = generate_address(id_num)
    info_dic['姓名'] = generate_name()
    return info_dic

print(generate_user_info())
