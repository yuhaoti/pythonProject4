# @Author  yuhaotian
# @date  2023/7/12 15:06
# @version  1.0
from libs.shop import Shop
from libs.login import Login
import pytest
from configs.config import NAME_PWD
@pytest.fixture(scope='session')
def start_running():
    print('-------项目开始测试-------')

@pytest.fixture(scope='session')
def login_init():
    print('-----开始登录-----')
    token = Login().login(NAME_PWD)
    yield token
    print('------登录结束--------')

@pytest.fixture(scope='session')
def shop_init(login_init):
    shop = Shop(login_init)
    yield shop

@pytest.fixture(scope='class')
def update_shop_init(shop_init):
    shop_id = shop_init.query({'page':1,'limit':20})['data']['records'][0]['id']
    image_info = shop_init.file_upload('../data/123.png')['data']['realFileName']
    updata_shop_obj = {'shop_init':shop_init,'shop_id':shop_id,'image_info':image_info}
    yield updata_shop_obj


'''
在使用pytest.mark.parametrize  对用例进行参数化的时候，传入的值包含中文，运行用例，控制台显示编码问题
解决方法：在用例的根目录下，新建conftest.py文件，将下面的代码复制进去
'''
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")









