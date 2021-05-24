#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
修改文件夹名称
Created on 2021/05/20
@author: cjq
"""

import os
import sys
from conf.database import batch_execute, execute_sql, get_data
from utils.time_utils import TimeDuration

REPORT_DIR = sys.argv[1]


def main(duration):
    dirs = os.listdir(REPORT_DIR)
    rows = get_list()
    """ print(rows) """
    for dir in dirs:
        result_list = list(filter(lambda item: item[2] == dir, rows))
        if len(result_list) == 0:
            continue
        row = result_list[0]
        stock_code = row[1]
        old_dir_name = os.path.join(REPORT_DIR, dir)
        new_dir_name = os.path.join(REPORT_DIR, stock_code)
        os.rename(old_dir_name, new_dir_name)


def get_list():
    select_sql = 'SELECT id, stock_code, bond_short AS stock_name FROM t_jj_corp_info ORDER BY stock_code'
    return get_data(select_sql)


if __name__ == '__main__':
    duration = TimeDuration()
    duration.start()
    main(duration)
    duration.stop()
    duration.printDurationInfo()
