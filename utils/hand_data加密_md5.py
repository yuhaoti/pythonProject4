# @Author  yuhaotian
# @date  2023/7/4 16:34
# @version  1.0

import hashlib

def get_md5_data(pwd:str,salt=""):
    md5 = hashlib.md5()    #获取MD5对象
    pwd = pwd+salt
    md5.update(pwd.encode('utf-8'))   #将密码转换成字节串
    return md5.hexdigest()  #md5得16进制返回


# if __name__ == '__main__':
#     print(get_md5_data('123456','mm'))






