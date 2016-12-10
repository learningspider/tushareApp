#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Created on 2016/11/25
@author: Chao Zhou
@group : Spider
@contact: 1161192890@qq.com
"""
import random

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


def quick_sort(array):
    k = array[0]
    left_flag = 0
    right_flag = len(array) - 1


    while left_flag <right_flag:
        #右边小旗子移动
        while array[right_flag] > k:
            right_flag -= 1
        temp = array[left_flag]
        array[left_flag] = array[right_flag]
        array[right_flag] = temp

        #左边小旗子移动
        while array[left_flag] < k:
            right_flag += 1
        temp = array[left_flag]
        array[left_flag] = array[right_flag]
        array[right_flag] = temp



if __name__ == '__main__':
    array = [472, 923, 946, 546, 804, 285, 6, 230, 882, 390, 196, 609, 604, 19, 602, 638, 414, 118, 993, 581]
    ''' i in range(20):
        array.append(random.randrange(1000))'''

    print array

    quick_sort(array)
    print array