#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
import os
import time

sys.path.append(sys.path[0][0:-9])
from download import stock_info, stock_crawling

THEAD_COUNT = 8
THEAD_POOL = []
DATA_PATH = sys.path[0][0:-12]+'data/stock_data/'
INFO_PATH = sys.path[0][0:-12]+'data/stock_info/'


def crate_stock_queue():
    stock_queue = []
    for d in dict:
        if 'sh' in d:
            for code in dict[d]:
                stock_queue.append([d.split('.')[0], 'sh' + code])
        elif 'sz' in d:
            for code in dict[d]:
                stock_queue.append([d.split('.')[0], 'sz' + code])
        else:
            for code in dict[d]:
                stock_queue.append([d, code])
    one_size = stock_queue.__len__() // THEAD_COUNT
    thead_stock = []
    for t in range(THEAD_COUNT):
        if (t != THEAD_COUNT - 1):
            thead_stock.append(stock_queue[t * one_size:(t + 1) * one_size])
        else:
            thead_stock.append(stock_queue[t * one_size:])
    return thead_stock


def start_crawling():
    thead_queue = crate_stock_queue()
    theadID = 0
    path = get_path()
    for t in thead_queue:
        thead = stock_crawling.StockCrawling(theadID, t, path)
        THEAD_POOL.append(thead)
        thead.start()
        print('Thread-' + str(theadID), 'started.')
        theadID += 1


def get_path():
    """
    获取当天股票数据保存目录
    :return:
    """
    today = time.strftime('%Y-%m-%d', time.localtime())
    path = DATA_PATH+ today
    p1 = path + '/' + 'sh_a'
    p2 = path + '/' + 'sh_b'
    p3 = path + '/' + 'sz_a'
    p4 = path + '/' + 'sz_b'
    p5 = path + '/' + 'stock_index'
    if not os.path.exists(path):
        os.makedirs(p1)
        os.makedirs(p2)
        os.makedirs(p3)
        os.makedirs(p4)
        os.makedirs(p5)
    return path


if __name__ == '__main__':
    o = stock_info.StockInfo(INFO_PATH)
    o.auto_update()
    # o.read_stock_info()
    dict = stock_info.StockInfo.stock_info_dic
    start_crawling()
