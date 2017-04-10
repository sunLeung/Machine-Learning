import scrapy
import json


class SinaSpider(scrapy.Spider):
    name = "sina"

    def start_requests(self):
        urls = [
            'http://vip.stock.finance.sina.com.cn/quotes_service/api/jsonp.php/var%20moneyFlowData=/MoneyFlow.ssi_ssfx_flzjtj?daima=sz000001&gettime=1']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        text = str(response.body)
        tmp_str = text.split('moneyFlowData')[1][4:-3]
        data = {}
        for attr in tmp_str.split(','):
            attr_ = attr.split(':')
            if (attr_[0] == 'ticktime'):
                data[attr_[0]] = attr_[1][1:] + ':' + attr_[2] + ':' + attr_[3][:-1]
            else:
                data[attr_[0]] = attr_[1][1:-1]
        return data
