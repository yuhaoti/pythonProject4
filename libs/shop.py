# @Author  yuhaotian
# @date  2023/7/11 14:32
# @version  1.0
from libs.login import Login
from common.baseAPI import BaseApi
class Shop(BaseApi):
    def update(self,data,new_id,image_info):
        if data['id'] != '0000':
            data['id']=new_id
        data['image_path'] = image_info
        data['image'] = f'/file/getImgStream?fileName={image_info}'
        return super(Shop,self).update(data)
#
if __name__ == '__main__':
    test_data = {
        'username': 'ct0958',
        'password': '14443'
    }
    token = Login().login(test_data)
    # 创建店铺实例
    shop = Shop(token)
#     列出店铺
    test_data = {'page':1,'limit':20}
    shop_res = shop.query(test_data)
    print('列出商铺信息---->>',shop_res)
    # 获取店铺id
    shop_id = shop_res['data']['records'][0]['id']
    print('店铺id---->',shop_id)
#   文件上传接口
    image_info= shop.file_upload('../data/123.png')
    print('列出上传图片信息--->',image_info)
    image_infos = image_info['data']['realFileName']
    print('列出图片信息---->',image_infos)
    # 店铺更新
    updata_data = {
            "name": "星巴克新建店",
            "address": "上海市静安区秣陵路303号",
            "id": "id",
            "Phone": "13176876632",
            "rating": "6.0",
            "recent_order_num": 100,
            "category": "快餐便当/简餐",
            "description": "满30减5，满60减8",
            "image_path": "b8be9abc-a85f-4b5b-ab13-52f48538f96c.png",
            "image": "http://121.41.14.39:8082/file/getImgStream?fileName=b8be9abc-a85f-4b5b-ab13-52f48538f96c.png"

    }
    resp = shop.update(updata_data,shop_id,image_infos)
    print(resp)



#     data = {'name': '%E5%A4%A7%E9%B8%AD%E6%A2%A8%E5%8D%97%E5%B1%B1%E5%BA%97222',
#             'address': '%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BE%90%E6%B1%87%E5%8C%BA%E6%B2%AA%E9%97%B5%E8%B7%AF9001%E5%8F%B7',
#             'description': '%E8%8F%9C%E5%93%81%E5%B7%B2%E6%9B%B4%E6%96%B0%EF%BC%8C%E7%96%AB%E6%83%85%E6%9C%9F%E9%97%B4%E6%B3%A8%E6%84%8F%E9%98%B2%E6%8A%A4',
#             'id': '15218',
#             'phone': '18300000957',
#             'rating':'4.5',
#             'recent_order_num':'500',
#             'category':'%E5%BF%AB%E9%A4%90%E4%BE%BF%E5%BD%93%2F%E7%AE%80%E9%A4%90',
#             'image_path':'0c51f87b-8b05-4b9e-b64e-b1a7f446ce53.jpg',
#             'image':'%2Ffile%2FgetImgStream%3FfileName%3D0c51f87b-8b05-4b9e-b64e-b1a7f446ce53.jpg'
#             }
#     resp = Shop(token).update(data,'15218','../data/123.png')
#     print(resp)

    # def addshop(self):
    #     test_data = {
    #         'page':1,
    #         'limit':20
    #     }
    #
    #     header = {}
    # def file_(self):

#
# if __name__ == '__main__':
#     test_data = {
#         'username': 'ct0958',
#         'password': '14443'
#     }
#     token = Login().login(test_data)
#     data = {'page':1,
#             'limit':20
#     }
#     resp = Shop(token).query(data)
#     res1 = str(resp['data']['records'][-1]['item_id'])
#
#     print(resp)
#     print(res1)




# if __name__ == '__main__':
#     test_data = {
#         'username': 'ct0958',
#         'password': '14443'
#     }
#     token = Login().login(test_data)
#
#
#     resp = Shop(token)
#     res2 = resp.file_upload('../data/123.png')
#     print('=======',res2)


    # print(resp)
    # print(res1)





