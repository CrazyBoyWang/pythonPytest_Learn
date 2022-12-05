import pytest

mobile = "13248290532"


@pytest.mark.skip
def test_one():
    expect = 1
    actual = 2
    assert expect == actual


# 如果为true跳过该步骤，false则执行该步骤
@pytest.mark.skipif('len(mobile)==11')
def test_two():
    print(len(mobile))
    print("执行了")
    expect1 = 1
    actual1 = 1
    assert expect1 == actual1
