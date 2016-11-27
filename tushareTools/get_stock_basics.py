#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Created on 2016/11/25
@author: Chao Zhou
@group : Spider
@contact: 1161192890@qq.com
"""


import tushare as ts
import os
import pandas as pd
datapath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#股票名称、代码
def get_stock():
    g = ts.get_stock_basics()
    t=g['name']
    datapath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = os.path.join(datapath, 'data', 'code.cvs')
    t.to_csv(filename)
    return t

#公积金 未分配利润 净资产选股
def get_stock_basics():
    g=ts.get_stock_basics()
    datapath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = os.path.join(datapath,'data','basic.cvs')
    filetrade = os.path.join(datapath, 'data', 'trade.cvs')
    print filename
    g = g[['name','reservedPerShare','bvps','perundp']]
    g.to_csv(filename)

    ttrade = ts.get_today_all()
    ttrade = ttrade[['code','trade']]
    ttrade.to_csv(filetrade)
    g = pd.read_csv(filename)

    ttrade = pd.read_csv(filetrade)
    ttrade = ttrade[['code','trade']]
    g = pd.merge(g,ttrade,how = 'outer',on='code')
    g = g[g.trade>0]
    g['total'] = g['reservedPerShare'] + g['bvps'] + g['perundp']
    g['end'] = g['trade'] - g['total']
    #g = g.sort(['end'])
    g = g.sort_values(by='end')
    g.to_csv(filename)

    return g

#计算移动平均线
def MovingAverage():
    # 导入数据 - 注意：这里请填写数据文件在您电脑中的路径
    stock_data = pd.read_csv('stock data/sh600000.csv', parse_dates=[1])

    # 将数据按照交易日期从远到近排序
    stock_data.sort('date', inplace=True)

    # ========== 计算移动平均线

    # 分别计算5日、20日、60日的移动平均线
    ma_list = [5, 20, 60]

    # 计算简单算术移动平均线MA - 注意：stock_data['close']为股票每天的收盘价
    for ma in ma_list:
        stock_data['MA_' + str(ma)] = pd.rolling_mean(stock_data['close'], ma)

    # 计算指数平滑移动平均线EMA
    for ma in ma_list:
        stock_data['EMA_' + str(ma)] = pd.ewma(stock_data['close'], span=ma)

    # 将数据按照交易日期从近到远排序
    stock_data.sort('date', ascending=False, inplace=True)

    # ========== 将算好的数据输出到csv文件 - 注意：这里请填写输出文件在您电脑中的路径
    stock_data.to_csv('sh600000_ma_ema.csv', index=False)

if __name__ == '__main__':
    get_stock()