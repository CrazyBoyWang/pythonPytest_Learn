import pytest
import requests

from utils.log_util import logger


def setup_module():
    print("准备测试数据")


def teardown_module():
    print("清理测试数据")


def test_mobile():
    logger.info("开始执行测试")
    params = {'shouji': 13321170726, "appkey": "Oc818521d38759e1"}

    url = 'http://sellshop.5istudy.online/sell/shouji/query'

    a = requests.post(url=url, data=params)
    result = a.json()

    assert a.status_code == 200

    assert result['status'] == 0

    assert result['msg'] == "ok"

    assert result['result']['shouji'] == "13321170726"

    print(a.json())

    print(a.status_code)
    logger.info("执行结束")


if __name__ == '__main__':
    pytest.main(['q', 'test_two.py'])
