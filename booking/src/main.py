#!/usr/bin/python3
# -*- coding:utf-8 -*-

import requests
import random
import hashlib
from PIL import Image
from lxml import etree
from io import BytesIO
import os

# 用户资料
user_name = "身份证"
pwd = "密码"

# 番禺中心医院
his_cd = 1018
# 产科门诊
dep_id = 1005
# 医生ID
doc_map = {
    '廖乐君': '0864',
    '张建丽': '0276',
    '蒋静文': '2525',
    '陈烨': '2640',
    '何婧': '2876'
}

session = requests.session()


def login():
    url = 'http://www.guahao.gov.cn/logined.xhtml?r=' + "%.17f" % (random.uniform(0, 1))

    header = {
        'Accept': 'application/json, text/javascript, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,ko;q=0.6,en;q=0.4,zh-TW;q=0.2,ja;q=0.2',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'www.guahao.gov.cn',
        'Origin': 'http://www.guahao.gov.cn',
        'Referer': 'http://www.guahao.gov.cn/doctorslist.xhtml?HIS_CD=1018&DEP_ID=1005',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    m = hashlib.md5()
    m.update(pwd.encode("utf-8"))
    form_data = {
        'CARD_NO': user_name,
        'CARD_TYP': 1,
        'PWD': m.hexdigest()
    }

    # login and keep cookies
    session.post(headers=header, data=form_data, url=url)

    resp = session.post(headers=header, data=form_data, url=url)
    resp_data = resp.json()
    if (resp.status_code == 200):
        print("Login success")
    else:
        print(resp_data)
        print(resp_data['GWA']['MSG_DAT'])


def appointment(doc_name, date, t):
    url = 'http://www.guahao.gov.cn/ajx_regtime.xhtml'
    if (not doc_name in doc_map.keys()):
        print(("找不到%s医生" % (doc_name)))
        return
    doc_id = doc_map[doc_name]
    params = {
        'HIS_CD': his_cd,
        'DEP_ID': dep_id,
        'DOC_ID': doc_id,
        'DOC_NM': '',
        'REG_DAT': date,
        'TM_FLG': 2,
        'REG_FEE': 100,
        'TRE_FEE': 600,
        'STA_TM': '',
        'END_TM': ''
    }
    resp = session.get(url=url, params=params)
    print(resp.url)
    # 解析数据
    dom_tree = etree.HTML(resp.text)
    trs = dom_tree.xpath('/html/body/table/tbody/tr')
    xpath = ''
    if (t == 'show'):
        xpath = '//td/text()|//td/b/text()|//td/a/text()'
    elif (t == 'get'):
        xpath = '//td/text()|//td/b/text()|//td/a/text()'
    data = trs[0].xpath(xpath)
    result = []
    for index in range(len(data)):
        data[index] = str(data[index]).strip()
        if (data[index] != ''):
            result.append(data[index])
    appointment = []
    tmp = []
    for index in range(len(result)):
        if (index % 4 == 0 and index > 0):
            appointment.append(tmp)
            tmp = []
        tmp.append(result[index])
        if (index == len(result) - 1):
            appointment.append(tmp)
    return appointment


def getappointment(doc_name, date, sta_tm, end_tm):
    url = 'http://www.guahao.gov.cn/reg_confirm.xhtml'
    if (not doc_name in doc_map.keys()):
        print(("找不到%s医生" % (doc_name)))
        return
    doc_id = doc_map[doc_name]
    params = {
        'HIS_CD': 1018,
        'DEP_ID': 1005,
        'DOC_ID': doc_id,
        'DOC_NM': '',
        'REG_DAT': date,
        'TM_FLG': 2,
        'REG_FEE': 100,
        'TRE_FEE': 600,
        'STA_TM': sta_tm,
        'END_TM': end_tm
    }
    resp = session.get(url=url, params=params)
    dom_tree = etree.HTML(resp.text)
    regForm = dom_tree.xpath('//form[@name="regForm"]')
    div_code = dom_tree.xpath('//img[@id="divCode"]/@src')[0]
    code = image_tostring("http://www.guahao.gov.cn" + div_code)
    print(code)
    data = {
        'token': regForm[0].xpath('//input[@id="token"]/@value')[0],
        'YB_CHK_FLG': regForm[0].xpath('//input[@id="YB_CHK_FLG"]/@value')[0],
        'REG_FLG': regForm[0].xpath('//input[@id="REG_FLG"]/@value')[0],
        'REG_PAY_TYP': regForm[0].xpath('//input[@id="REG_PAY_TYP"]/@value')[0],
        'HIS_CD': regForm[0].xpath('//input[@id="HIS_CD"]/@value')[0],
        'DEP_ID': regForm[0].xpath('//input[@id="DEP_ID"]/@value')[0],
        'DEP_NM': regForm[0].xpath('//input[@id="DEP_NM"]/@value')[0],
        'DOC_ID': regForm[0].xpath('//input[@id="DOC_ID"]/@value')[0],
        'DOC_NM': regForm[0].xpath('//input[@id="DOC_NM"]/@value')[0],
        'REG_DAT': regForm[0].xpath('//input[@id="REG_DAT"]/@value')[0],
        'TIM_FLG': regForm[0].xpath('//input[@id="TIM_FLG"]/@value')[0],
        'STA_TIM': regForm[0].xpath('//input[@id="STA_TIM"]/@value')[0],
        'END_TIM': regForm[0].xpath('//input[@id="END_TIM"]/@value')[0],
        'REG_FEE': regForm[0].xpath('//input[@id="REG_FEE"]/@value')[0],
        'TRE_FEE': regForm[0].xpath('//input[@id="TRE_FEE"]/@value')[0],
        'VER_ID': code,
        'OPE_SEX': regForm[0].xpath('//input[@id="opeSex"]/@value')[0],
        'OPE_IDC': regForm[0].xpath('//input[@id="opeIdc"]/@value')[0],
        'CONN_NO': regForm[0].xpath('//input[@id="connNo"]/@value')[0],
        'CONN_TYP': regForm[0].xpath('//input[@id="connTyp"]/@value')[0],
        'CONN_BIRTH_DT': regForm[0].xpath('//input[@id="connBirthDt"]/@value')[0],
        'GRAVIDAFLAG': regForm[0].xpath('//input[@id="gravidFlag"]/@value')[0],
        'SUCKLEFLAG': regForm[0].xpath('//input[@id="suckleFlag"]/@value')[0]
    }
    print(data)
    # 挂号动作
    url = 'http://www.guahao.gov.cn/guahao.xhtml'
    resp = session.post(url=url, data=data)
    json = resp.json()
    print(json['GWA']['ERR'][0]['MSG_INF'])
    print(resp.json())


def image_tostring(url):
    # 生成验证码
    params = {
        'r':"%.17f" % (random.uniform(0, 1))
    }
    resp = session.get(url,params=params)
    i = Image.open(BytesIO(resp.content))
    i.save('image.png')
    # 调用tesseract shell
    binPath = os.path.abspath('..') + ('/bin/Tesseract-OCR/')
    command = ('%stesseract.exe image.png tmp') % (binPath)
    os.system(command)
    file = open('tmp.txt')
    code = file.read().strip()
    file.close()
    os.remove('tmp.txt')
    os.remove('image.png')
    return code


if __name__ == '__main__':
    login()
    # # print(appointment('何婧', '2017-07-06','show'))
    getappointment('张建丽', '2017-07-11', '15:00', '16:00')
