from selenium import webdriver
from lxml import etree
from time import sleep

# 实例化一个浏览器对象（一定要传入浏览器的驱动程序）
bro = webdriver.Chrome(executable_path='chromedriver')

# 让浏览器发起一个指定url的对应请求
bro.get('http://scxk.nmpa.gov.cn:81/xk/')

# 获取浏览器当前页码的源码数据
page_text = bro.page_source

# 解析企业名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="gzlist"]/li')

for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)

sleep(10)
bro.quit()

'''
返回值：

广东天姿化妆品科技有限公司
平顶山市聚隆工贸有限公司
江苏娜维日用品实业有限公司
江苏省苏盐生活家股份有限公司化妆品分公司
江西乔盛茶皂素科技有限公司
江西鸿仁堂生物科技有限公司
广东粤妆生物科技有限公司
诺斯贝尔化妆品股份有限公司
沃德（天津）营养保健品有限公司
哈尔滨佰纳民生药业有限公司
蔚伊思美容品（武汉）有限公司
广州华人生物科技有限公司
国妆（广州）科技有限公司
广东菲塔赫医药生物科技有限公司
广州市高维化妆品有限公司
'''
