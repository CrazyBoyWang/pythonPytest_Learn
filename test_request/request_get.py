import requests

json = {'shouji':13321170726,'appkey':'Oc818521d38759e1'}
a = requests.get('http://sellshop.5istudy.online/sell/shouji/query',params=json)

print(a.json())

print(a.status_code)
