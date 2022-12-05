import pytest
import requests

from utils.read_data import get_data


def setup_module():
    print("准备测试数据")


def teardown_module():
    print("清理测试数据")

def test_mobile():
    params = get_data["mobile_belong"]
    print("打印数据：{0}".format(params))
    url = 'http://sellshop.5istudy.online/sell/shouji/query'

    a = requests.post(url=url, data= params)
    result = a.json()

    assert a.status_code == 200

    assert result['status'] == 0

    assert result['msg'] == "ok"

    assert result['result']['shouji'] == "13321170726"

    print(a.json())

    print(a.status_code)

@pytest.mark.parametrize("mobile,appkey",get_data["mobile_belong_method2"])
def test_mobile_method2(mobile,appkey):
    params = {
        "shouji": mobile,
        "appkey": appkey
    }
    print("打印数据：{0}".format(params))
    url = 'http://sellshop.5istudy.online/sell/shouji/query'

    a = requests.post(url=url, data= params)
    result = a.json()

    assert a.status_code == 200

    assert result['status'] == 0

    assert result['msg'] == "ok"

    assert result['result']['shouji'] == "13321170726"

    print(a.json())

    print(a.status_code)


@pytest.mark.parametrize("mobile,appkey",get_data["mobile_belong_method3"])
def test_mobile_method3(mobile,appkey):
    params = {
        "shouji": mobile,
        "appkey": appkey
    }
    print("打印数据：{0}".format(params))
    url = 'http://sellshop.5istudy.online/sell/shouji/query'

    a = requests.post(url=url, data= params)
    result = a.json()

    assert a.status_code == 200

    assert result['status'] == 0

    assert result['msg'] == "ok"

    # assert result['result']['shouji'] == "13321170726"

    print(a.json())

    print(a.status_code)


if __name__ == '__main__':
    pytest.main(['q', 'test_two.py'])
