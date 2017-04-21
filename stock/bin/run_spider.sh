#!/bin/bash

# Author: yxleung
# Email: liangyuxin.02@gmail.com
# Date: 2017-04-17
# Description: 启动爬虫程序

current_date=`date +%Y%m%d%H`
PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"
export PATH
cd /Users/leungyuxin/PycharmProjects/Machine-Learning/stock/src/download/
nohup python3 -u main.py > ../../logs/${current_date}.log&
