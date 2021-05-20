#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
资产负债表（通用）(STK_BALA_GEN)
Created on 2021/04/15
@author: cjq
"""

import datetime
import json
import time
import sys

import requests

from conf.database import batch_execute, execute_sql, get_data, get_uuid
from conf.request import API_URL, getHeaders
from utils.time_utils import TimeDuration

REPORT_NAME = '资产负债表'
LIMIT_SIZE = int(sys.argv[1])
STOCK_INDEX = int(sys.argv[2])


def main():
    duration = TimeDuration()
    duration.start()
    rows = get_corp_list()
    sql_list = []
    stock_index = STOCK_INDEX
    for row in rows:
        corp_id = row[0]
        stock_code = row[1]
        stock_name = row[2]
        stock_index += 1
        url = '/db/STK_BALA_GEN/full=2&filter-A_STOCKCODE-str={}&filter-RPT_TYPE-str=合并&filter-RPT_SRC-in-str=年报&filter-RPT_DATE-gte-dt=20201231&zip=Gzip&field=RPT_DATE,ENDDATE,A_STOCKCODE,B100000,B300000&skip=0&limit=20'.format(
            stock_code)

        data = {
            'url': url,
            'page': 1,
            'skip': 0,
            'limit': 20,
            'id': 'd6663'
        }

        print('{} {}，准备爬取第{}支股票，股票代码：{}， 股票名称：{}，已耗时：{}'.format(
            datetime.datetime.now(), REPORT_NAME, stock_index, stock_code, stock_name, duration.getTillNow()))
        resp = requests.post(API_URL, data=data, headers=getHeaders())
        json_data = json.loads(resp.text)
        remain_count = LIMIT_SIZE + STOCK_INDEX - stock_index

        if json_data['code'] != 200:
            print('{} 爬取失败，数据为空，当前剩余{}支股票，已耗时：{}'.format(
                datetime.datetime.now(), remain_count, duration.getTillNow()))
            continue

        print('{} 成功爬取数据，当前剩余{}支股票，已耗时：{}'.format(
            datetime.datetime.now(), remain_count, duration.getTillNow()))
        array = json_data['data']
        new_list = filter_data(array)
        for item in new_list:
            append_sql_list(sql_list, corp_id, item)
        time.sleep(1)

    batch_execute(sql_list)
    print('成功更新{}数据到第{}支股票'.format(REPORT_NAME, stock_index))

    duration.stop()
    duration.printDurationInfo()


def filter_data(data_list):
    new_list = []
    for item in data_list:
        if (item['RPT_DATE'] == item['ENDDATE']):
            new_list.append(item)
    return new_list


def append_sql_list(sql_list, corp_id, stockItem):
    year = stockItem['RPT_DATE'][0:4]
    amt3 = null_if(stockItem['B100000'])
    amt4 = null_if(stockItem['B300000'])

    sql = "UPDATE t_jj_corp_research_subsidy SET amt3={},amt4={},update_ts='{}' WHERE corp_id = '{}' AND year = '{}'".format(
        amt3, amt4, datetime.datetime.now(), corp_id, year)
    sql_list.append(sql)


def get_corp_list():
    select_sql = 'SELECT id, stock_code, bond_short AS stock_name FROM t_jj_corp_info ORDER BY stock_code limit {} offset {}'.format(
        LIMIT_SIZE, STOCK_INDEX)
    return get_data(select_sql)


def null_if(val):
    if val is None:
        return 'null'
    else:
        return val


if __name__ == '__main__':
    main()
