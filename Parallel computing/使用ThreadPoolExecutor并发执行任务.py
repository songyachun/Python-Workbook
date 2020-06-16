"""
# @Author         : SYACHUN
# @Date           : 2020-06-16 19:25:01
# @LastEditTime: 2020-06-16 19:42:35
# @LastEditors: SYACHUN
# @Description    : 爬取网页
# @FilePath       : \weikeban\使用ThreadPoolExecutor并发执行任务.py
"""
import concurrent.futures as cf
import time
import urllib.request


def load_page(url):
    with urllib.request.urlopen(url, timeout=60) as conn:
        return ('{}主页大小：{}字节'.format(url, len(conn.read())))


if __name__ == "__main__":
    URLS = ['https://v3.bootcss.com/',
            'https://www.cnblogs.com/', 'http://www.baidu.com/']
    start_time = time.time()
    for url in URLS:
        print(load_page(url))
    end_time = time.time()
    print('串行处理消耗时间：{}'.format(end_time-start_time))
    # 使用ThreadPoolExecutor并发处理
    start_time = time.time()
    executor = cf.ThreadPoolExecutor()
    wait_for = [executor.submit(load_page, url) for url in URLS]
    for f in cf.as_completed(wait_for):
        print(f.result())
    end_time = time.time()
    print("并发处理消耗时间：{}".format(end_time-start_time))
