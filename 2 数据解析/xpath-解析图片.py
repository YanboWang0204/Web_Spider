# 解析下载图片数据 http://pic.netbian.com/4kmeinv/
# 我们其实想解析的就是 img src 的页面，再发请求

import requests
from lxml import etree
import os

if __name__ == "__main__":
    # 先爬取页面源码数据
    url = 'http://pic.netbian.com/4kmeinv/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
    }
    response = requests.get(url=url, headers=headers)
    # 手动设定响应数据的编码格式，但可能解决不了
    # response.encoding = 'utf-8'
    page_text = response.text

    # 数据解析： src属性值， alt属性值作名称
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]//li')

    # 创建文件夹存储图片
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')

    for li in li_list:
        img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'   # 我们会发现img_name乱码了，可以考虑给response编码，或者img_name直接编码
        # 通用处理中文乱码的解决方案
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        # print(img_name, img_src)

        # 请求图片进行持久化存储
        img_data = requests.get(url=img_src, headers=headers).content
        img_path = 'picLibs/' + img_name

        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功！！！')
