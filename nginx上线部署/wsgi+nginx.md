# django自带的服务器性能有点低，uwsgi
### 1.安装  - 有nginx模块，和nginx无缝对接
    - pip install uwsgi
### 2.配置uwsgi.ini
	```
	  [uwsgi]
	  # 使用nginx连接时，使用
	  socket= 127.0.0.1:8000
	  # 直接作为web服务器使用
	  # 配置工程目录
	  chdir=/var/www/Tpp
	  # 配置项目的wsgi目录，相对于工程目录
	  wsgi-file=Tpp/wsgi.py
	
	  # 配置进程，线程信息
	  process=4
	  threads=2
	  enable-threads=True
	  master=True
	  pidfile=uwsgi.pid
	  daemonize=uwsgi.log
	```
### 3.修改nginx对接
	  ```
	  vim /etc/nginx/conf.d/default.conf
	  server {
	    ...
	    location / {
	      root /var/www/Tpp;
	      # proxy_pass http://localhost:8000;
	      include /etc/nginx/uwsgi_params;
	      uwsgi_pass http://localhost:8000;
	    }
	    ...
	  }
	  ```
	加载`nginx nginx -s reload`
	启动 `uwsgi --ini uwsgi.ini(Tpp中)` 
### 4.linux直接启
  * ssh root:Root123@服务器公网IP
  * free -h
  * ps -ef|grep uwsgi

5.项目

```
# uwsig使用配置文件启动
[uwsgi]
# 项目目录
chdir=/data/wwwroot/tuliao
# 指定项目的application
module=server.wsgi
# 指定sock的文件路径       
socket=%(chdir)/uwsgi/uwsgi.sock
socket = 127.0.0.1:8041
# 进程个数       
workers=5
#线程个数
threads=2
pidfile=%(chdir)/uwsgi/uwsgi.pid
stats=%(chdir)/uwsgi/uwsgi.status
# 指定IP端口       
http=:8042
# 指定静态文件
#static-map=/static=/data/python/taowushe-server/collectedstatic
# 启动uwsgi的用户名和用户组
uid=root
gid=root
# 启用主进程
master=true
# 自动移除unix Socket和pid文件当服务停止的时候
vacuum=true
# 序列化接受的内容，如果可能的话
thunder-lock=true
# 启用线程
enable-threads=true
# 设置自中断时间
harakiri=30
# 设置缓冲
post-buffering=4096
# 设置日志目录
daemonize=%(chdir)/uwsgi/uwsgi.log

#自动给进程命名
"uwsgi.ini" 42L, 960C 
```

