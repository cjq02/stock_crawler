#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
请求相关数据
Created on 2021/04/15
@author: cjq
"""

API_URL = 'http://z3cloud.cn/api-interfaces'

def getHeaders():
    return {
        'Cookie': 'Hm_lvt_3433c12dbaa82e357ff3b962fb281dac=1620264621,1621221979; Hm_lpvt_3433c12dbaa82e357ff3b962fb281dac=1621221995; XSRF-TOKEN=eyJpdiI6InM4cXFEeGxQSlFhSWdOb2RqQUdzdEE9PSIsInZhbHVlIjoiTXh5amZsS0JnaW5zOG9KbEd5RmttTEFWRndrUXlZNEowUU9jSnd0N0hQMGJjaVZ6S2MrVnAycks1XC9EMHlkajIiLCJtYWMiOiJkMWU4ZmUzODIyNmRkYmZkOWEwYTQwMWYyOTRiYTg1Y2ViYWJhYmY2MmFmMmE3ZWE4YzE0MDQ4ZjIxNjRlN2I4In0%3D; z3cloud_session=eyJpdiI6IjNycytsN3RsOVwvRXZDUVpRTFg3QUZ3PT0iLCJ2YWx1ZSI6IkE2aVVNOGhIU2FDMURxMlFcLzR4TzZneGVkYUloWWR1cHExNVJDNTVGSlI3MkdTcjk0Z3FkODZ2NXVvVVY5T1N5IiwibWFjIjoiZTQ0NmI5YzNiODhhZjU4MGIyODg5YWNhMzRiZjMwYjc0NGMyZTU5OTRlNzc2MzJlYWY5NjNhNjIzNjhhMmZmOCJ9',
        'X-CSRF-TOKEN': 'cRH7Lo9oAAHfyJuGalShtwiCkvo6gGMoXwPpdJST'
    }
