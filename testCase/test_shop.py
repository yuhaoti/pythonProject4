# @Author  yuhaotian
# @date  2023/7/12 14:27
# @version  1.0

import pytest
import allure
from utils.handle_excel import get_excel
from libs.shop import Shop
from utils.handle_path import report_path
from common.apiAssert import ApiAssert

@allure.epic('外卖系统')
@allure.feature('我的商铺')
class TestShop:
    @pytest.mark.parametrize('title,req_body,exp_resp',get_excel('我的商铺', 'listshopping', '标题', '请求参数', '响应预期结果'))
    @allure.story('列出商铺')
    @allure.title('{title}')
    def test_shop_query(self,shop_init:Shop,title,req_body,exp_resp):
        resp = shop_init.query(req_body)
        # assert resp['code'] == exp_resp['code']
        ApiAssert.api_assert(resp, '==', exp_resp, assert_info='code', msg='登录接口断言')

        # ApiAssert.api_assert(str(resp['code']), '==', str(exp_resp['code']))
        # ApiAssert.api_assert(str(resp['code']), '==', str(exp_resp['code']), assert_info='msg', msg='登录接口断言')



# 第一个版本
    @pytest.mark.parametrize('title,req_body,exp_resp', get_excel('我的商铺', 'updateshopping', '标题', '请求参数', '响应预期结果'))
    @allure.story('修改商铺')
    @allure.title('{title}')
    def test_shop_update(self,shop_init: Shop,title,req_body,exp_resp):
        with allure.step('1.用户登录'):
            pass
        with allure.step('2.选中编辑的商铺'):
            shop_id = shop_init.query({'page':1,'limit':20})['data']['records'][0]['id']
        with allure.step('3.替换店铺图片'):
            message_info = shop_init.file_upload('../data/123.png')['data']['realFileName']
        with allure.step('4.提交店铺信息'):
            resp = shop_init.update(req_body,shop_id,message_info)
        with allure.step('5.判断是否操作成功'):
            ApiAssert.api_assert(resp, '==', exp_resp, assert_info='code', msg='登录接口断言')








    # @pytest.mark.parametrize('title,req_body,exp_resp',get_excel('我的商铺', 'updateshopping', '标题', '请求参数', '响应预期结果'))
    # @allure.story('修改商铺')
    # @allure.title('{title}')
    # def test_shop_update(self, update_shop_init, shop_init, title, req_body, exp_resp):
    #     with allure.step('4.提交店铺信息'):
    #         resp = shop_init.update(req_body, update_shop_init['shop_id'], update_shop_init['image_info'])
    #         print(resp)
    #     with allure.step('5.判断是否操作成功'):
    #         # pass
    #         assert resp['code'] == exp_resp['code']


# if __name__ == '__main__':
#
#     pytest.main([__file__,'-sv'])
import os
if __name__ == '__main__':
    '''创建一个html网页'''
    # path = '../outFiles/report'
    path = report_path
    pytest.main([__file__, '-sv', '--alluredir', f'{path}', '--clean-alluredir'])
    # -v 详细的信息
    os.system(rf'allure serve {path}')



