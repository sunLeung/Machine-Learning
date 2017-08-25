#!/usr/local/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import metrics

keys = ['stat_time', 'ch', 'subpub', 'na', 'client_new_uv', 'client_new_pv', 'server_new_uv',
        'server_new_pv',
        'sdk_new_uv', 'daily_uv', 'boot_pv', 'boot_uv', 'login_pv', 'login_uv', 'scroll_pv', 'scroll_uv',
        'ad_exposure_uv', 'ad_click_pv', 'ad_click_uv', 'ch_enter_pv', 'ch_enter_uv', 'ch_edit_pv',
        'ch_edit_uv',
        'video_play_pv', 'video_play_uv', 'video_play_duration', 'subscription_pv', 'subscription_uv',
        'search_pv', 'search_uv', 'push_arrive_pv', 'push_arrive_uv', 'push_show_pv', 'push_show_uv',
        'push_delete_pv', 'push_delete_uv', 'push_click_pv', 'push_click_uv', 'read_pv', 'read_uv',
        'read_imei_count', 'read_duration', 'is_cheat']

# read data
# df1 = pd.read_csv('dataset/20170701-15.csv')
# df2 = pd.read_csv('dataset/20170716-31.csv')
# df3 = pd.read_csv('dataset/20170801-13.csv')
# df = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
# filter data
# sort_df = df.sort_values(axis=0, by='server_new_uv', ascending=False)


df = pd.read_csv('dataset/channel_cheat_feature.csv', delimiter='`', header=None, encoding='utf8')
df.columns = keys
df = df[df['server_new_uv'] >= 20]

positive_sample = df[df['is_cheat'] == 1]
negative_sample = df[df['is_cheat'] == 0].sample(frac=0.01)

df = pd.concat([positive_sample, negative_sample], ignore_index=True, axis=0)

data_X = df.iloc[:, 4:].as_matrix()
data_y = df.is_cheat.as_matrix()


def train1():
    # 生成训练集、预测集
    X = preprocessing.scale(data_X)
    X_train, X_test, y_train, y_test = train_test_split(X, data_y, test_size=0.3)
    knn = KNeighborsClassifier()
    knn.fit(X_train, y_train)

    # predict = knn.predict(X_test)
    print(knn.score(X_test, y_test))


def cross_validation():
    X = preprocessing.scale(data_X)
    knn = KNeighborsClassifier()
    score = cross_val_score(knn, X=X, y=data_y, cv=5, scoring='accuracy')
    print(score)


def show_data():
    data = df[df['server_new_uv'] >= 20]

    print(data[data['is_cheat'] == 1]['is_cheat'].count())
    print(data[data['is_cheat'] == 0]['is_cheat'].count())
    print(data['is_cheat'].count())


def svc_train():
    # 生成训练集、预测集
    X = preprocessing.scale(data_X)
    X_train, X_test, y_train, y_test = train_test_split(X, data_y, test_size=0.3)
    clf = SVC()
    # clf.fit(X_train, y_train)
    # score = clf.score(X_test, y_test)
    score = cross_val_score(clf, X=X, y=data_y, cv=5, scoring='accuracy')
    print(score)


def logistic_train():
    # 生成训练集、预测集
    X = preprocessing.scale(data_X)

    model = LogisticRegression()

    # 交叉验证
    # score = model.score(X_test, y_test)
    score = cross_val_score(model, X=X, y=data_y, cv=5, scoring='accuracy')
    print(score)

    # # 混淆矩阵验证
    X_train, X_test, y_train, y_test = train_test_split(X, data_y, test_size=0.6)
    model.fit(X_train, y_train)
    # y_predict = model.predict(X_test)
    # confu_ma = metrics.confusion_matrix(y_true=y_test, y_pred=y_predict)
    # recall_score = metrics.recall_score(y_true=y_test, y_pred=y_predict)
    # print(confu_ma)
    # print(recall_score)

    # 使用训练出来的模型预测全局数据
    df = pd.read_csv('dataset/channel_cheat_feature.csv', delimiter='`', header=None, encoding='utf8')
    df.columns = keys
    all_X = df.iloc[:, 4:].as_matrix()
    all_y = df.is_cheat.as_matrix()
    X1 = preprocessing.scale(all_X)
    y_predict = model.predict(X1)
    confu_ma = metrics.confusion_matrix(y_true=all_y, y_pred=y_predict, labels=[1, 0],)
    recall_score = metrics.recall_score(y_true=all_y, y_pred=y_predict)
    print(confu_ma)
    print(recall_score)


if __name__ == '__main__':
    # train1()
    # show_data()
    # cross_validation()
    # svc_train()
    logistic_train()
