'''
爬取豆瓣电影分类排行榜 https://movie.douban.com/ 中的电影详情数据

Request Method: GET
Content-Type: application/json

Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36

参数（query string parameters）：
type: 24
interval_id: 100:90
action:
start: 20
limit: 20
'''

import requests
import json

if __name__ == "__main__":
    url = 'https://movie.douban.com/j/chart/top_list?'

    # 把参数封装到字典里
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': ' ',
        'start': '0',   # 从库中的第几部电影去取
        'limit': '20'    #一次取出的个数
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
    }

    response = requests.get(url=url, params=param, headers=headers)
    print(response)
    list_data = response.json()
    print(list_data)

    # 存储
    fp = open('douban.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)

    print('over !!!')
