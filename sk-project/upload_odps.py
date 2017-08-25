#!/usr/local/bin/python
# -*- coding:utf-8 -*-
import os

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