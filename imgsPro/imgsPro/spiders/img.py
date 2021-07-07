import scrapy
from imgsPro.items import ImgsproItem


class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//div[@id="container"]/div')
        for div in div_list:
            # src = div.xpath('./div/a/img/@src').extract_first()
            # print(src)
            # 返回的都是None，原因是图片软加载机制
            # 我们观察后几张图片发现 img 带的属性是 src2(伪属性), 只有慢慢拖动到图片显示，src2才会变成src
            # 而一个都没有是因为scrapy没有真正可视化浏览器，所以图片都不在可视化界面里
            # 只需要把src都改成src2
            src = div.xpath('./div/a/img/@src2').extract_first()
            print(src)

            item = ImgsproItem()
            item['src'] = src

            yield item