#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
批量导入年报
Created on 2021/05/21
@author: cjq
"""

import os
import sys
from datetime import datetime
from conf.database import batch_execute, execute_sql, get_data, get_uuid
from utils.time_utils import TimeDuration

ROOT_DIR = sys.argv[1]
REPORT_DIR = '/stock/year_report'


def main(duration):
    dirs = os.listdir(ROOT_DIR + REPORT_DIR)
    rows = get_list()
    """ print(rows) """
    sql_list = []
    for dir in dirs:
        result_list = list(filter(lambda item: item[1] == dir, rows))
        if len(result_list) == 0:
            continue
        row = result_list[0]
        corp_id = row[0]
        stock_code = row[1]
        files = os.listdir('{}/{}'.format(ROOT_DIR + REPORT_DIR, dir))
        for file_name in files:
            add_sql(sql_list, corp_id, stock_code, file_name)
    batch_execute(sql_list)
        


def get_list():
    select_sql = 'SELECT id, stock_code AS stock_name FROM t_jj_corp_info ORDER BY stock_code'
    return get_data(select_sql)

def add_sql(sql_list, corp_id, stock_code, file_name):
    id = get_uuid()
    currentTime = datetime.now()
    file_url = '{}/{}/{}'.format(REPORT_DIR, stock_code, file_name)
    sql = "INSERT INTO t_jj_corp_year_report (id, corp_id, file_name, file_url, create_ts) values('{}','{}', '{}', '{}', '{}')".format(
        id, corp_id, file_name, file_url, currentTime)
    sql_list.append(sql)
    print('{} 新增sql：{}'.format(currentTime, sql))

if __name__ == '__main__':
    duration = TimeDuration()
    duration.start()
    main(duration)
    duration.stop()
    duration.printDurationInfo()
