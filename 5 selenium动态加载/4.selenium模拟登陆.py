# 模拟登陆qq空间

from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='chromedriver')

bro.get('https://qzone.qq.com/')

bro.switch_to.frame('login_frame')
a_tag = bro.find_element_by_id('switcher_plogin')
a_tag.click()

username_tag = bro.find_element_by_id('u')
password_tag = bro.find_element_by_id('p')

username_tag.send_keys('761993493')
sleep(1)
password_tag.send_keys('yan19990204bo')
sleep(1)

btn = bro.find_element_by_id('login_button')
btn.click()

sleep(3)

bro.quit()
