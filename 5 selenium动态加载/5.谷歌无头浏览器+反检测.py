from selenium import webdriver
from time import sleep
# 实现无可视化界面
from selenium.webdriver.chrome.options import Options
# 实现规避检测
from selenium.webdriver import ChromeOptions


# 实现无可视化界面
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 实现规避检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])


# 如何实现让selenium无可视化界面 + 规避被检测的风险
bro = webdriver.Chrome(executable_path='chromedriver', chrome_options=chrome_options, options=option)

# 如何让我们的谷歌浏览器无可视化界面（无头浏览器）, phantomJS（一个有名的无头浏览器，但已经不维护了）
bro.get('https://www.baidu.com')

# 有打印结果说明行为动作触发了，但谷歌浏览器没有跳出
print(bro.page_source)
sleep(2)
bro.quit()
