# 识别古诗文网登陆验证码

'''
使用打码平台识别验证码的编码流程：
   - 将验证码图片进行本地下载
   - 调用平台提供的示例代码进行图片数据识别
'''

import requests
from lxml import etree
from chaojiying import Chaojiying_Client


# 封装验证码函数
def getCodeText(imgPath, codeType):
    username = 'wyb200845'
    password = 'yan19990204bo'
    appid = '908457'

    chaojiying = Chaojiying_Client(username, password, appid)  # 用户中心>>软件ID 生成一个替换 96001
    im = open(imgPath, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    result = chaojiying.PostPic(im, codeType)['pic_str']  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    return result


# 将验证码图片下载到本地
# 只要获取到验证码图片的img src，对其发请求就能保存到本地了

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
    }
page_text = requests.get(url=url, headers=headers).text

# 解析验证码图片img对象中src属性值
tree = etree.HTML(page_text)
code_img_src = 'https://so.gushiwen.cn' + tree.xpath('//*[@id="imgCode"]/@src')[0]
img_data = requests.get(url=code_img_src, headers=headers).content

with open('./code.jpg', 'wb') as fp:
    fp.write(img_data)

# 调用打码平台
code_text = getCodeText('code.jpg', 1902)
print('识别结果为：', code_text)
# 返回结果为 识别结果为： qgk8， 对比图片发现是正确的
