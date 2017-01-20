#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Created on 2017/01/20
@author: Chao Zhou
@group : Spider
@contact: 1161192890@qq.com
"""

import re,os,crypt
from tushareTools import threadPool
class hackLinuxPW():

    def __init__(self,dictFile,user,pwd):
        self.user = user
        self.dictFile = dictFile
        self.pwd = pwd
        self.salt = re.search('\$(\w+)\$(\w+)\$',pwd).group()
        # self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # self.data_dir = os.path.join(self.BASE_DIR,'data')
        self.testPass(self.pwd)

    def comparePass(self,pw):
        cryptWord = crypt.crypt(pw, self.salt)
        if (cryptWord == self.pwd):
            print '[+] Found Password: ' + pw + '\n'
        print 'compare once!'



    def testPass(self,pw):
        pool = threadPool.ThreadPool(20)
        pool.start()
        with open(self.dictFile) as f:
            for line in f:
                line = line.strip('\n')
                pool.callInThread(self.comparePass(),line)


        print "[-]Password not found.\n"
        pool.stop()






if __name__ == '__main__':
    hackLinuxPW(r'D:\tushareApp\data\dictpasswd','root','$6$HqfT0spQ$S4I6WjbP0DCg3OrtSqUuBTWIGA7/BsVg1G9svm2sEHE/bdO03lOqk/6O4J0BFCi5.vLgDnVZBiFchzUdZojQt/')