#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Created on 2017/1/2
@author: Chao Zhou
@group : Spider
@contact: 1161192890@qq.com
"""

import contextlib,threading
from Queue import Queue
#import twisted.python.threadpool

workerStop = object()

class ThreadPool():
    workers = 0
    threadFactory = threading.Thread
    currentThread = staticmethod(threading.current_thread)
    def __init__(self,maxthreads=20,name=None):
        self.q = Queue(0)
        self.max = maxthreads
        self.name = name
        self.waiters = []
        self.working = []

    def start(self):
        while self.workers < min(self.max,self.q.qsize()):
            self.startAWorker()

    def startAWorker(self):
        self.workers +=1
        name = 'PoolThread-%s-%s' % (self.name or id(self), self.workers)
        newThread = self.threadFactory(target=self._worker, name = name)
        newThread.start()

    def callInThread(self,func,*args,**kw):
        self.callInThreadWithCallback(None,func,*args,**kw)

    def callInThreadWithCallback(self,onResult,func,*args,**kw):
        o = (func,args,kw,onResult)
        self.q.put(o)

    @contextlib.contextmanager
    def _workerState(self,stateList,workerThread):
        stateList.append(workerThread)
        try:
            yield
        finally:
            stateList.remove(workerThread)

    def _worker(self):
        ct = self.currentThread()
        o = self.q.get()
        while o is not workerStop:
            with self._workerState(self.working,ct):
                function,args,kwargs,onResult = o
                del o
                try:
                    result = function(*args,**kwargs)
                    success = True
                except:
                    success = False
                    if onResult is None:
                        pass
                    else:
                        pass
                del function,args,kwargs

                if onResult is not None:
                    try:
                        onResult(success,result)
                    except:
                        pass

                del onResult,result

            with self._workerState(self.waiters,ct):
                o = self.q.get()

    def stop(self):
        while self.workers:
            self.q.put(workerStop)
            self.workers -=1




if __name__ == '__main__':
    def onResult(status, result):
        # status, execute action status
        # result, execute action return value
        pass

    def show(arg):
        import time
        time.sleep(1)
        print arg

    pool = ThreadPool(20)

    for i in range(500):
        pool.callInThread(show,i)

    pool.start()
    pool.stop()