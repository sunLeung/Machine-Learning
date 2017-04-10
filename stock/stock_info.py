import urllib.request as request
import time
import xlrd


class StockInfo:
    __sh_url = 'http://query.sse.com.cn/security/stock/downloadStockListFile.do?csrcCode=&stockCode=&areaName=&stockType=%s'
    __sh_heads = {'Referer': 'http://www.sse.com.cn/assortment/stock/list/share/'}
    __sz_url = 'http://www.szse.cn/szseWeb/ShowReport.szse?SHOWTYPE=xlsx&CATALOGID=1110&tab%sPAGENO=1&ENCODE=1&TABKEY=tab%s'
    __save_path = 'data/stock_info/%s'
    __today = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    __files = ['sh_a.xls', 'sh_b.xls', 'sz_a.xlsx', 'sz_b.xlsx']

    stock_info_dic = {}

    def __sh_a_info(self):
        url = self.__sh_url % (1)
        path = self.__save_path % (self.__files[0])
        self.__download(url, path, self.__sh_heads)
        print(self.__today, ' sh_a.xls download success')

    def __sh_b_info(self):
        url = self.__sh_url % (2)
        path = self.__save_path % (self.__files[1])
        self.__download(url, path, self.__sh_heads)
        print(self.__today, ' sh_b.xls download success')

    def __sz_a_info(self):
        url = self.__sz_url % (2, 2)
        path = self.__save_path % (self.__files[2])
        self.__download(url, path, {})
        print(self.__today, ' sz_a.xls download success')

    def __sz_b_info(self):
        url = self.__sz_url % (3, 3)
        path = self.__save_path % (self.__files[3])
        self.__download(url, path, {})
        print(self.__today, ' sz_b.xls download success')

    def __download(self, url, path, heads):
        try:
            with open(path, 'wb') as f:
                req = request.Request(url=url, headers=heads)
                response = request.urlopen(req)
                f.write(response.read())
        except Exception as e:
            print(e)

    def down_stock_info(self):
        self.__sh_a_info()
        self.__sh_b_info()
        self.__sz_a_info()
        self.__sz_b_info()

    def __read_sh_stock_info(self, file):
        path = self.__save_path % (file)
        dict = {}
        with open(path) as f:
            count = 0
            for line in f:
                if count == 0:
                    pass
                attrs = line.split('\t')
                if attrs[2].strip() != '':
                    dict[attrs[2].strip()] = attrs[1].strip()
                count += 1
        StockInfo.stock_info_dic[file] = dict

    def __read_sz_stock_info(self, file):
        path = self.__save_path % (file)
        data = xlrd.open_workbook(path)
        table = data.sheets()[0]
        nrows = table.nrows
        dict = {}
        for i in range(nrows):
            if i != 0:
                r = table.row_values(i)
                if r[5].strip() != '':
                    dict[r[5].strip()] = r[1].strip()
        StockInfo.stock_info_dic[file] = dict

    def read_stock_info(self):
        c = self.__files.__len__()
        for i in range(c):
            if i < 2:
                self.__read_sh_stock_info(self.__files[i])
            else:
                self.__read_sz_stock_info(self.__files[i])

    def auto_update(self):
        self.down_stock_info()
        self.read_stock_info()
