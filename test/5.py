#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
批量新增研发补助
Created on 2021/04/16
@author: cjq
"""

import datetime
import json

import requests
from conf.database import batch_execute, execute_sql, get_data, get_uuid
from conf.request import API_URL, getHeaders
from utils.time_utils import TimeDuration


def main():
    # 开始
    duration = TimeDuration()
    duration.start()
    rows = get_corp_list()
    stock_index = 0
    update_index = 0
    year_list = [2015, 2016, 2017, 2018, 2019, 2020]
    sql_list = []
    for row in rows:
        corp_id = row[0]
        for year in year_list:
            add_sql(sql_list, corp_id, year)
    print('sql数量：{}'.format(len(sql_list)))
    duration.stop()
    duration.printDurationInfo()


def add_sql(sql_list, corp_id, year):
    id = get_uuid()
    sql = "INSERT INTO t_jj_corp_research_subsidy (id, corp_id, year, create_ts) values('{}','{}', '{}', '{}')".format(
        id, corp_id, year, datetime.datetime.now())
    sql_list.append(sql)
    print('{} 新增sql：{}'.format(datetime.datetime.now(), sql))


def get_corp_research_subsidy_list(corp_id, year):
    select_sql = "SELECT id FROM t_jj_corp_research_subsidy WHERE corp_id = '{}' AND year = '{}'".format(
        corp_id, year)
    return get_data(select_sql)


def get_corp_list():
    select_sql = 'SELECT id, stock_code, bond_short AS stock_name FROM t_jj_corp_info ORDER BY stock_code'
    return get_data(select_sql)


def partition(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def null_if(val):
    if val is None:
        return 'null'
    else:
        return val


if __name__ == '__main__':
    main()
