import pytest
import requests


def test_mobile():
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

