import pytest


# @pytest.mark.parametrize(key,value)
# @pytest.mark.parametrize("key",["value"])
# def test_prarmetrize_01(key):
#     print("参数化" + key)


# 单次循环
# @pytest.mark.parametrize("key",["value"])
# def test_prarmetrize_01(key):
#     assert key == 'value'

# 多次循环，根据注释中里面带参数数量。有多少参数就会循环多少次
@pytest.mark.parametrize("key", ["value", "abc", "def"])
def test_prarmetrize_01(key):
    assert key == 'value'
