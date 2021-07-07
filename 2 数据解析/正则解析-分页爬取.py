'''
观察url发现，/page/x决定了第几页的url,以此我们来进行分页爬取
https://www.qiushibaike.com/imgrank/page/2/
https://www.qiushibaike.com/imgrank/page/3/
'''


import requests
import re
import os

if __name__ == "__main__":
    # 创建一个文件夹，保存所有图片
    if not os.path.exists('./retuLibs'):
        os.mkdir('./retuLibs')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
    }

    # 设置一个通用的url模板
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    # pageNum = 2

    for pageNum in range(1, 14):
        # 对应页码的url
        new_url = format(url%pageNum)  # format返回字符串

        # 用通用爬虫对url对应的一整张页面进行爬取
        page_text = requests.get(url=new_url, headers=headers).text  # 页面的源码数据

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