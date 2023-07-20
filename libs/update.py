# @Author  yuhaotian
# @date  2023/7/11 16:51
# @version  1.0
from libs.login import Login
from common.baseAPI import BaseApi

class Update(BaseApi):
    pass
from libs.shop import Shop
if __name__ == '__main__':
    test_data = {
        'username': 'ct0958',
        'password': '14443'
    }
    token = Login().login(test_data)
    data = {'name':'1111',
            'id':'48850',
            'idMenu':'94484',
            'idShop':'15218',
            'specsJson':'[{"specs":" 默 认","packing_fee":0,"price":20}]'
    }
    resp = Update(token).update(data)
    print(resp)









