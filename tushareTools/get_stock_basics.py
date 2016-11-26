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

#股票名称、代码
def get_stock():
    g = ts.get_stock_basics()
    t=g['name']
    datapath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = os.path.join(datapath, 'data', 'code.cvs')
    t.to_csv(filename)
    return t

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
    g['total'] = g['reservedPerShare'] + g['bvps'] + g['perundp']
    g['end'] = g['trade'] - g['total']
    g = g.sort(['end'])
    g.to_csv(filename)

    return g

if __name__ == '__main__':
    get_stock()