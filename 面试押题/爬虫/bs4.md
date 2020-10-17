import urllib.request
from bs4 import BeautifulSoup
import time
import pymysql

# 拼接url，并且生成请求对象
def handle_request(url, keyword, page):
    url = url.format(keyword, page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request

# 解析并且保存内容
def parse_content(content, db, cursor):
    # 生成soup对象
    soup = BeautifulSoup(content, 'html5lib')
    # 解析内容
    # 首先找到包含工作的所有的div列表
    # 数一数，一页应该50个
    # 先去找到包含所有工作的div
    odiv = soup.find('div', id='resultList')
    div_list = odiv.find_all('div', class_='el')[1:]
    # print(len(div_list))
    # 遍历这个列表，依次获取工作的每个信息
    for div in div_list:
        # 得到职位名称
        jobname = div.select('.t1 > span > a')[0]['title']
        # 得到公司名称
        company = div.select('.t2 > a')[0]['title']
        # 得到工作地点
        area = div.select('.t3')[0].string
        # 得到薪资水平
        salary = div.select('.t4')[0].string
        # 得到发布时间
        publish_time = div.select('.t5')[0].string
        # print(company, area, salary, publish_time)
        # 将这些信息都放到字典中
        item = {
            'jobname': jobname,
            'company': company,
            'area': area,
            'salary': salary,
            'publish_time': publish_time
        }
        # 将item字典写到文件中
        # string = str(item)
        # fp.write(string + '\n')

        # 将数据写入数据库
        save_to_mysql(item, db, cursor)

# 保存到数据库中的函数
def save_to_mysql(item, db, cursor):
    # 拼接sql语句
    sql = """insert into work(jobname, company, area, salary, publish_time) values('%s', '%s', '%s', '%s', '%s')""" % (item['jobname'], item['company'],item['area'], item['salary'], item['publish_time'])
    # 执行sql语句
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

# 链接数据库函数, 返回游标
def connect_mysql():
    db = pymysql.connect(host='47.94.192.240', port=3306, user='root', password='zzcno123', db='job', charset='utf8')
    cursor = db.cursor()
    return db, cursor

def main():
    # 让用户输入要爬取的关键字
    keyword = input('请输入要爬取的关键字-')
    # 输入起始页码和结束页码
    start_page = int(input('请输入起始页码-'))
    end_page = int(input('请输入结束页码-'))
    # 最原始的url就是
    url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,{},2,{}.html'

    # 打开文件
    # fp = open('work.txt', 'w')
    db, cursor = connect_mysql()

    # 写循环，依次爬取每一页的工作信息
    for page in range(start_page, end_page + 1):
        print('正在爬取第--%s--页。。。。。。' % page)
        # 根据page和url拼接每一页的url，并且生成请求对象
        request = handle_request(url, keyword, page)
        # 发送请求，得到响应
        content = urllib.request.urlopen(request).read().decode('gbk')
        # 解析响应
        # 保存到文件中
        # parse_content(content, fp)
        # 保存到数据库中
        parse_content(content, db, cursor)
        print('结束爬取第--%s--页' % page)
        time.sleep(3)
    
    # 关闭文件
    # fp.close()

    # 关闭数据库
    cursor.close()
    db.close()

if __name__ == '__main__':
    main()