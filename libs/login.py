# @Author  yuhaotian
# @date  2023/7/6 8:52
# @version  1.0
# from utils.hand_data加密_md5 import get_md5_data
# from common.baseAPI import BaseApi
# class Login(BaseApi):
#     def login(self,test_data):
#         # test_data = {
#         #     'username': 'ct0958',
#         #     'password': '14443'
#         # }
#         test_data['password'] = get_md5_data(test_data['password'])
#         payload = test_data
#         res = self.send_method(payload)
#         return res

# if __name__ == '__main__':
#     res1 = Login().login()
#     print(res1)


from utils.hand_data加密_md5 import get_md5_data
from common.baseAPI import BaseApi
class Login(BaseApi):
    def login(self,test_data,token_name=False):
        test_data['password'] = get_md5_data(test_data['password'])
        payload = test_data
        res = self.send_method(payload)
        if token_name:
            return res
        else:
            return res['data']['token']


if __name__ == '__main__':
    res1 = Login().login({
            'username': 'ct0958',
            'password': '14443'
        })
    print(res1)