```
cd /usr/lib/systemd/system/
[Unit]
Description=uWSGI Emperor Service
After=syslog.target

[Service]
PIDFile=/data/wwwroot/feizhou/uwsgi/uwsgi.pid
#EnvironmentFile=-/usr/bin/uwsgi
ExecStartPre=/bin/mkdir -p /data/wwwroot/feizhou/uwsgi

ExecStartPre=/bin/chown -R uwsgi:uwsgi /data/wwwroot/feizhou/uwsgi
ExecStart=/usr/bin/uwsgi --ini /data/wwwroot/feizhou/uwsgi.ini
ExecReload=/bin/kill -HUP $MAINPID
KillSignal=SIGQUIT
Restart=always
Type=forking
StandardError=syslog
NotifyAccess=all

[Install]
WantedBy=multi-user.target
```

