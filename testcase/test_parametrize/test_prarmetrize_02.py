import pytest


# 传多个参数时，one,two 分别代表两个key，key里面对应的数据要一一对应要不会报错
# @pytest.mark.parametrize("one,two", [("value","abc"), ("abc", "def"),("不知道","")])
# def test_prarmetrize_02(one,two):
#     print(one, two)
#     # assert one == 'value'

# 传多个参数时，就算参数只有一组，需要用数组或元组方式圈起来一层，要不执行会报错
@pytest.mark.parametrize("one,two", [("value","abc")])
def test_prarmetrize_02(one,two):
    print(one, two)
    # assert one == 'value'
