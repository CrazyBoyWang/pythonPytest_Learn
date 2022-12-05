import pytest


@pytest.mark.pro
class TestThree:
    def test_one(self):
        expect = 1
        actual = 2
        assert expect == actual

    def test_two(self):
        expect1 = 1
        actual1 = 1
        assert expect1 == actual1
