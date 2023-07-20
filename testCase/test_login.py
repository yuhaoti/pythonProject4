# @Author  yuhaotian
# @date  2023/7/11 9:13
# @version  1.0
import os
import allure
import pytest
from utils.handle_excel import get_excel
from libs.login import Login
from common.apiAssert import ApiAssert

@allure.epic('订餐系统')
@allure.feature('登录模块')
class Test_Login:

    test_data= get_excel('登录模块','Login','标题','请求参数', '响应预期结果')
    @pytest.mark.parametrize('title,req_body,rexp_body',test_data)
    @allure.story('登录接口')
    @allure.title('{title}')
    def test_login(self,title,req_body,rexp_body):
        resp = Login().login(req_body,True)
        ApiAssert.api_assert(resp,'==',rexp_body,assert_info='msg',msg = '登录接口断言')
        # assert resp['msg'] == rexp_body['msg']






if __name__ =='__main__':
    '''创建一个html网页'''
    path = '../outFiles/report'
    pytest.main([__file__, '-sv', '--alluredir', f'{path}', '--clean-alluredir'])
    # -v 详细的信息
    os.system(rf'allure serve {path}')



