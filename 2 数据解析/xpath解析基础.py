'''
如何实例化一个etree对象：
    - 导包：from lxml import etree

    - 1. 将本地的html文档中的源码数据加载到etree对象中：
         etree.parse(filePath)
    - 2. 将互联网上获取的页面源码数据加载到对象中：
         etree.HTML('page_text')

xpath('xpath表达式')： xpath只可以根据层级关系进行定位
    - /: 表示从根节点开始定位，一个/表示一个层级
    - //:表示多个层级，可以表示从任意位置开始定位
    - 属性定位:  tag[@attrName="attrvalue"]   e.g.//div[@class="song"]
    - 索引定位： //div[@class="song"]/p[3] 索引从1开始而不是0
    - 取文本：
      - /text() 获取标签中直系文本内容
      - //text() 获取标签下所有文本内容
    - 取属性：
      - /@attrName  e.g. img/@src

'''

from lxml import etree

if __name__ == "__main__":
    # 实例化一个etree对象，且把被解析的源码加载到对象中
    tree = etree.parse('test.html')

    # 获取title
    r = tree.xpath('/html/head/title')
    print(r)  # 返回一个list[<Element title at 0x1bd5d300c00>],包含element对象title

    # 获取div, 源文件中有3个div对象，因此列表应该返回3个element对象
    r = tree.xpath('/html/body/div')
    print(r)  # 返回[<Element div at 0x1be2e6d0d00>, <Element div at 0x1be2e6d0c80>, <Element div at 0x1be2e6d0d40>]

    # //
    r = tree.xpath('/html//div')  # 结果与之前一致
    print(r)

    r = tree.xpath('//div')  # 或者直接全部省略
    print(r)

    # 属性定位，指定特定的div对象
    r = tree.xpath('//div[@class="song"]')
    print(r)

    # 索引定位
    r = tree.xpath('//div[@class="song"]/p')  # 4个p标签，返回4个对象的list
    r = tree.xpath('//div[@class="song"]/p[3]')  # 拿到苏轼的p标签，注意这里的索引不是从0开始，而是1

    # 取文本 “杜牧”
    r = tree.xpath('//div[@class="tang"]//li[5]/a/text()')
    print(r)  # 返回['杜牧 ']列表，可以加[0]来取字符串
    r = tree.xpath('//div[@class="tang"]//li[5]/a/text()')[0]

    # text()只能返回直系文本内容
    r = tree.xpath('//li[7]/text()')  # 返回 [] 因为度蜜月不是li标签的直系文本内容

    # 改成//text()就可获得标签下所有文本内容
    r = tree.xpath('//li[7]//text()')
    print(r)

    # 以div[@class="tang"]为例，获取所有文本
    r = tree.xpath('//div[@class="tang"]//text()')
    print(r)

    # 返回['\n        ', '\n            ', '清明时节雨纷纷 ', '\n            ', '秦时明月汉时关 ', '\n            ', '崔九堂前几度闻 ',
    # '\n            ', '杜甫 ', '\n            ', '杜牧 ', '\n

    # 取属性：取img src属性值
    r = tree.xpath('//div[@class="song"]/img/@src')
    print(r)  # 返回 ['http://www.baidu.com/meinv.jpg']
