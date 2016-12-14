#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Created on 2016/11/25
@author: Chao Zhou
@group : Spider
@contact: 1161192890@qq.com
"""
import random,sys
#sys.setrecursionlimit(15000)
def tSort(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

def bubble_Sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j] < array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp

def insert_sort(array):
    for i in range(len(array)):
        position = i
        current_value = array[i]
        while position > 0 and current_value>array[position-1]:
            array[position] = array[position - 1]
            position = position-1
        array[position] = current_value


def quick_sort(array,start,end):
    if start >= end:
        return
    k = array[start]
    left_flag = start
    right_flag = end


    while left_flag <right_flag:
        #右边小旗子移动
        while left_flag<right_flag and array[right_flag] > k:
            right_flag -= 1
        temp = array[left_flag]
        array[left_flag] = array[right_flag]
        array[right_flag] = temp

        #左边小旗子移动
        while left_flag<right_flag and array[left_flag] <= k:
            left_flag += 1
        temp = array[left_flag]
        array[left_flag] = array[right_flag]
        array[right_flag] = temp
    quick_sort(array,start,left_flag-1)
    quick_sort(array,left_flag+1,end)


if __name__ == '__main__':
    array = [64,77,67,8,6,84,55,20,43,67]
    '''for i in range(1000):
        array.append(random.randrange(1000))'''

    print array

    quick_sort(array,0,len(array)-1)
    print array