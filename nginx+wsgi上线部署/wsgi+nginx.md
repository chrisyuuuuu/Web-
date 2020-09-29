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
