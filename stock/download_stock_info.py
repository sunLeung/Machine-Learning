import stock.stock_info as stock_info_download

if __name__ == '__main__':
    o = stock_info_download.StockInfo()
    o.read_stock_info()
    dict = stock_info_download.StockInfo.stock_info_dic
    count = 0
    for d in dict:
        count += dict[d].__len__()
    print(count)
