#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
股票代码表(STK_CODE)
Created on 2021/04/15
@author: cjq
"""

import json
import time

import requests

from conf.database import execute_sql, get_uuid
from conf.request import API_URL, getHeaders


def main():
    pageIndex = 1
    while(True):
        try:
            data = {
                'url': '/db/STK_CODE/full=2&filter-STATUS_TYPE-str=正常上市&filter-STK_TYPE-str=A股&zip=Gzip&skip=0&limit=20',
                'page': pageIndex,
                'skip': 0,
                'limit': 20,
                'id': 'd4574'
            }
            resp = requests.post(API_URL, data=data, headers=getHeaders())
            list = json.loads(resp.text)['data']

            for item in list:
                id = get_uuid()
                corp_code = item['COMCODE']
                stock_code = item['STOCKCODE']
                bond_short = item['STOCKSNAME']
                sql = "INSERT INTO t_jj_corp_info (id, corp_code, stock_code, bond_short) values('{0}','{1}', '{2}', '{3}')".format(
                    id, corp_code, stock_code, bond_short)
                execute_sql(sql)
                # print(resp.content.decode('unicode_escape'))
                print('股票代码：{0}，股票名称：{1}'.format(stock_code, bond_short))

            print('已导入{0}条数据'.format(pageIndex*20))
            pageIndex += 1
            """ time.sleep(1) """
        except BaseException:
            break
    print('导入数据成功！')


if __name__ == '__main__':
    main()
