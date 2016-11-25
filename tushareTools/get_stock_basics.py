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

def get_stock_basics():
    g=ts.get_stock_basics()
    datapath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r'\data\cvs'
    g.to_csv(datapath)
    return g

if __name__ == '__main__':
    get_stock_basics()