# @Author  yuhaotian
# @date  2023/7/11 16:27
# @version  1.0

from libs.login import Login
from common.baseAPI import BaseApi
class Food(BaseApi):
    pass




if __name__ == '__main__':
    test_data = {
        'username': 'ct0958',
        'password': '14443'
    }
    token = Login().login(test_data)
    data = {'name': '%E5%B7%A7%E4%B9%90%E5%85%B9',
            'idShop':'3269',
            'category_id':'6705',
            'attributesJson':'[%22%E6%96%B0%22]',
            'specsJson': '[%7B%22specs%22:%22%E9%BB%98%E8%AE%A4%22,%22packing_fee%22:0,%22price%22:20%7D'
            }
    resp = Food(token).food(data)
    print(resp)