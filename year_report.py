import json
import os
import xlrd
import csv
from time import sleep
from urllib import parse
import random

import requests

YEAR_REPORT_DIC = 'Stock Year Reports'

def get_address(stock_name):
    url = "http://www.cninfo.com.cn/new/information/topSearch/detailOfQuery"
    data = {
        'keyWord': stock_name.lower(),
        'maxSecNum': 10,
        'maxListNum': 5,
    }
    user_agent_list = [
        "Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 75.0.3770.100Safari / 537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Firefox/61.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"]

    hd = {
        'Host': 'www.cninfo.com.cn',
        'Origin': 'http://www.cninfo.com.cn',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip,deflate',
        'Connection': 'keep-alive',
        'Content-Length': '70',
        'User-Agent': random.choice(user_agent_list),
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json,text/plain,*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    r = requests.post(url, headers=hd, data=data)
    """ print(r.text) """
    r = r.content
    m = str(r, encoding="utf-8")
    """ print(m) """
    pk = json.loads(m)
    orgId = pk["keyBoardList"][0]["orgId"]  # 获取参数
    plate = pk["keyBoardList"][0]["plate"]
    code = pk["keyBoardList"][0]["code"]
    """ print(orgId, plate, code) """
    return orgId, plate, code


def get_PDF(orgId, plate, code):
    url = "http://www.cninfo.com.cn/new/hisAnnouncement/query"
    data = {
        'stock': '{},{}'.format(code, orgId),
        'tabName': 'fulltext',
        'pageSize': 30,
        'pageNum': 1,
        'column': plate,
        'category': 'category_ndbg_szsh;',
        'plate': '',
        'seDate': '',
        'searchkey': '',
        'secid': '',
        'sortName': '',
        'sortType': '',
        'isHLtitle': 'true',
    }
    user_agent_list = [
        "Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 75.0.3770.100Safari / 537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Firefox/61.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"]

    hd = {
        'Host': 'www.cninfo.com.cn',
        'Origin': 'http://www.cninfo.com.cn',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip,deflate',
        'Connection': 'keep-alive',
        # 'Content-Length': '216',
        'User-Agent': random.choice(user_agent_list),
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json,text/plain,*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'X-Requested-With': 'XMLHttpRequest',
        # 'Cookie': cookies
    }
    data = parse.urlencode(data)
    # print(data)
    r = requests.post(url, headers=hd, data=data)
    # print(r.text)
    r = str(r.content, encoding="utf-8")
    r = json.loads(r)
    reports_list = r['announcements']
    for report in reports_list:
        if '摘要' in report['announcementTitle'] or "20" not in report['announcementTitle']:
            continue
        if 'H' in report['announcementTitle']:
            continue
        else:  # http://static.cninfo.com.cn/finalpage/2019-03-29/1205958883.PDF
            pdf_url = "http://static.cninfo.com.cn/" + report['adjunctUrl']
            file_name = report['announcementTitle']
            download_PDF(pdf_url, file_name)
            sleep(1)


def download_PDF(url, file_name):  # 下载pdf
    url = url
    r = requests.get(url)
    down_file = '{}\{}\{}\{}.pdf'.format(
        os.getcwd(), YEAR_REPORT_DIC, stock_name, file_name)
    if os.path.exists(down_file):
        print('当前目录下{}已经存在！'.format(down_file))
    else:
        print('正在下载：{}，文件路径：{}'.format(url, down_file))
        f = open(down_file, "wb")
        f.write(r.content)


if __name__ == '__main__':
    # stock_list = [ '中信银行','民生银行', '华夏银行','交通银行', '中国银行', '招商银行', '浦发银行','建设银行', ]
    # stock_list = ["山西焦煤"]

    # workBook = xlrd.open_workbook('stock_name.xlsx')
    # SheetName = workBook.sheet_names()[0]
    # sheet1_content = workBook.sheet_by_name(SheetName)
    # stock_list = sheet1_content.col_values(0)[1:]

    error_list = []
    with open('./data/stock_name.txt', encoding='utf-8', errors='ignore') as f:
        stock_list = f.readlines()

    for stock_name in stock_list:
        stock_name = stock_name.strip()
        try:
            orgId, plate, code = get_address(stock_name)
            stock_name_path = './{}/{}'.format(YEAR_REPORT_DIC, stock_name)
            if not os.path.exists(stock_name_path):
                os.mkdir(stock_name_path)
            get_PDF(orgId, plate, code)
            print(stock_name + "下载完成；")
        except:
            error_list.append(stock_name)
            continue
    print("全部下载完成！")
    print("有问题的股票：")
    print(error_list)
