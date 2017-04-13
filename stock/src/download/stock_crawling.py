#!/usr/bin/python3
# -*- coding:utf-8 -*-

import threading
import time
import requests


class StockCrawling(threading.Thread):
    url = 'http://hq.sinajs.cn/list=%s'
    path = '../../data/stock_data/%s/%s'
    session = requests.Session()

    def __init__(self, theadID, queue):
        threading.Thread.__init__(self)
        self.theadID = theadID
        self.queue = queue
        codes_list = []
        for i in queue:
            codes_list.append(i[1])
        self.url = self.url % (','.join(codes_list))

    def __crawling_data(self):
        data = ''
        try:
            resp = self.session.get(self.url)
            resp_data = resp.text
            if resp_data != '':
                lines = resp_data.split('\n')
                count = lines.__len__()
                for i in range(count - 1):
                    line = lines[i]
                    folder = self.queue[i][0]
                    code = self.queue[i][1]
                    if '=' in line:
                        data = line.split('=')
                        result_code = data[0].split('_')[2].strip()
                        if result_code == code:
                            data = data[1]
                            data = code + '`' + data[1: -5].replace(',', '`')
                            file = self.path % (folder, code)
                            with open(file, 'a', encoding='utf-8') as f:
                                f.write(data + '\n')
                        else:
                            print('Error different stock code', 'result code:', result_code, 'code:', code)
                            pass
            time.sleep(1)
        except Exception as e:
            print(e, 'stock_data code:', code)
        return data

    def run(self):
        count = 0
        while True:
            # 判断是否开市时间
            if self.__is_open_market():
                start_time = time.clock()
                self.__crawling_data()
                count += 1
                print('Thead-' + str(self.theadID), ' crawling finish:', count, ' cost seconds:',
                      time.clock() - start_time)
            else:
                print('Thead-' + str(self.theadID), 'Market closed.')
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
