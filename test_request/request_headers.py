import requests

params = {'type': 'tv', 'source': 'index'}

url = 'https://movie.douban.com/j/search_tags'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

a = requests.get(url=url, params=params,headers=headers)
print(a.status_code)

print(a.json())

