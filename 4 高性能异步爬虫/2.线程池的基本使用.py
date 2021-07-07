'''
import time


# 使用单线程串行方式执行
def get_page(str):
    print("正在下载：", str)
    time.sleep(2)
    print("下载成功：", str)


name_list = ['xiaozi', 'aa', 'bb', 'cc']

start_time = time.time()

for i in range(len(name_list)):
    get_page(name_list[i])

end_time = time.time()
print('%d second' % (end_time - start_time))

# 4个阻塞操作，time 8 second
'''

import time
# 导入线程池模块对应的类
from multiprocessing.dummy import Pool


# 使用线程池方式执行
start_time = time.time()
def get_page(str):
    print("正在下载：", str)
    time.sleep(2)
    print("下载成功：", str)


name_list = ['xiaozi', 'aa', 'bb', 'cc']

# 实例化一个线程池对象
pool = Pool(4)  # 线程池中开辟4个线程对象，对应4个阻塞对象

# 将列表中每一个元素传递给get_page进行处理 pool.map(func, iter)
# map的返回值就是func的返回值，现在get_page没返回值，如果有会依次赋值给map的返回值
pool.map(get_page, name_list)

end_time = time.time()
print('%d second' % (end_time - start_time))

# 这次返回的就是 2 second，线程池同时运行了4个对象
