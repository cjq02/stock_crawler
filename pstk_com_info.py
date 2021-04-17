#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
公司基本信息查询 (PSTK_COM_INFO) 
Created on 2021/04/15
@author: cjq
"""

import json

import requests

from conf.database import execute_sql, get_data, get_uuid
from conf.request import API_URL, getHeaders


def main():
    rows = get_list()
    stock_code_list = []
    for row in rows:
        stock_code_list.append(row[1])

    stock_codes_list = []
    for chunk in list(partition(stock_code_list, 20)):
        stock_codes_list.append(','.join(chunk))

    # print(stock_codes_list)

    updateIndex = 0
    for stock_codes_str in stock_codes_list:
        url = '/base/PSTK_COM_INFO/full=2&filter-STOCKCODE-in-str={0}&zip=Gzip&skip=0&limit=20'.format(
            stock_codes_str)

        data = {
            'url': url,
            'page': 1,
            'skip': 0,
            'limit': 20,
            'id': '52'
        }
        resp = requests.post(API_URL, data=data, headers=getHeaders())
        print('请求数据股票代码：{}'.format(stock_codes_str))
        array = json.loads(resp.text)['data']
        for item in array:
            do_update(item)
            updateIndex += 1
            print('成功更新第{}条数据, 股票代码：{}，股票名称：{}'.format(
                updateIndex, item['STOCKCODE'], item['A_STOCKSNAME']))
    print('全部更新完成！')


def do_update(item):
    name = item['COMNAME']
    stock_code = item['STOCKCODE']
    supervision_name = item['CSRC_INDU_NAME']
    sw_industry_code = item['SW_INDU_CODE']
    sw_industry_name = item['SW_INDU_NAME']
    register_address = item['REGI_ADDR']

    update_sql = "UPDATE t_jj_corp_info SET name='{}', supervision_name='{}',sw_industry_code='{}',sw_industry_name='{}',register_address='{}'  WHERE stock_code = '{}'".format(
        name, supervision_name, sw_industry_code, sw_industry_name, register_address, stock_code)
    execute_sql(update_sql)


def get_list():
    select_sql = 'SELECT id, stock_code FROM t_jj_corp_info ORDER BY stock_code'
    return get_data(select_sql)


def partition(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


if __name__ == '__main__':
    main()
