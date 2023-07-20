# @Author  yuhaotian
# @date  2023/7/6 9:22
# @version  1.0
import yaml


def get_yaml_data():
    path = '../configs/apiPathConfig.yaml'
    with open(path,encoding='utf-8') as f:
        res = yaml.safe_load(f.read())     #yaml.safe_load(sys.stdin)只是yaml.load(sys.stdin,Loader=yaml.SafeLoader)。
        # yam.salf_load  函数用来解析yaml文件格式的数据
        return res



if __name__ == '__main__':

    # path = '../configs/apiPathConfig.yaml'
    res = get_yaml_data()
    print(res)

