#!/usr/local/bin/python
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

# wa_file = pd.read_csv("dataset/wa_channel_cheat_feature.txt", sep="`|=", header=None, engine='python')
#
# df2 = wa_file.ix[:, 1::2]
# df2.columns = list(wa_file.ix[0, 0::2])
# print(df2.head())
keys = ['stat_time=', 'ch=', 'subpub=', 'na=', 'client_new_uv=', 'client_new_pv=', 'server_new_uv=',
        'server_new_pv=',
        'sdk_new_uv=', 'daily_uv=', 'boot_pv=', 'boot_uv=', 'login_pv=', 'login_uv=', 'scroll_pv=', 'scroll_uv=',
        'ad_exposure_uv=', 'ad_click_pv=', 'ad_click_uv=', 'ch_enter_pv=', 'ch_enter_uv=', 'ch_edit_pv=',
        'ch_edit_uv=',
        'video_play_pv=', 'video_play_uv=', 'video_play_duration=', 'subscription_pv=', 'subscription_uv=',
        'search_pv=', 'search_uv=', 'push_arrive_pv=', 'push_arrive_uv=', 'push_show_pv=', 'push_show_uv=',
        'push_delete_pv=', 'push_delete_uv=', 'push_click_pv=', 'push_click_uv=', 'read_pv=', 'read_uv=',
        'read_imei_count=', 'read_duration=', 'is_cheat=']


def convert_to_csv():
    outfile = open("dataset/channel_cheat_feature.csv", mode='w', encoding='utf8')
    with open("dataset/wa_channel_cheat_feature.txt", encoding='utf8') as f:
        i = 1
        for line in f:
            i += 1
            for key in keys:
                line = line.replace(key, '')
            outfile.write(line)
            print(i)
    outfile.close()


def convert_to_odps():
    df = pd.read_csv('dataset/channel_cheat_feature.csv', delimiter='`')
    df.columns = keys

    date_list = df['stat_time='].unique()
    for str_date in date_list:
        tmp = df[df['stat_time='] == str_date]
        tmp = tmp.drop(['stat_time='], axis=1, inplace=False)
        tmp.to_csv('output/' + str_date + '.csv', index=False, header=False, encoding='UTF8')
        print(str_date + ' success')


if __name__ == '__main__':
    convert_to_csv()
    # convert_to_odps()
