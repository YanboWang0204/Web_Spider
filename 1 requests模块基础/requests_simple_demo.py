'''
requests模块：python中原生的一款基于网络请求的模块
作用：模拟浏览器发请求

如何使用：(requests模块的编码流程)
    -指定URL
    -发起请求(get, post)
    -获取响应数据
    -持久化存储

pip install requests
'''

import requests

# 爬取搜狗首页的数据
if __name__ == "__main__":
    # step1 : 指定URL
    url = 'https://www.sogou.com/'
    # step2: 发起请求
    response = requests.get(url=url)  # get方法会返回一个响应对象

    #step3: 获取响应数据
    page_text = response.text  #text返回的是字符串形式的响应数据
    print(page_text)

    # step4: 持久化存储
    with open('sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取结束')
