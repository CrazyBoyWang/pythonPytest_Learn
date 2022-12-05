import pytest


# 字典类型
@pytest.mark.parametrize("one", [{"value": "abc"}, {"value": "abc1"}, {"value": "abc2"}])
def test_prarmetrize_02(one):
    print(one["value"])
    # assert one == 'value'


@pytest.mark.parametrize("one", [{"value": "abc", "value1": "abc"}, {"value": "abc1", "value1": "abc1"},
                                     {"value": "abc2", "value1": "abc2"}])
def test_prarmetrize_02(one):
    print(one["value"] + one["value1"])
    # assert one == 'value'
