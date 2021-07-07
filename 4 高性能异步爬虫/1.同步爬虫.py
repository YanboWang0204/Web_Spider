import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
    }

urls = [
    'http://xmdx.sc.chinaz.net/Files/Download/jianli/201904/jianli10231.rar',
    'http://zjlt.sc.chinaz.net/Files/Download/jianli/201904/jianli10229.rar',
    'http://xmdx.sc.chinaz.net/Files/Download/jianli/201904/jianli10231.rar'
]


def get_content(url):
    print('正在爬取：', url)

    # get方法是一个阻塞的方法（串行）
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.content


def parse_content(content):
    print('响应数据的长度为：', len(content))


for url in urls:
    content = get_content(url)
    parse_content(content)