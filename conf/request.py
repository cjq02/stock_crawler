#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
请求相关数据
Created on 2021/04/15
@author: cjq
"""

API_URL = 'http://xxx.cn/api-interfaces'

def getHeaders():
    return {
        'Cookie': 'keyword=eyJpdiI6InMxTVpUZlNmOXVcL2pXZitFbE40STlnPT0iLCJ2YWx1ZSI6ImFzcU5BTVZ0S2pGTDNHMmFzZGxSRlNnbHluUjhHU1BydW16NnBHUXJySEE9IiwibWFjIjoiNGIyZmRmZjEwNTNiNTVmOTVjOWIwMzk4NjFmMjZlZTgwYTJhZWJmMTkzOGE3ODg3MDEyMTUzYjQ4NTI0NjhjMyJ9; Hm_lvt_c26dbbade3b41a6d0fefa3d9b00e285a=1618455547; Hm_lvt_3433c12dbaa82e357ff3b962fb281dac=1618491455,1618536517,1618579806,1618629308; XSRF-TOKEN=eyJpdiI6Ikl3QWxyeW14MlpRaWhCd0hYMDNrdnc9PSIsInZhbHVlIjoiZWVpeEs4WCtiVlJMRkhXOTJZUzNRVW9mTkg0MEdRcDdBNHJVcW0rRjFxcjYybFVhVHg4cXRmUVZyam0waGZVbCIsIm1hYyI6IjQ3M2JlMjI1NTlmMTFhNjFhZDgzMWI3NDIwY2UxMDNlZDljM2M2ZTAwMjgxOTBhZWQzOTkwYTJkYTIzMDgxMjAifQ%3D%3D; z3cloud_session=eyJpdiI6IlplQ0FEbVFcLzhtQ0FKU0Jydm9ubmNRPT0iLCJ2YWx1ZSI6IjZPWk1FV1p4UFhzRk5YaUtvdW1nSlBjS0hJYXBkUUtwMStZQkp2UG9COVVocE1uNmhyY0JzZHlaSjhJQkEzZ0oiLCJtYWMiOiIyNjNiOGQ0NzRlMmI3NTlmZjlkN2Y5NDgyMzMwZjdlYTVjZDFjMmUzY2JhMGNkOWQzYzQ1MjI1NzYxZmJiODA5In0%3D; Hm_lpvt_3433c12dbaa82e357ff3b962fb281dac=1618629321',
        'X-CSRF-TOKEN': 'POvBpR8fqV5FaPOKo9Jt46Mmc895mS3Lo7TgJKoG'
    }
