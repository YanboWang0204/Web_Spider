# 爬取国家药品监督管理总局中化妆品生产许可证相关数据

import requests
import json

if __name__ == '__main__':
    '''
    url = 'http://scxk.nmpa.gov.cn:81/xk/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }

    page_text = requests.get(url=url, headers=headers).text

    with open('./test.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    '''
    # 这样出来的网页是乱码，也没有我们直接打开浏览器获得的各个公司的链接，说明这些公司的链接可能是通过AJAX请求得到的
    # 我们可以用抓包工具验证，在response里搜索某个公司的名称发现没有，因此对该url发请求不能链接到这些公司的许可证

    # Response中每条记录有一个独特的ID字段，再观察每个公司对应的许可证页面，我们发现这个id可以对应许可证的url
    # 例如： http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=ff83aff95c5541cdab5ca6e847514f88
    # id值可以通过从首页对应的ajax请求到的json串中获取，域名和id值拼接出一个企业许可证的url

    # 但我们会发现详情页的数据也是ajax动态加载出来的
    # 例如：http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
    #      http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
    # 观察发现所有post请求的url是一样的，只有参数id值是不同的
    # 因此只要我们可以批量获取id后，就可以将id和url形成一个完整的详情页对应详情数据的ajax请求的url


    # 批量获取不同企业id
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    # 参数封装
    # 获取多页

    id_list = []  # 存储企业id
    for page in range(1, 6):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }

        json_ids = requests.post(url=url, data=data, headers=headers).json()
        for dic in json_ids["list"]:
            id_list.append(dic['ID'])

    # print(id_list)

    # 获取企业详情数据
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'

    all_data_list = []  # 存储所有企业详细信息
    for id in id_list:
        data = {
            'id': id
        }
        detail_json = requests.post(url=post_url, data=data, headers=headers).json()
        #print(detail_json, '------------------ending----------------------')
        all_data_list.append(detail_json)

    # 持久化存储all_data_list
    fp = open('alldata.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)
    print('over')

