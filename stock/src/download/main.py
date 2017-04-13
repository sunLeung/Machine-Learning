#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys

sys.path.append(sys.path[0][0:-9])
from download import stock_info, stock_crawling

THEAD_COUNT = 8
THEAD_POOL = []


def crate_stock_queue():
    stock_queue = []
    for d in dict:
        if ('sh' in d):
            for code in dict[d]:
                stock_queue.append([d.split('.')[0], 'sh' + code])
        else:
            for code in dict[d]:
                stock_queue.append([d.split('.')[0], 'sz' + code])
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
    for t in thead_queue:
        thead = stock_crawling.StockCrawling(theadID, t)
        THEAD_POOL.append(thead)
        thead.start()
        print('Thread-' + str(theadID), 'started.')
        theadID += 1


if __name__ == '__main__':
    o = stock_info.StockInfo()
    o.auto_update()
    # o.read_stock_info()
    dict = stock_info.StockInfo.stock_info_dic
    start_crawling()