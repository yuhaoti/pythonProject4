# @Author  yuhaotian
# @date  2023/7/18 16:25
# @version  1.0
import time



def show_time(func):
    def inner(*args,**kwargs):
        start_time = time.time()

        res = func(*args,**kwargs)
        endtime = time.time()
        print(f'执行测试用例')
    return inner
# test = show_time(test)  #狸猫换太子
# test()

@show_time
def test():
    print('开始执行测试用例')
    time.sleep(1)
    print('结束执行测试用例')
test()
