import time
import requests
import asyncio
'''
单线程的协程爬取
花费时间：15.2s
'''

total = 100

async def get_page():
    url = 'http://127.0.0.1:5000/'
    future = loop.run_in_executor(None, requests.get, url)
    response = await future

if __name__ == '__main__':
    time0 = time.time()
    tasks = [asyncio.ensure_future(get_page()) for i in range(0, total)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    time1 = time.time()
    print(f"爬取{total}个网页，总共花费时间:{time1-time0:.2f}s")
