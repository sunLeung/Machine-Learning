#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys

sys.path.append(sys.path[0][0:-10])
from stock.src import stock_crawling, stock_info

THEAD_COUNT = 20
THEAD_POOL = []


def crate_stock_queue():
    stock_queue = []
    for d in dict:
        if ('sh' in d):
            for code in dict[d]:
                stock_queue.append([d.split('.')[0], 'sh' + code])
        else:
            for code in dict[d]:
                stock_queue.append([d.split('.')[0], 'sh' + code])
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
    dict = stock_info.StockInfo.stock_info_dic
    start_crawling()
    # while True:
    #     time.sleep(10)
    #     for t in THEAD_POOL:
    #         t.join()
