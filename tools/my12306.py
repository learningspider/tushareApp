#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Created on 2017/01/25
@author: Chao Zhou
@group : Spider
@contact: 1161192890@qq.com
"""
import urllib,urllib2,json,ssl,requests,re

def login12306():
    login_html = 'https://kyfw.12306.cn/otn/login/init'
    login_dict = {
        'username': "用户名",
        'pwd': "密码",
        'imgcode': "",
        'f': 'json'
    }
    login_res = requests.post(
        url="https://mp.weixin.qq.com/cgi-bin/login?lang=zh_CN",
        data=login_dict,
        headers={'Referer': 'https://mp.weixin.qq.com/cgi-bin/login?lang=zh_CN'})

    # 登陆成功之后获取服务器响应的cookie
    resp_cookies_dict = login_res.cookies.get_dict()
    # 登陆成功后，获取服务器响应的内容
    resp_text = login_res.text
    # 登陆成功后，获取token
    token = re.findall(".*token=(\d+)", resp_text)[0]

    return {'token': token, 'cookies': resp_cookies_dict}

def getlist():
    flag = False

    # ssl._create_default_https_context = ssl._create_unverified_context()  # 关闭证书验证
    # req = urllib.urlopen(r'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2017-01-31&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=CDW&purpose_codes=ADULT',context=ssl._create_default_https_context)

    req = requests.get('https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2017-01-31&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=CDW&purpose_codes=ADULT',verify=False)
    html = req.text
    # html = req.read()
    print html
    dict_html = json.loads(html)
    print dict_html
    dict_html = dict_html['data']
    while not flag:
        for i in dict_html:
            yp =  i['queryLeftNewDTO']['yw_num']
            print yp
            if yp !=u'无' and yp != '--':
                print 'wu'
                flag = True
                break
            else:
                print '暂时无票，继续等待！'

if __name__ == '__main__':
    getlist()
