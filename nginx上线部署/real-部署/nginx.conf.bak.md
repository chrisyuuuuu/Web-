```
server {
    listen 80;
    server_name feizhou.imhehe.com;

    access_log /data/wwwlogs/feizhou_nginx.log combined;
    index index.html index.htm index.php;
    include /etc/nginx/conf.d/rewrite/none.conf;
    root /data/wwwroot/feizhou/;


    #location ~ .*\.(wma|wmv|asf|mp3|mmf|zip|rar|jpg|gif|png|swf|flv)$ {
    #   valid_referers none blocked *.imhehe.com;
    #   if ($invalid_referer) {
    #       return 403;
    #   }
    #}


    location / {
        include uwsgi_params;
        #include /usr/local/nginx/conf/uwsgi_params;
        #uwsgi_pass 127.0.0.1:8080;
        uwsgi_pass unix:/data/wwwroot/feizhou/uwsgi/uwsgi.sock;
        uwsgi_read_timeout 30;
        #index index.html index.htm;
                #proxy_read_timeout 150;
    }

    location /static/ {
        expires 30d;
        access_log off;
        autoindex on;
        alias /data/wwwroot/feizhou/collectedstatic/;
    }

    #location /pc/ {
    #    expires -1;
    #    access_log off;
    #    autoindex on;
    #    alias /data/wwwroot/feizhou/feizhou-html/dist/;
    #}



    location /images/ {
    #location /media/ {
        expires 30d;
        access_log off;
        autoindex on;
        alias /data/wwwroot/feizhou/media/;
    }


    #location ~ .*\.(js|css)?$ {
    #   expires 7d;
    #   access_log off;
    #   autoindex on;
        #        alias /data/wwwroot/feizhou/collectedstatic;
    #}




}




#server {
#    listen 443;
#    server_name feizhou.imhehe.com;
#
#
#    ssl on;
#    ssl_certificate /etc/nginx/conf.d/keys/feizhou.imhehe.com.pem;
#    ssl_certificate_key /etc/nginx/conf.d/keys/feizhou.imhehe.com.key;
#
#
#
#    access_log /data/wwwlogs/feizhou_nginx.log combined;
#    index index.html index.htm index.php;
#    include /etc/nginx/conf.d/rewrite/none.conf;
#    root /data/wwwroot/feizhou/;
#
#
#
#    #location ~ .*\.(wma|wmv|asf|mp3|mmf|zip|rar|jpg|gif|png|swf|flv)$ {
#    #   valid_referers none blocked *.imhehe.com imhehe.com;
#    #   if ($invalid_referer) {
##rewrite# ^/ http://www.linuxeye.com/403.html;
#    #       #return 403;
#    #   }
#    #}
#
#
#    location / {
#        include uwsgi_params;
#        #include /usr/local/nginx/conf/uwsgi_params;
#        #uwsgi_pass 127.0.0.1:8089;
#        uwsgi_pass unix:/data/wwwroot/feizhou/uwsgi/uwsgi.sock;
#        uwsgi_read_timeout 2;
#        #index index.html index.htm;
#                #proxy_read_timeout 150;
#    }
#
#    location /static/ {
#        expires 30d;
#        access_log off;
#        autoindex on;
#        alias /data/wwwroot/feizhou/collectedstatic/;
#    }
#
#
#
#    location /media/ {
#        expires 30d;
#        access_log off;
#        autoindex on;
#        alias /data/wwwroot/feizhou/media/;
#    }
#
#    #location ~ .*\.(js|css)?$ {
#    #   expires 7d;
#    #   access_log off;
#    #}
#}
#
```

