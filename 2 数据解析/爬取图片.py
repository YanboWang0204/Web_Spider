# 收藏糗图百科下的热图板块的图片

import requests
import json

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
    }
    # 右击可以找到‘复制图片地址’，这个url可以找到图片
    url = 'https://pic.qiushibaike.com/system/pictures/12342/123424058/medium/JPVO5AAE1XA6I8GX.jpg'

    # content返回二进制形式的图片数据
    # text(字符串)， content(二进制)， json() (对象)
    img_data = requests.get(url=url).content

    with open('./retu.jpg', 'wb') as fp:    # 'wb' 二进制写入
        fp.write(img_data)
