import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']

    # 解析5大板块对应url
    models_urls = []

    # 浏览器只需要实例化一次
    def __init__(self):
        self.bro = webdriver.Chrome(executable_path='chromedriver')

    def parse(self, response):
        li_list = response.xpath('//*[@id="js_festival_wrap"]/div[3]/div[2]/div[2]/div[2]/div/ul/li')
        # 5大板块
        a_list = [3, 4, 6, 7, 8]
        for index in a_list:
            model_url = li_list[index].xpath('./a/@href').extract_first()
            self.models_urls.append(model_url)
        # 依次对每个板块对应的页面进行请求
        for url in self.models_urls:
            yield scrapy.Request(url, callback=self.parse_model)

    # 解析每一个板块页面中对应新闻标题和详情页的url
    # 但现在都是动态加载的，所以我们需要在中间件中编辑
    def parse_model(self, response):
        div_list = response.xpath('/html/body/div[1]/div[3]/div[4]/div[1]/div/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/img/@alt').extract_first()
            new_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()

            item = WangyiproItem()
            item['title'] = title
            # 对新闻详情页url发起请求
            yield scrapy.Request(url=new_detail_url, callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        content = response.xpath('//*[@id="endText"]/div[1]//text()').extract()
        content = ''.join(content)

        # 请求传参
        item = response.meta['item']
        item['content'] = content

        yield item

    # 关闭浏览器
    def closed(self, spider):
        self.bro.quit()
