import requests
import json

if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

    kw = input('enter a city name: ')
    data = {
        'cname': '',
        'pid': '',
        'keyword': kw,
        'pageIndex': '1',
        'pageSize': '10'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }

    response = requests.post(url=url, data=data, headers=headers)
    page_text = response.text

    # json格式存储
    # fileName = kw + '.json'
    # fp = open(fileName, 'w', encoding='utf-8')
    # json.dump(page_text, fp=fp, ensure_ascii=False)

    # TXT格式存储
    fileName = kw + '.txt'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    print(page_text)
