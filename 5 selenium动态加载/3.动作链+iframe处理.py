from selenium import webdriver
from time import sleep
# 导入动作链对应的类
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path='chromedriver')

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

'''
# 先定位要拖动的小方块
div = bro.find_element_by_id('draggable')
print(div)
# 但这样就会报错了，报错原因是定位不到标签，这是因为现在的这一块包含在iframe子页面中
# 如果定位的标签是存在iframe标签中，必须通过以下操作进行标签定位
'''

# 切换浏览器标签定位的作用域
bro.switch_to.frame('iframeResult')  # 传iframe的id
div = bro.find_element_by_id('draggable')

# 动作链：长按并拖动拖动
action = ActionChains(bro)  # 实例化对象
action.click_and_hold(div)  # 点击长按指定标签

# 拖动
for i in range(5):
    # move_by_offset(x, y):x水平方向，竖直方向
    action.move_by_offset(17, 0).perform()  # perform() 立即执行
    sleep(0.3)

# 释放动作链接
action.release()

bro.quit()
