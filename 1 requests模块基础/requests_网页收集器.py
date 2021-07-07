# 爬取搜狗指定此条对应的搜索结果页面（简易网页收集器）

'''
反反爬机制：UA伪装
UA：User-Agent(请求载体的身份标识)

UA检测：门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份标识为某一款浏览器，说明这个请求正常
但若检测到不是基于浏览器，则该请求不正常（爬虫），服务器可能会拒绝该次请求

UA伪装：让爬虫对应的请求身份标识伪装成某一款浏览器
'''

import requests

# 搜索 波晓张， 得到很长一串URL，可以删的只剩 query=波晓张 这个参数
if __name__ == "__main__":
    # url = 'https://www.sogou.com/web?query=%E6%B3%A2%E6%99%93%E5%BC%A0'  #复制下来会发现‘波晓张’被编码了，当然改回去也是Ok的
    # url = 'https://www.sogou.com/web?query=波晓张'

    # 处理url携带参数：封装到字典中，我们希望有一个动态的参数
    url = 'https://www.sogou.com/web?'  # 问号可删可不删

    # UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
    }

    kw = input('enter a word:')
    param = {
        'query': kw
    }
    # 对指定URL发起的请求对应的URL是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url, params=param, headers=headers)

    page_text = response.text

    fileName = kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName, '保存成功！！')
