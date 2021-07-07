from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='chromedriver')

# 以淘宝为例
bro.get('https://world.taobao.com/')


# 物品的搜索实现

# 标签定位(找到搜索框)
search_input = bro.find_element_by_id('mq')
# 标签交互（输入搜索物）
search_input.send_keys('Iphone')

# 滚轮拖动实现

# 在抓包工具Console界面输入js代码：window.scrollTo(0, document.body.scrollHeight)
# 即向下滚动一屏幕
bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')
sleep(2)

# 找到搜索按钮并点击
btn = bro.find_element_by_xpath('//*[@id="J_PopSearch"]/div[1]/div/form/input[2]')
btn.click()

# 回退
bro.get('https://www.baidu.com')
sleep(2)
bro.back()  # 回退
sleep(2)
bro.forward()  # 前进


sleep(5)
bro.quit()
