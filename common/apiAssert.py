# @Author  yuhaotian
# @date  2023/7/13 19:10
# @version  1.0

from utils.handle_loguru import log
import traceback
class ApiAssert:
    @classmethod
    def api_assert(cls,result,condition,exp_result,assert_info,msg):
        try:
            result,exp_result = str(result[assert_info]),str(exp_result[assert_info])
            assert_type = {
                '==':result==exp_result,
                '!=':result!=exp_result,
                '>':result > exp_result,
                '<':result< exp_result,
                'in':result in exp_result,
                'not in':result not in exp_result,
            }
            if condition in assert_type:
                assert assert_type[condition]
            else:
                raise AssertionError('请输入正确的断言情况')
            # log_pass.format(exp_result[assert_info],result[assert_info])
            # log.info(f'{msg},断言类型{condition},(预期结果，实际结果){exp_result[assert_info],result[assert_info]}')
            log.info(f'{msg},断言类型{condition},(预期结果，实际结果){exp_result,result}')
        except Exception as error:
            log.error(traceback.format_exc())
            raise error





