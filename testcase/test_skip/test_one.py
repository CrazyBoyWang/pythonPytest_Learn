import pytest


@pytest.mark.test
def test_one():
    expect = 1
    actual = 2
    assert expect == actual


def test_two():
    expect1 = 1
    actual1 = 1
    assert expect1 == actual1
