import os
import time

if __name__ == '__main__':
    while True:
        os.system('scrapy crawl --nolog sina -o ../../../temp/00001.jl')
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        time.sleep(120)
