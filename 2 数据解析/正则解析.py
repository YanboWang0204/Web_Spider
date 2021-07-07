# 收藏糗图百科下的热图板块的图片

'''
使用聚焦爬虫将页面中的所有热图进行解析、提取
点‘检查’可以发现图片属性中有
     <img src="//pic.qiushibaike.com/system/pictures/12342/123424058/medium/JPVO5AAE1XA6I8GX.jpg"
      lt="糗事#123424058" class="illustration" width="100%" height="auto">
所以我们希望对src带的地址发起请求，再仔细分析代码结构，发现是一串<div>嵌套
图片的src在<div class='thumb'>中
<div class="thumb">

<a href="/article/123424058" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/12342/123424058/medium/JPVO5AAE1XA6I8GX.jpg" alt="糗事#123424058" class="illustration" width="100%" height="auto">
</a>
</div>

我们可以编写一个正则来获取链接
ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'

'''

import requests
import re
import os

if __name__ == "__main__":
    # 创建一个文件夹，保存所有图片
    if not os.path.exists('./retuLibs'):
        os.mkdir('./retuLibs')
    url = 'https://www.qiushibaike.com/imgrank/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
    }

    # 用通用爬虫对url对应的一整张页面进行爬取
    page_text = requests.get(url=url, headers=headers).text  # 页面的源码数据

    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    img_src_list = re.findall(ex, page_text, re.S)  # re.S单行匹配，re.M多行匹配，返回对象是一个列表
    # print(img_src_list)

    for src in img_src_list:
        # 拼接出完整的图片地址
        src = 'https:' + src
        # 请求到了图片的二进制数据
        img_data = requests.get(url=src, headers=headers).content
        # 生成图片名称
        img_name = src.split('/')[-1]
        imgPath = './retuLibs/' + img_name

        # 存储图片
        with open(imgPath, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功！！')
