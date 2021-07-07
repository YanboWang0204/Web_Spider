# 需求：爬取梨视频的生活类视频下最热视频的数据

import requests
from lxml import etree
import re
from multiprocessing.dummy import Pool

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
    }

# 原则：线程池处理的是阻塞且耗时的操作

# 对生活页视频发请求解析出视频详情页的url和视频的名称
url = 'https://www.pearvideo.com/category_5'
page_text = requests.get(url=url, headers=headers).text

tree = etree.HTML(page_text)
li_list = tree.xpath('/html/body/div[2]/div[1]/div/ul/li')
urls = []  # 存储所有视频的链接
for li in li_list:
    detail_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
    # print(detail_url, name)

    # 对详情页的url发请求
    detail_page_text = requests.get(url=detail_url, headers=headers).text
    with open('seepage.html', 'w', encoding='utf-8') as fp:
        fp.write(detail_page_text)

    # 从详情页中解析出视频的地址（url）
    # 问题是此时的视频页面是ajax动态加载的，可以在Name下的video的Response中查询<video发现没有
    # 但搜索mp4可以找到一个srcUrl， 但问题是现在这个属性在javascript类下，所以只能用正则来提取

    vtree = etree.HTML(detail_page_text)
    video_url = vtree.xpath('//*[@id="JprismPlayer"]/video')
    print(video_url)

    dic = {
        'name': name,
        'url': video_url
    }
    urls.append(dic)


def get_video_data(dic):
    url = dic['url']
    print(dic['name'], '正在下载......')
    data = requests.get(url=url, headers=headers).content
    # 持久化存储(也是一个耗时的操作)
    with open(dic['name'], 'wb') as fp:
        fp.write(data)
        print(dic['name'], '下载成功')


# 使用线程池对视频数据进行请求（较为耗时的阻塞操作）
pool = Pool(4)
pool.map(get_video_data, urls)

pool.close()
pool.join()  # 主线程在子线程结束后再结束
