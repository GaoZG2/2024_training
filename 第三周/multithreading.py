import requests
from threading import Thread

# 定义下载函数
def download_html(url):
    try:
        response = requests.get(url)

        # 如果请求失败，抛出异常
        response.raise_for_status()

        # 打印获取到的HTML数据
        print(response.text, end='\n\n')
    except requests.RequestException as e:
        print(f"请求错误：{e}", end='\n\n')

# html资源URL
url = 'https://www.baidu.com'

# 创建线程并启动
threads = []
for i in range(3):  # 创建3个线程
    t = Thread(target=download_html, args=(url,))
    threads.append(t)
    t.start()

# 等待所有线程执行完毕
for t in threads:
    t.join()
