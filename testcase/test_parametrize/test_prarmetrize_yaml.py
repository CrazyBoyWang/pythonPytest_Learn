import pytest

from utils.read_data import get_data
# # 字典类型
# @pytest.mark.parametrize("one", [{"value": "abc"}, {"value": "abc1"}, {"value": "abc2"}])
# def test_prarmetrize_02(one):
#     print(one["value"])
#     # assert one == 'value'


# 通过yaml配置文件获取参数数据,多参数配置方法
@pytest.mark.parametrize("name,word",get_data['heroes_name_word'])
def test_prarmetrize_02(name,word):
    print(name,word)

