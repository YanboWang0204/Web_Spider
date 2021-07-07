'''
在百度输入ip检索，可以得到本机ip: 188.39.230.50
那如果我们代理成功，就应该在请求后显示的不是本机的ip了
https://www.baidu.com/s?wd=ip
'''

import requests

url = 'https://www.baidu.com/s?wd=ip'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }

# 这里需要utf-8编码否则会乱码，而且百度的反爬会让你第二次登陆就是安全验证的界面，可以换个浏览器ip
response = requests.get(url=url, headers=headers, proxies={"https": '58.22.177.14:9999'})
response.encoding = 'utf-8'
page_text = response.text

with open('ip代理.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
