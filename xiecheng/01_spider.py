import requests
import time
'''
普通爬取，花费时间300s
'''

total = 100

def get_page():
    url = 'http://127.0.0.1:5000/'
    r = requests.get(url, timeout=10)

if __name__ == '__main__':
    time0 = time.time()
    for i in range(total):
        get_page()
    time1 = time.time()
    print(f"爬取{total}个网页，总共花费时间:{time1-time0:.2f}s")
