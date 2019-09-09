import time
import requests
from multiprocessing.dummy import Pool as ThreadPool
'''
4线程的协程爬取
花费时间：
运行有bug
'''
thread_num = 4
total = 100

async def get_page(loop):
    url = 'http://127.0.0.1:5000'
    future = loop.run_in_executor(None, requests.get, url)
    response =  await future

def divide(i):
    import asyncio
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)
    tasks = [asyncio.ensure_future(get_page(loop)) for j in range(total//thread_num)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == '__main__':
    time0 = time.time()
    pool = ThreadPool(thread_num)
    i = [j for j in range(thread_num)]
    pool.map(divide, i)
    pool.close()
    pool.join()
    time1 = time.time()
    print(f"爬取{total}个网页，总共花费时间:{time1-time0:.2f}s")
