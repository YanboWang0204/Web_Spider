# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


# 下载中间件
class MiddleproDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    # UA池
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"
    ]

    # 代理IP
    PROXY_http = [
        '153.180.102.104:80',
        '195.208.131.189:56055'
    ]
    PROXY_https = [
        '120.83.49.90:9000',
        '95.189.112.214:35508'
    ]


    # 拦截请求
    def process_request(self, request, spider):
        # UA伪装
        # request.headers['User-Agent'] = 'xxxx' 这样和settings修改就一样了，我们希望用尽量多的ip
        # 所以我们列一个UA池，并且随机选择 random模块
        request.headers['User-Agent'] = random.choice(self.user_agent_list)
        return None

    # 拦截所有的响应
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    # 拦截发生异常的请求
    def process_exception(self, request, exception, spider):
        # 一般来说换ip都是因为我们被ban了，请求发生异常，所以代理ip写在这
        # request.meta['proxy'] = 'http://ip.port' 我们也用代理池分http和https类型

        if request.url.split(':')[0] == 'http':
            request.meta['proxy'] = 'http://' + random.choice(self.PROXY_http)
        else:
            request.meta['proxy'] = 'https://' + random.choice(self.PROXY_https)

        # 将修正后的对象进行重新的请求发送
        return request

    # 中间件记得要开启对应的settings，下载中间件就开启下载的