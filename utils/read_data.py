import os

import yaml

# 获取config文件中的yaml文件地址。参考util中test.py操作
path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"config","data.yaml")
def read_data():
    # 读取文件
    f = open(path,encoding="utf8")
    data = yaml.safe_load(f)
    return data


get_data = read_data()

# print(get_data['heroes_name_word'])
