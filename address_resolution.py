#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
地址解析
Created on 2021/04/17
@author: cjq
"""

import datetime
import json
import time

import cpca
import requests

from conf.database import batch_execute, execute_sql, get_data, get_uuid
from utils.time_utils import TimeDuration


def main():
    duration = TimeDuration()
    duration.start()
    rows = get_corp_list()
    corp_count = len(rows)
    corp_index = 0
    sql_list = []
    for row in rows:
        corp_id = row[0]
        stock_code = row[1]
        stock_name = row[2]
        register_address = row[3]

        print('{} 准备处理第{}支股票，股票代码：{}， 股票名称：{}，地址：{}'.format(
            datetime.datetime.now(), corp_index, stock_code, stock_name, register_address))

        df = cpca.transform([register_address])
        data = json.loads(df.to_json(orient="records",force_ascii=False))
        province = data[0]['省']
        city = data[0]['市']
        corp_index += 1
        remain_count = corp_count - corp_index
        print('{} 解析成功！省：{}，市：{}，当前剩余{}支股票，已耗时：{}'.format(datetime.datetime.now(), province, city, remain_count, duration.getTillNow()))
        sql_list.append(get_sql(corp_id, province, city))

    # print(sql_list)
    batch_execute(sql_list)

    duration.stop()
    duration.printDurationInfo()


def filter_data(data_list):
    new_list = []
    for item in data_list:
        if (item['RPT_DATE'] == item['ENDDATE']):
            new_list.append(item)
    return new_list


def get_sql(id, province, city):
    return "UPDATE t_jj_corp_info SET province='{}', city='{}' WHERE id = '{}'".format(
        province, city, id)


def get_corp_list():
    select_sql = 'SELECT id, stock_code, bond_short AS stock_name, register_address FROM t_jj_corp_info ORDER BY stock_code'
    return get_data(select_sql)


def null_if(val):
    if val is None:
        return 'null'
    else:
        return val


if __name__ == '__main__':
    main()
