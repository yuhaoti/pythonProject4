# @Author  yuhaotian
# @date  2023/7/11 20:13
# @version  1.0


from libs.login import Login
from common.baseAPI import BaseApi
class Del(BaseApi):
    pass



if __name__ == '__main__':
    test_data = {
        'username': 'ct0958',
        'password': '14443'
    }
    token = Login().login(test_data)
    # data = {'Host':'<calculated when request is sent>',
    #         'User-Agent':'PostmanRuntime/7.32.3',
    #         'Accept':'*/*',
    #         'Accept-Encoding':'gzip, deflate, br',
    #         'Connection':'keep-alive',
    #
    # }
    # data = {'id':'48837'}
    resp = Del(token).del_food()
    print(resp)
