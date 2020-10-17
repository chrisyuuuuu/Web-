day09-爬虫9

1、多线程优化
2、scrapy
    是什么？是一个非常强大的爬虫框架，框架，已经为你实现了好多功能，你只需要将你的精力放到自己的业务逻辑中即可。多进程、多线程、去重队列，框架为你实现好了，你不用管。底层语言使用python实现的，所以你可尝试看源码学习它
    安装：pip install scrapy
    认识框架
        引擎（engine）、调度器（scheduler）、爬虫（spiders）、管道（pipeline）、下载器（downloader）
    工作原理
        见百鸟朝凤图
    使用
    （1）新建工程
        scrapy startproject xxx
    （2）认识目录结构
        firstbloodpro             总的工程目录
            firstbloodpro         工程目录
                __pycache__       缓存文件
                spiders           爬虫核心目录
                    __pycache__   缓存文件
                    __init__.py   包的标记
                    lala.py       爬虫文件（*）
                __init__.py       包的标记
                items.py          定义数据结构的地方（*）
                middlewares.py    中间件（*）
                pipelines.py      管道文件（*）
                settings.py       配置文件（*）
            scrapy.cfg            工程配置文件，一般不用
    （3）新建爬虫文件
        cd firstbloodpro
        scrapy genspider 爬虫名字 爬取域名
    （4）认识爬虫文件
        见代码
    （5）启动爬虫
        cd firstbloodpro/firstbloodpro/spiders
        scrapy crawl 爬虫名字
        修改settings.py文件，修改ua和robots.txt协议
    （6）认识response对象
        response.text     字符串格式内容
        response.body     字节格式内容
        response.url      请求的url
        response.headers  响应头
        response.status   状态码
    （7）输出指定格式文件
        scrapy crawl qiubai -o qiubai.json
        scrapy crawl qiubai -o qiubai.xml
        scrapy crawl qiubai -o qiubai.csv   
        输出csv中间有空行，自己网上搜一把
4、yield item和请求
    首先定义数据结构
        这种对象直接当作字典使用，而且可以通过dict快速的转化为字典
    将item扔给管道进行处理
    爬取其它页面数据
3、scrapy shell
    是什么？是scrapy的一个终端调试工具，以后写xpath的步骤就是现在这下面调试好，然后再贴到代码中
    如何使用？
    再任意终端界面下，输入执行  scrapy shell url  即可
    特殊情况，进不去的，新建一个工程，配置好之后，再scrapy shell url 进去
    ret = response.xpath()
        ret[0].extract() === ret.extract()[0] == ret.extract_first()
    ret = response.css(选择器)
        获取属性
        ret = response.css('#content-left > div > div > a > img::attr(src)')
        获取内容
        ret = response.css('#content-left > div h2::text')
    哪个效率高呢，xpath效率高
5、日志信息和错误等级
    五个等级
    CRITICAL
    ERROR
    WARNING
    INFO
    DEBUG
    默认的级别是DEBUG
    LOG_LEVEL = 'ERROR
    LOG_FILE = 'log.txt'
6、发送post请求
    scrapy.FormRequest(url=url, formdata=xxx, callback=self.xxx)
    如果向一上来就发送post，重写一个方法  start_requests