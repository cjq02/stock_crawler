#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
数据库操作
Created on 2021/04/15
@author: cjq
"""

import datetime
import uuid
import json
import psycopg2


def get_conn():
    json_file = open('./conf/conn.json')
    conn_info = json.load(json_file)
    print(conn_info['database'])
    return psycopg2.connect(database=conn_info['database'], user=conn_info['user'], password=conn_info['password'], host=conn_info['host'], port=conn_info['port'])


def execute_sql(sql):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(sql)

    conn.commit()
    cursor.close()
    conn.close()


def batch_execute(sql_list):
    conn = get_conn()
    cursor = conn.cursor()

    sql_length = len(sql_list)
    print('共{}条sql，开始执行...'.format(sql_length))

    index = 0
    for sql in sql_list:
        index += 1
        remain_length = sql_length-index
        print('{} 执行第{}条sql（剩余{}条）：{}'.format(
            datetime.datetime.now(), index, remain_length, sql))
        cursor.execute(sql)

    conn.commit()
    cursor.close()
    conn.close()


def get_data(sql):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(sql)
    data = cursor.fetchall()

    conn.commit()
    cursor.close()
    conn.close()

    return data


def get_uuid():
    return uuid.uuid4().hex
