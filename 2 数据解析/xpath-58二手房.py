# 爬取58二手房中的房源信息，只要求解析房源的title

import requests
from lxml import etree

if __name__ == "__main__":
    # 先爬取页面源码数据
    url = 'https://bj.58.com/ershoufang/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
    }
    page_text = requests.get(url=url, headers=headers).text

    # 数据解析
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
    fp = open('58.txt', 'w', encoding='utf-8')

    for li in li_list:
        # 局部解析
        title = li.xpath('./div[2]/h2/a/text()')[0]  # ./表示从li开始
        print(title)
        fp.write(title + '\n')
