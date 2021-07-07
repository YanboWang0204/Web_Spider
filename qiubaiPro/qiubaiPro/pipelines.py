# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class QiubaiproPipeline:

    fp = None

    # 重写父类的一个方法：该方法只会在开始爬虫的时候被调用一次
    def open_spider(self, spider):
        print('开始爬虫....')
        self.fp = open('./qiubai.txt', 'w', encoding='utf-8')

    # 接收爬虫文件提交过来的item对象
    # 专门用来处理item类型对象，进行持久化存储
    # 每接收一个item， process_item就会被调用一次

    def process_item(self, item, spider):
        author = item['author']
        content = item['content']

        self.fp.write(author + ':' + content + '\n')

        return item  # 这句就保证了item会被传递给下一个即将被执行的管道类

    # 关闭文件，也只要调用一次的父类方法
    def close_spider(self, spider):
        print('结束爬虫！')
        self.fp.close()


# 一个管道类对应将一组数据存储到一个平台或载体中
class MysqlPipeline(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306,
                                    user='root', password='yan19990204bo',
                                    db='qiubai')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute('insert into qiubai values("%s","%s")' % (item["author"], item["content"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()


# Q: 爬虫文件提交的item类型的对象最终会提交给哪一个管道类?
#    - 先执行优先级高的管道类
#    - 确保在先执行的管道类中process_item中添加 return item
#    - 这句就保证了item会被传递给下一个即将被执行的管道类
