#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
数据库操作
Created on 2021/04/15
@author: cjq
"""

import datetime
import uuid

import psycopg2


def get_conn():
    return psycopg2.connect(database="szfile_dev", user="szfile_dev", password="szfile_dev", host="120.79.137.53", port="5432")


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
    
    print('共{}条sql，开始执行...'.format(len(sql_list)))

    index = 0
    for sql in sql_list:
        index += 1
        print('{} 执行第{}条sql：{}'.format(datetime.datetime.now(), index, sql))
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
