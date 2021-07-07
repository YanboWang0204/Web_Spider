import scrapy


# scrapy.Spider副类
class FirstSpider(scrapy.Spider):
    # 爬虫文件名称：就是爬虫源文件的唯一标识
    name = 'first'

    # 允许的域名：用来限定start_urls列表中哪些url可以进行请求发送（只有在这个列表中的域名可以发请求）
    # 一般都不会用到，因为大多时候保存文件和导向链接的url可能不在一个域名下
    # allowed_domains = ['www.baidu.com']

    # 起始的url列表：该列表中存放的url会被scrapy自动发请求
    start_urls = ['http://www.baidu.com/', 'http://www.sogou.com/']

    # 解析数据：response就是请求成功后对应的响应对象，多个对象parse会被调用多次
    def parse(self, response):
        print(response)
        '''        
        执行工程：scrapy crawl first
        我们会发现打印出来的没有网页信息，只有一些配置，找到其中一条日志：
        INFO: Overridden settings:
              {'BOT_NAME': 'FirstBlood',
               'NEWSPIDER_MODULE': 'FirstBlood.spiders',
               'ROBOTSTXT_OBEY': True,
               'SPIDER_MODULES': ['FirstBlood.spiders']}
        
        这里的'ROBOTSTXT_OBEY': True，在settings.py中修改
        再次执行，返回中有两条：
        <200 http://www.baidu.com/>
        <200 https://www.sogou.com/>
        
        这些输出日志很影响查看，我们可以在命令中加参数：
        scrapy crawl first --nolog
        
        但问题是一旦有错，错误信息也不输出，我们很难debug，可以在配置文件settings.py里修改 显示指定类型的日志信息
        LOG_LEVEL = 'ERROR'
        '''
