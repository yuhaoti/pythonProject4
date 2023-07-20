# @Author  yuhaotian
# @date  2023/7/5 14:58
# @version  1.0
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS_cipher
class Rsa_Encrypt:
    def __init__(self,filepath='./'):
        self.filepath = filepath


    def Encrypt(self,data):  #加密公钥
        with open(self.filepath+'public_pemll','rb') as op:
            public_content = op.read()   #读取文件
            publickey = RSA.importKey(public_content)   #获取密钥文本
            cipher = PKCS_cipher.new(publickey)     #将密钥实例化
            cipher_text = cipher.encrypt(data.encode('utf-8'))   #利用获取到得密钥进行加密因为只能是字节串所以用encode加密
            return base64.b64encode(cipher_text).decode()      #用base64再进行加密再利用decode转化成字符串格式
    def rsa_decrypt(self,text):  #解密私钥
        with open(self.filepath+'public_jiemi','rb') as op:
            private_key = op.read()   #读取文件
            cipher = PKCS_cipher.new(RSA.importKey(private_key))  #获取cipher实例对象
            retval = cipher.decrypt(base64.b64decode(text), 'ERROR').decode('utf-8')  #解密，解密不成功返回ERROR
            return retval

if __name__ == '__main__':
    res = Rsa_Encrypt().Encrypt('123456')
    print(res)
    print('-------------')
    res1 = Rsa_Encrypt().rsa_decrypt(res)
    print('-----------')
    print(res1)





# def rsa_decrypt(text):
#     """校验RSA加密 使用私钥进行解密"""
#     cipher = PKCS_cipher.new(RSA.importKey(private_key))
#     retval = cipher.decrypt(base64.b64decode(text), 'ERROR').decode('utf-8')
#     return retval
#
# res1 = rsa_decrypt('ml0SZgGMr3ViO5nScgy6jJJPFTU0TkrWXvm/+Lla1Nl4xqv3NSMu'
#                    'srYwq9e+PauSnf6Dfn0pVHE67TvT95mxL6WOcwKfa2bdRx3E'
#                    '46tVepVSyAhMBhQ+PjsCAX5+BkwAeracwlsx1+2dfoblb+ZEgCX0z61Jfka1Kq2f/5SLEBw=')
#
# print(res1)