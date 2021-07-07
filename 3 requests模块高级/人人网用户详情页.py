import requests
from lxml import etree
from chaojiying import Chaojiying_Client


def getCodeText(imgPath, codeType):
    username = 'wyb200845'
    password = 'yan19990204bo'
    appid = '908457'

    chaojiying = Chaojiying_Client(username, password, appid)  # 用户中心>>软件ID 生成一个替换 96001
    im = open(imgPath, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    result = chaojiying.PostPic(im, codeType)['pic_str']  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    return result


# 创建session对象
session = requests.Session()

url = 'http://www.renren.com/SysHome.do'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
    }
page_text = requests.get(url=url, headers=headers).text

# 解析验证码图片img对象中src属性值
tree = etree.HTML(page_text)
code_img_src = tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
code_img_data = requests.get(url=code_img_src, headers=headers).content

with open('./renren_code.jpg', 'wb') as fp:
    fp.write(code_img_data)

result = getCodeText('renren_code.jpg', 1902)
# print('识别结果为：', result)  # 可以先测试一下：结果是fpqm，正确，说明目前程序没有问题

# post的模拟登陆
login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=20208304652'

data = {
    'email': '13915885978',
    'icode': result,
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '68cd3eeb400fdb1c52689e2757ae1c88d3d82c8524e999051bd57434f5a48658',
    'rkey': 'a75c249ee903f45aabc5742813171017',
    'f': 'http%3A%2F%2Fwww.renren.com%2F975196016%2Fnewsfeed%2Fphoto'
}

# 使用session进行POST请求发送
response = session.post(url=login_url, data=data, headers=headers)
print(response.status_code)

# 爬取当前用户的个人主页对应的页面数据
detail_url = 'http://www.renren.com/975196016/profile'

# 使用携带cookie的session进行get请求的发送
detail_page_test = session.get(url=detail_url, headers=headers).text
with open('wyb.html', 'w', encoding='utf-8') as fp:
    fp.write(detail_page_test)

# 我们会发现这样保存下来的不是个人详情页，而是登陆界面，所以失败了
'''
http/https协议特性：无状态
   - 服务器端不会记录我们的登陆状态，因此发起的第二次基于个人主页页面请求的时候，服务器并不知道此请求是基于登录状态下的请求
   
cookie: 用来让服务器端记录客户端的相关状态
   - 用抓包工具记录，找到Name下一条叫profile的记录，在Request Headers里面有Cookie这一项
   - 这里包含在请求中的cookie就是服务器端用来记录客户端状态的 

1. 手动cookie处理：通过抓包工具获取cookie值，并封装到headers中（不方便，且有的网站的cookie是有时长的）
headers = {
    'cookie': 'xxxxxx'
}

2. 自动处理：
   - cookie值的来源是哪里
     - 模拟登陆POST请求后，由服务器端进行创建（在Response headers里有Set-Cookie）
   - session会话对象：
     - 作用：1.可以进行请求的发送
            2.如果请求过程中产生了cookie，则该cookie会被自动存储/携带在session对象中
   
   - 步骤：
     - 创建一个session对象：requests.Session()
     - 使用session对象进行模拟登陆POST请求的发送（cookie就会被存储在session中）
     - session对象对个人主页对应的get请求进行发送（携带了cookie）
'''

