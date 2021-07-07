'''
需求：对人人网进行模拟登陆
F12调抓包工具，先clear,再点 preserve log，登陆进去，在Name里找到一个login，
它是一个POST请求，参数是
email: 13915885978
icode:
origURL: http://www.renren.com/home
domain: renren.com
key_id: 1
captcha_type: web_login
password: 3606d7014455277cfd095964344376f841262984b9b7b5ea8a4ae1d6a878b672
rkey: 227f4ceb2f44827f9de8296ca1ef1c3f
f: http%3A%2F%2Fsafe.renren.com%2F

Request URL: http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=20208304652
Content-Type: text/html

编码流程：
   - 验证码识别，获取验证码图片的文字数据
   - 对POST请求进行发送（处理请求参数）
   - 对响应数据进行持久化存储
'''

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


'''
保存页面的方法
response = requests.post(url=login_url, data=data, headers=headers)
login_text = response.text
with open('renren.html', 'w', encoding='utf-8') as fp:
    fp.write(login_text)

保存的结果是一个字典：{"code":true,"homeUrl":"http://www.renren.com/home"}
只要把其中的URL放到浏览器中，就能看到你的页面了
'''

# 但有的网页登陆成功后返回的不一定是用户页面的html，可能是字符串等等，我们需要一种更统一的方式验证是否登陆成功
# 我们可以通过查看POST请求的响应状态码，如果是200意味着登陆成功

response = requests.post(url=login_url, data=data, headers=headers)
print(response.status_code)
