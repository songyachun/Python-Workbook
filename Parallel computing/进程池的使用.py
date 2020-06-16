"""
# @Author         : SYACHUN
# @Date           : 2020-06-16 17:11:11
# @LastEditTime: 2020-06-16 18:59:08
# @LastEditors: SYACHUN
# @Description    : 
# @FilePath       : \weikeban\进程池的使用.py
"""
from multiprocessing import Pool, TimeoutError
import time
import os


def f(x):
    return x*x


if __name__ == "__main__":
    with Pool(processes=4) as pool:
        res1 = pool.map(f, range(10))
        print("pool.map的结果：{}".format(res1))
        res2 = pool.apply_async(f, (20,))
        print(res2.get(timeout=1))
        res3 = pool.apply_async(os.getpid, ())
        print(res3.get(timeout=1))
        res4 = pool.apply_async(time.sleep, (10,))
        try:
            print(res4.get(timeout=1))
        except TimeoutError:
            print("结果超时")
        res5 = [pool.apply_async(os.getpid, ()) for i in range(5)]
        print([res.get(timeout=1) for res in res5])
        print("在With语句中，进程池可用")
    print("在With语句之外，进程池自动关闭，不再可用")
