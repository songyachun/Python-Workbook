# -*-coding=utf-8-*-
"""
# Author       : SYACHUN
# Date         : 2020-04-07 14:33:42
# LastEditTime: 2020-04-18 21:58:22
# LastEditors: SYACHUN
# FilePath     : \Python-Workbook\Data Structures and Algorithms\Chaper 4 递归\4-5文件系统的使用情况.py
# Description  : 
"""


import os


def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            # print('childpath=', childpath)
            total += disk_usage(childpath)
    print('{0:7}'.format(total), path)
    return total


if __name__ == "__main__":
    patha = r'D:\Desktop\Python-Workbook'
    disk_usage(patha)
