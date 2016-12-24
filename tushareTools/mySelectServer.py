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
import Queue

def mySelect():
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sk.setblocking(False)
    sk.bind('127.0.0.1',8005)
    sk.listen(10)

    inputs = [sk,]
    output = []
    message = {}

    while True:
        rList,wList,e = select.select(inputs,output,inputs,1)
        print inputs
        print e
        time.sleep(1)
        for r in rList:
            if r == sk:
                conn , address = r.accept()
                inputs.append(conn)
                message[conn] = Queue.Queue()
                print address
            else:
                client_data = r.recv(1024)
                if client_data:
                    output.append(r)
                    message[r].put(client_data)
                else:
                    inputs.remove(r)
                '''
                if client_data:
                    r.sendall(client_data)
                else:
                    inputs.remove(r)
                '''

        for w in wList:
            try:
                data = message[w].get_nowait(client_data)
                w.sendall(data)
            except Queue.Empty:
                output.remove(w)
            output.remove(w)
            del message[w]




if __name__ == '__main__':
    mySelect()