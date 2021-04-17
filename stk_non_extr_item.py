#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
上市公司非经常性损益表(STK_NON_EXTR_ITEM)
Created on 2021/04/15
@author: cjq
"""

import datetime
import json
import time

import requests

from conf.database import batch_execute, execute_sql, get_data, get_uuid
from conf.request import API_URL, getHeaders
from utils.time_utils import TimeDuration

REPORT_NAME = '非经常性损益表'
STOCK_INDEX = 3900
LIMIT_SIZE = 88


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
        corp_code = row[3]
        stock_index += 1

        print('{} {}，准备爬取第{}支股票，股票代码：{}， 股票名称：{}，已耗时：{}'.format(
            datetime.datetime.now(), REPORT_NAME, stock_index, stock_code, stock_name, duration.getTillNow()))

        pageIndex = 1
        array = []

        while(True):
            url = '/db/STK_NON_EXTR_ITEM/full=2&filter-COMCODE-int={}&filter-RPT_SRC-str=年报&filter-RPT_DATE-gte-dt=20151231&zip=Gzip&skip=0&limit=20'.format(
                corp_code)

            data = {
                'url': url,
                'page': pageIndex,
                'skip': 0,
                'limit': 20,
                'id': 'd14163'
            }
            resp = requests.post(API_URL, data=data, headers=getHeaders())
            try:
                json_data = json.loads(resp.text)
            except BaseException:
                break
            if json_data['code'] != 200:
                remain_count = LIMIT_SIZE + STOCK_INDEX - stock_index
                print('{} 爬取失败，数据为空，当前剩余{}支股票，已耗时：{}'.format(
                datetime.datetime.now(), remain_count, duration.getTillNow()))
                break

            print('{} 成功爬取第{}页数据'.format(datetime.datetime.now(), pageIndex))
            
            array.extend(json_data['data'])
            pageIndex += 1

        remain_count = LIMIT_SIZE + STOCK_INDEX - stock_index
        print('{} 成功爬取数据，当前剩余{}支股票，已耗时：{}'.format(
            datetime.datetime.now(), remain_count, duration.getTillNow()))

        if len(array) == 0:
            continue

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
        if '政府补助' in item['ITEM']:
            new_list.append(item)
    return new_list


def append_sql_list(sql_list, corp_id, stockItem):
    year = stockItem['RPT_DATE'][0:4]
    amt6 = null_if(stockItem['END_BOOK_VAL'])

    sql = "UPDATE t_jj_corp_research_subsidy SET amt6={},update_ts='{}' WHERE corp_id = '{}' AND year = '{}'".format(
        amt6, datetime.datetime.now(), corp_id, year)
    sql_list.append(sql)


def get_corp_list():
    select_sql = 'SELECT id, stock_code, bond_short, corp_code AS stock_name FROM t_jj_corp_info ORDER BY stock_code limit {} offset {}'.format(
        LIMIT_SIZE, STOCK_INDEX)
    return get_data(select_sql)


def null_if(val):
    if val is None:
        return 'null'
    else:
        return val


if __name__ == '__main__':
    main()
