day09-����9

1�����߳��Ż�
2��scrapy
    ��ʲô����һ���ǳ�ǿ��������ܣ���ܣ��Ѿ�Ϊ��ʵ���˺ö๦�ܣ���ֻ��Ҫ����ľ����ŵ��Լ���ҵ���߼��м��ɡ�����̡����̡߳�ȥ�ض��У����Ϊ��ʵ�ֺ��ˣ��㲻�ùܡ��ײ�����ʹ��pythonʵ�ֵģ�������ɳ��Կ�Դ��ѧϰ��
    ��װ��pip install scrapy
    ��ʶ���
        ���棨engine������������scheduler�������棨spiders�����ܵ���pipeline������������downloader��
    ����ԭ��
        �����񳯷�ͼ
    ʹ��
    ��1���½�����
        scrapy startproject xxx
    ��2����ʶĿ¼�ṹ
        firstbloodpro             �ܵĹ���Ŀ¼
            firstbloodpro         ����Ŀ¼
                __pycache__       �����ļ�
                spiders           �������Ŀ¼
                    __pycache__   �����ļ�
                    __init__.py   ���ı��
                    lala.py       �����ļ���*��
                __init__.py       ���ı��
                items.py          �������ݽṹ�ĵط���*��
                middlewares.py    �м����*��
                pipelines.py      �ܵ��ļ���*��
                settings.py       �����ļ���*��
            scrapy.cfg            ���������ļ���һ�㲻��
    ��3���½������ļ�
        cd firstbloodpro
        scrapy genspider �������� ��ȡ����
    ��4����ʶ�����ļ�
        ������
    ��5����������
        cd firstbloodpro/firstbloodpro/spiders
        scrapy crawl ��������
        �޸�settings.py�ļ����޸�ua��robots.txtЭ��
    ��6����ʶresponse����
        response.text     �ַ�����ʽ����
        response.body     �ֽڸ�ʽ����
        response.url      �����url
        response.headers  ��Ӧͷ
        response.status   ״̬��
    ��7�����ָ����ʽ�ļ�
        scrapy crawl qiubai -o qiubai.json
        scrapy crawl qiubai -o qiubai.xml
        scrapy crawl qiubai -o qiubai.csv   
        ���csv�м��п��У��Լ�������һ��
4��yield item������
    ���ȶ������ݽṹ
        ���ֶ���ֱ�ӵ����ֵ�ʹ�ã����ҿ���ͨ��dict���ٵ�ת��Ϊ�ֵ�
    ��item�Ӹ��ܵ����д���
    ��ȡ����ҳ������
3��scrapy shell
    ��ʲô����scrapy��һ���ն˵��Թ��ߣ��Ժ�дxpath�Ĳ������������������Ժã�Ȼ��������������
    ���ʹ�ã�
    �������ն˽����£�����ִ��  scrapy shell url  ����
    �������������ȥ�ģ��½�һ�����̣����ú�֮����scrapy shell url ��ȥ
    ret = response.xpath()
        ret[0].extract() === ret.extract()[0] == ret.extract_first()
    ret = response.css(ѡ����)
        ��ȡ����
        ret = response.css('#content-left > div > div > a > img::attr(src)')
        ��ȡ����
        ret = response.css('#content-left > div h2::text')
    �ĸ�Ч�ʸ��أ�xpathЧ�ʸ�
5����־��Ϣ�ʹ���ȼ�
    ����ȼ�
    CRITICAL
    ERROR
    WARNING
    INFO
    DEBUG
    Ĭ�ϵļ�����DEBUG
    LOG_LEVEL = 'ERROR
    LOG_FILE = 'log.txt'
6������post����
    scrapy.FormRequest(url=url, formdata=xxx, callback=self.xxx)
    �����һ�����ͷ���post����дһ������  start_requests