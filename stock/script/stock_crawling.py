#!/usr/bin/python3
# -*- coding:utf-8 -*-

import threading
import time
import urllib.request as request


class StockCrawling(threading.Thread):
    url = 'http://hq.sinajs.cn/list=%s'
    path = '../data/stock_data/%s/%s'

    def __init__(self, TheadID, queue):
        threading.Thread.__init__(self)
        self.TheadID = TheadID
        self.queue = queue

    def __crawling_data(self, folder, code):
        data = ''
        try:
            url = self.url % (code)
            req = request.Request(url)
            resp = request.urlopen(req)
            resp_data = str(resp.read(), encoding='gbk')
            if (resp_data != ''):
                data = resp_data.split('=')[1]
                data = data[1: -6].replace(',', '`')
                file = self.path % (folder, code)
                with open(file, 'a', encoding='utf-8') as f:
                    f.write(data + '\n')
            resp.close()
        except Exception as e:
            print(e, 'stock_data code:', code)
        return data

    def run(self):
        count = 0
        while True:
            # 判断是否开市时间
            if self.__is_open_market():
                start_time = time.clock()
                for q in self.queue:
                    self.__crawling_data(q[0], q[1])
                count += 1
                print('Thead-' + str(self.TheadID), ' crawling finish:', count, ' cost seconds:',
                      time.clock() - start_time)
            else:
                print('Thead-' + str(self.TheadID), 'Market closed.')
                break

    def __is_open_market(self):
        lt = time.localtime()
        t = '%02d%02d' % (lt[3], lt[4])
        if int(t) >= 930 and int(t) <= 1130:
            return True
        elif int(t) >= 1300 and int(t) <= 1500:
            return True
        else:
            return False
