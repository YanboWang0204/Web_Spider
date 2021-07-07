from bs4 import BeautifulSoup

'''
如何实例化BeautifulSoup对象：
- 导包：from bs4 import BeautifulSoup
- 对象的实例化（两种方法）：
  - 1.将本地的html文档中的数据加载到该对象中
      fp = open('./test.html', 'r', encoding='utf-8')
      soup = BeautifulSoup(fp, 'lxml')
      
  - 2.将互联网上获取的页面源码加载到该对象中
      page_text = response.text
      soup = BeautifulSoup(page_text, 'lxml')

- 提供的用于数据解析的方法和属性
  - soup.tagName（标签名），返回html中第一次出现该tagName的标签
  
  - soup.find():
        - find('tagName')  # 相当于soup.tagName
        - 属性定位: 
          - soup.find('tagName', class_/id/attr = 'name')
          
  - soup.find_all('tagName'): 返回一个list包含符合标准的所有标签(和find功能一致)
  
  - select:
    - select('某种选择器（id, class, 标签...）')  # 返回一个list '.class'  '#id' 'a'(标签)  ’.class a‘ 
    - 层级选择器:
      - soup.select('.tang > ul > li > a')  # > 表示一个层级选择
      - soup.select('.tang > ul a') # 空格表示多个层级
  
  - 获取标签之间的文本数据
    - soup.a.text/string/get_text()
    - text/get_text(): 可以获取某一个标签中所有的文本内容（包括非直系）
    - string：只可以获取直系的文本内容
    
  - 获取标签中属性值
    - soup.a['href']
'''

if __name__ == "__main__":
    # 将本地的html文档数据加载到该对象中
    fp = open('./test.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'lxml')
    # print(soup)

    # soup.tagName（标签名），返回html第一次出现该tagName的标签
    # print(soup.div)

    # soup.find('div') 相当于soup.div
    # print(soup.find('div'))

    # print(soup.find('div', class_="song"))  # 记得此时class_有下划线才是参数名称

    # print(soup.find_all('div'))  # 返回的是一个list，包含所有该类型

    # print(soup.select('.tang'))

    # 层级选择 >
    # print(soup.select('.tang > ul > li > a')[0])

    # 多层级选择
    # print(soup.select('.tang > ul a')[0])

    # 获取文本
    # print(soup.select('.tang > ul > li > a')[0].text)

    # 获取属性
    # print(soup.select('.tang > ul > li > a')[0]['href'])
