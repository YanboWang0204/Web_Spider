from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from PIL import Image
from chaojiying import Chaojiying_Client


def getCodeText(imgPath, codeType):
    username = 'wyb200845'
    password = 'yan19990204bo'
    appid = '908457'

    chaojiying = Chaojiying_Client(username, password, appid)  # 用户中心>>软件ID 生成一个替换 96001
    im = open(imgPath, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    result = chaojiying.PostPic(im, codeType)['pic_str']  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    return result


bro = webdriver.Chrome(executable_path='chromedriver')

bro.get('https://kyfw.12306.cn/otn/resources/login.html')


login_tag = bro.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a')
login_tag.click()
sleep(1)

bro.execute_script("document.body.style.zoom='0.8'")
# 截图并保存
bro.save_screenshot('aa.png')

# 先根据img类找到验证码的位置
code_img_ele = bro.find_element_by_xpath('//*[@id="J-loginImg"]')
# 确定验证码图片对应左上角和右下角的坐标（裁剪区域）
location = code_img_ele.location  # 左上角坐标 x, y, 字典形式
size = code_img_ele.size   # 长和宽(width, height)， 字典形式

# 左上角和右下角坐标
rangle = (
    int(location['x']), int(location['y']),
    int(location['x'] + size['width']), int(location['y'] + size['height'])
)

# 裁剪用PIL中Image类
i = Image.open('./aa.png')
code_img_name = './code.png'
frame = i.crop(rangle)
frame.save(code_img_name)

result = getCodeText('./code.png', 9004)

# 把坐标存成列表形式
all_list = []
if '|' in result:
    list_1 = result.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    xy_list = []
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)

print(all_list)

bro.execute_script("document.body.style.zoom='1.0'")
# 遍历列表，使用动作链对每一个列表元素对应的位置进行点击操作
action = ActionChains(bro)

for l in all_list:
    x = l[0]
    y = l[1]
    # 切换参照物到验证码图片位置
    place = action.move_to_element_with_offset(code_img_ele, x, y)
    place.click().perform()
    sleep(0.5)

username_tag = bro.find_element_by_id('J-userName')
password_tag = bro.find_element_by_id('J-password')

username_tag.send_keys('13915885978')
sleep(1)
password_tag.send_keys('yan19990204bo')
sleep(1)

bro.find_element_by_xpath('//*[@id="J-login"]').click()
sleep(3)

bro.quit()
