#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Created on 2016/11/25
@author: Chao Zhou
@group : Spider
@contact: 1161192890@qq.com
"""

class TreeNode(object):
    def __init__(self,data=0,left=0,right=0):
        self.data = data
        self.left = left
        self.right = right


class BTree(object):
    def __init__(self,root=0):
        self.root = root

    def preOrder(self,treenode):
        if treenode is 0:
            return
        print treenode.data
        self.preOrder(treenode.left)
        self.preOrder(treenode.ritht)

    def inOrder(self,treenode):
        if treenode is 0:
            return
        self.inOrder(treenode.left)
        print treenode.data
        self.inOrder(treenode.right)

    def postOrder(self,treenode):
        if treenode is 0:
            return
        self.postOrder(treenode.left)
        self.postOrder(treenode.right)
        print treenode.data

if __name__ == '__main__':
    pass
