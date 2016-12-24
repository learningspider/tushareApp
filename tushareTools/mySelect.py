#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Created on 2016/12/24
@author: Chao Zhou
@group : Spider
@contact: 1161192890@qq.com
"""

import select,time
import socket

def mySelect():
    inputs = []
    output = []
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind('127.0.0.1',8005)
    sk.listen(5)
    while True:
        rList,w,e = select.select(inputs,[],inputs,1)
        print inputs
        print e
        time.sleep(1)
        for r in rList:
            if r == sk:
                conn , address = r.accept()
                inputs.append(conn)
                output.append(conn)
                print address
            else:
                client_data = r.recv(1024)
                if client_data:
                    r.sendall(client_data)
                else:
                    inputs.remove(r)


if __name__ == '__main__':
    mySelect()