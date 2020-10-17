import threading
import requests
import time
from lxml import etree
from queue import Queue
import json

class CrawlThread(threading.Thread):
    def __init__(self, crawl_name, page_queue, data_queue):
        super().__init__()
        self.name = crawl_name
        self.page_queue = page_queue
        self.url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,{}.html'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        self.data_queue = data_queue
    
    def run(self):
        '''
        1、从页码队列取出一个页码
        2、拼接url
        3、发送请求，得到响应
        4、将响应放入数据队列里面
        '''
        while 1:
            page = self.page_queue.get()
            url = self.url.format(page)
            r = requests.get(url=url, headers=self.headers)
            self.data_queue.put(r.text)
            # 循环的退出条件

class ParseThread(threading.Thread):
    def __init__(self, parse_name, data_queue, fp, lock):
        super().__init__()
        self.name = parse_name
        self.data_queue = data_queue
        self.fp = fp
        self.lock = lock
    
    def run(self):
        '''
        1、从数据队列取出数据
        2、解析并且保存文件
        '''
        while 1:
            content = self.data_queue.get()
            self.parse_content(content)
            # 写循环的退出条件
    
    def parse_content(self, content):
        # 解析
        item = {
            '职位名称': 'lala',
            '公司名称': 'dudu',
        }
        string = json.dumps(item, ensure_ascii=False)
        # 如果加锁成功，再去写
        if self.lock.acquire():
            self.fp.write(string + '\n')
            self.lock.release()

# 创建队列函数
def create_queue():
    page_queue = Queue()
    # 放入待爬取的页码
    for page in range(1, 11):
        page_queue.put(page)
    data_queue = Queue()
    return page_queue, data_queue

def main():
    fp = open('lala.txt', 'w', encoding='utf8')
    lock = threading.Lock()
    # 创建队列
    page_queue, data_queue = create_queue()
    # 创建一个列表，用来保存所有的采集线程
    crawl_thread_list = []
    parse_thread_list = []
    # 这是主线程，创建好多子线程
    # 创建3个采集线程
    crawl_name_list = ['采集线程1', '采集线程2', '采集线程3']
    for crawl_name in crawl_name_list:
        # 创建线程，并且给线程起名字
        tcrawl = CrawlThread(crawl_name, page_queue, data_queue)
        # 启动线程
        tcrawl.start()
        # 将线程保存起来
        crawl_thread_list.append(tcrawl)
    
    # 创建3个解析线程
    parse_name_list = ['解析线程1', '解析线程2', '解析线程3']
    for parse_name in parse_name_list:
        # 创建线程，并且给线程起名字
        tparse = ParseThread(parse_name, data_queue, fp, lock)
        # 启动线程
        tparse.start()
        # 将线程保存起来
        parse_thread_list.append(tparse)
    
    # 让主线程等待
    for tcrawl in crawl_thread_list:
        tcrawl.join()
    for tparse in parse_thread_list:
        tparse.join()
    
    fp.close()
    print('主线程-子线程全部结束')

if __name__ == "__main__":
    main()