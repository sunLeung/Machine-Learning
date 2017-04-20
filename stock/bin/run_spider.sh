#!/bin/bash

# Author: yxleung
# Email: liangyuxin.02@gmail.com
# Date: 2017-04-17
# Description: 启动爬虫程序

current_date=`date +%Y%m%d`
echo $current_date
PYTHON3 = /Library/Frameworks/Python.framework/Versions/3.6/bin:/usr/local/bin
PATH=$PATH:PYTHON3
echo $PATH
echo `python3 --version`
cd /Users/leungyuxin/PycharmProjects/Machine-Learning/stock/src/download/
nohup python3 -u main.py > ../../logs/current_date.log&
