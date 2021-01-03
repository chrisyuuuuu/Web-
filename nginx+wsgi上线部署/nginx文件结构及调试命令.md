### 1.反向代理

```
 proxy_pass URL; 反向代理，默认不转发header,需转发则设置proxy_set_header HOST $host;
 proxy_method POST;转发的方法名
 proxy_hide_header Cache-control;指定头部不被转发
 proxy_pass_header Cache-control;设置哪些头可转发
 proxy_request_header on;设置转发http请求头
 proxy_pass_request body on;设置转发请求体
```



### 2. nginx配置文件结构

    # main 全局配置
    events{ 工作模式，连接配置
      ...
    }
    http {  http的配置
      ...
      upstream xxx { 负载均衡配置
        ...
      }
      server {  主机配置
        ...
        location xxx{ url配置
          ...
        }
      }
  }
``

### 3. [安装] (http://www.nginx.org)
    - 装key,sudo apt-key add nginx_signing.key
    - 装软件源 vim /etc/apt/sources.list
        - deb  xxx  nginx版本  xxx
        - deb-src xxx  nginx版本  xxx
    - apt update
    - apt install nginx
### 4.nginx进入、退出
    - nginx
    - nginx -s quit
### 5.nginx对接Django,写nginx配置文件
```
    - `vim /etc/nginx/conf.d/default.conf`
    - `location / {
      root /var/www/Tpp;
    }`
    - 对接runserver
      - `server {
        ...
        location / {
          root /var/www/Tpp;
          proxy_pass http://localhost:8000;
        }
        ...
      }
	  `
    - 测试
      `nginx -t -c /etc/nginx/nginx.conf`
    - 启动
      - `nginx -c /etc/nginx/nginx.conf`
    - `ps -ef|grep nginx`
    - `apt install python-dev python3-dev(python.h报错)`
```