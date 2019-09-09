import time
import requests
from multiprocessing.dummy import Pool as ThreadPool
'''
4线程爬取
花费时间：75.5s
'''

total = 10
thread_num = 4

def get_page():
    url = 'http://127.0.0.1:5000/'
    # r = requests.get(url, timeout=10)
    print(url)

def divide(i):
    for j in range(0,total//thread_num):
        get_page()

if __name__ == '__main__':
    time0 = time.time()
    i = [j for j in range(0,thread_num)]
    pool = ThreadPool(thread_num)
    pool.map(divide, i)
    pool.close()
    pool.join()
    time1 = time.time()
    print(f"爬取{total}个网页，总共花费时间:{time1-time0:.2f}s")
