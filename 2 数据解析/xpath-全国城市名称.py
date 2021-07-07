# 解析出所有城市名称：https://www.aqistudy.cn/historydata/

import requests
from lxml import etree
import os

if __name__ == "__main__":

    '''
    # 先爬取页面源码数据
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
    }
    page_text = requests.get(url=url, headers=headers).text

    tree = etree.HTML(page_text)
    hot_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    all_city_names = []

    # 解析热门城市名称
    for li in hot_li_list:
        hot_city_name = li.xpath('./a/text()')[0]
        all_city_names.append(hot_city_name)

    # 解析全部城市的名称
    city_names_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    for li in city_names_list:
        city_name = li.xpath('./a/text()')[0]
        all_city_names.append(city_name)

    print(all_city_names, len(all_city_names))
    '''


    # 之前我们解析了两次，其实可以用通用xpath表达式一次解析出来

    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
    }
    page_text = requests.get(url=url, headers=headers).text

    tree = etree.HTML(page_text)
    # 解析到热门城市和所有城市对应的a标签
    # 热门城市：//div[@class="bottom"]/ul/li/a
    # 全部城市：//div[@class="bottom"]/ul/div[2]/li/a
    # 用 | 来连接
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_names = []
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        all_city_names.append(city_name)
    print(all_city_names, len(all_city_names))
