# -*- coding: utf-8 -*-
""" 

Created on: 2021-07-27 17:30
@author: Traceve
"""


from elasticsearch import Elasticsearch

es = Elasticsearch("ip", http_auth=("username", 'password'))

query_json = {
    "query": {
        "match_all": {}  # 获取所有数据
    }
}
page_num = 100  # 每次获取数据

query = es.search(index=8, body=query_json, scroll='5m', size=page_num)

results = query['hits']['hits']  # es查询出的结果第一页
total = query['hits']['total']  # es查询出的结果总量
scroll_id = query['_scroll_id']  # 游标用于输出es查询出的所有结果
every_num = int(total / page_num)  #

alist = []
for i in range(0, every_num + 1):
    # scroll参数必须指定否则会报错
    query_scroll = es.scroll(scroll_id=scroll_id, scroll='5m')['hits']['hits']
    results += query_scroll
for key in results:
    es_data_dict = key["_source"]["word"]
    # print(es_data_dict)
    alist.append(es_data_dict)
print(len(alist))
