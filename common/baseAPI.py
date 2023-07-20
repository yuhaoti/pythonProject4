

import requests
import inspect
from utils.hand_yaml import get_yaml_data
from configs import config
from utils.handle_loguru import log


class BaseApi:
    def __init__(self,in_token=False):
        if in_token:
            self.header = {'Authorization':in_token}
        else:
            self.header = None
        self.data = get_yaml_data()[self.__class__.__name__]

    def send_method(self,data=None,params=None,files=None,id=''):
        apidata = self.data[inspect.stack()[1][3]]
        resp = requests.request(apidata['method'],
                        url=f"{config.HOST}{apidata['path']}{id}",
                        data=data,params = params,
                        files=files,
                        headers=self.header)
        log_msg = f'''模块名:{self.__class__.__name__},接口名:{inspect.stack()[1][3]}
    请求的url:{resp.request.url}
    请求方法:{resp.request.method}
    请求体:{resp.request.body}
    响应体:{resp.json()}'''
        log.info(log_msg)

        return resp.json()

    def query(self,data):
        res = self.send_method(params=data)
        return res

    def food(self,data):
        res = self.send_method(params=data)
        return res


    def update(self,data):
        res = self.send_method(params=data)
        return res

    def del_food(self):
        res = self.send_method()
        return res


    def file_upload(self,file_path:str):
#         1.获取文件名
        file_name = file_path.split('/')[-1]
#         2.文件类型
        file_type = file_name.split('.')[-1]
        file = {'file':(file_name,open(file_path,'rb'),file_type)}
        return self.send_method(files=file)


# if __name__ == '__main__':
#     pass
    # test_data = {
    #     'username' : 'ct0958',
    #     'password' : '14443'
    # }
    # from utils.hand_data加密_md5 import get_md5_data
    # test_data['password'] = get_md5_data(test_data['password'])
    # payload = test_data
    # res = BaseApi().send_method(data=payload)
    # print(res)
