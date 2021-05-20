#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
公司基本信息查询 (PSTK_COM_INFO) 
Created on 2021/05/20
@author: cjq
"""

import json
import os
import requests

from conf.database import execute_sql, get_data, get_uuid
from conf.request import API_URL, getHeaders

YEAR_REPORT_DIR = 'Stock Year Reports'


def main():
    rows = get_list()
    for row in rows:
        stock_name = row[2].replace('*', '')
        stock_name_path = './{}/{}'.format(YEAR_REPORT_DIR, stock_name)
        if not os.path.exists(stock_name_path):
            os.mkdir(stock_name_path)
            print('创建文件夹：{}'.format(stock_name))


def get_list():
    select_sql = 'SELECT id, stock_code, bond_short FROM t_jj_corp_info ORDER BY stock_code'
    return get_data(select_sql)


def partition(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


if __name__ == '__main__':
    main()
