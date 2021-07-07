import scrapy
from qiubaiPro.items import QiubaiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    '''
    基于终端指令的存储
    
    def parse(self, response):
        
        # 解析作者名称和段子内容
        div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
        all_data = []  # 存储所有解析数据
        for div in div_list:

            # xpath返回的是列表，但列表元素是Selector类型的对象
            # 调用.extract()将Selector对象中data参数存储的字符串提取出来
            author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()

            # 如果列表只有一个元素，可以用.extract_first()直接取到字符串
            author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()

            # 列表调用extract之后，表示将列表中每一个Selector对象中data参数存储的字符串提取出来
            # 返回对象是一个列表
            content = div.xpath('./a[1]/div/span//text()').extract()
            # 想要字符串的话
            content = ''.join(content)

            # print(author, content)
            dic = {
                'author': author,
                'content': content
            }

            all_data.append(dic)

        # 只有parse函数的返回值可以进行终端指令的存储(类型：'json', 'jsonlines', 'jl', 'csv', 'xml', 'marshal', 'pickle')
        # scrapy crawl qiubai -o ./qiubai.csv
        return all_data
    '''

    def parse(self, response):
        div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
        all_data = []  # 存储所有解析数据
        for div in div_list:
            author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            content = div.xpath('./a[1]/div/span//text()').extract()
            # 想要字符串的话
            content = ''.join(content)

            # 实例化item对象且封装解析数据
            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content

            # 将item提交给管道
            yield item

        return all_data

    # 有时候会稍微报个错，因为有的是匿名用户没有author值，但scrapy还是能完成爬虫任务把文件保存下来
    # 这个时候就要调整xpath 记得用 |
    # author = div.xpath('./div[1]/a[2]/h2/text() | ./div[1]/span/h[2]/text()')[0].extract()
