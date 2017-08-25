#!/usr/local/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import datetime
import os


def clean_data():
    # read data
    df1 = pd.read_csv('dataset/20170701-15.csv')
    df2 = pd.read_csv('dataset/20170716-31.csv')
    df3 = pd.read_csv('dataset/20170801-13.csv')
    df = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
    # filter data
    # sort_df = df.sort_values(axis=0, by='server_new_uv', ascending=False)

    begin = datetime.date(2017, 7, 1)
    end = datetime.date(2017, 8, 13)

    d = begin
    delta = datetime.timedelta(days=1)
    while d <= end:
        str_date = d.strftime('%Y-%m-%d')
        tmp = df[df.stat_time == str_date]
        tmp = tmp.drop(['stat_time', 'str'], axis=1, inplace=False)
        tmp = tmp.groupby(['ch', 'subpub', 'na']).sum().reset_index()
        tmp[tmp.is_cheat == 2] = 1
        tmp.to_csv('output/' + str_date + '.csv', index=False, header=False,encoding='UTF8')
        print(str_date + ' success')
        d += delta


in_path = 'D:/odps/imei'
out_path = 'output/'

odps_clt_bin = 'D:/installed/odps_clt_release_64/bin/odpscmd.bat'

odps_cmd_base = odps_clt_bin + ' --project kpi_control_dev -e "%s"';

table = 'intl_ucnews_channel_feature'


def upload_odps(file, table):
    print('=======upload==========')
    cmd = odps_cmd_base % ('tunnel upload %s %s -dbr true')
    cmd = cmd % (file, table)
    print(cmd)
    r = os.system(cmd)
    print(r)


def create_partition(table, partition):
    print('=======create==========')
    cmd = odps_cmd_base % ("alter table %s add partition (dt='%s')")
    cmd = cmd % (table, partition)
    print(cmd)
    r = os.system(cmd)
    print(r)


def drop_partition(table, partition):
    print('=======drop==========')
    cmd = odps_cmd_base % ("alter table %s DROP IF EXISTS PARTITION (dt='%s')")
    cmd = cmd % (table, partition)
    print(cmd)
    r = os.system(cmd)
    print(r)


def upload():
    dt_dir = os.listdir(out_path)
    for dt in dt_dir:
        dt = dt.split('.')[0]
        print(dt)
        drop_partition(table, dt)
        create_partition(table, dt)
        data_path = out_path + '/' + dt + '.csv'
        upload_odps(data_path, table + '/dt=' + dt)


if __name__ == '__main__':
    upload()
    # clean_data()
# df.drop(['str', 'stat_time'], axis=1, inplace=True)
#
# print(df.columns)
