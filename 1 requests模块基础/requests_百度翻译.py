'''
百度翻译：例如输入dog，页面自动更新了翻译部分，我们想要的并不是整个页面，而是翻译的部分
AJAX：旨在不重载整个页面的情况下对网页的局部进行更新

检查 > Network > XHR (ajax对应请求)

- post 请求（携带参数）
- 响应数据时一组json数据
'''

import requests
import json

if __name__ == "__main__":
    post_url = 'https://fanyi.baidu.com/sug'
    # post请求参数处理
    word = input('enter a word: ')
    data = {
        'kw': word
    }

    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
    }
    response = requests.post(url=post_url, data=data, headers=headers)

    # 获取响应数据：json()方法返回的是obj(如果确认响应数据时json类型的，才可以使用json())
    # 在Response headers里看 content-type: application/json
    dic_obj = response.json()
    print(dic_obj)

    # 持久化存储
    fileName = word + '.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)  # 中文不能进行ASCII编码

    print('over !!!')
