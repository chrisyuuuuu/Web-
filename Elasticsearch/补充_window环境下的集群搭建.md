节点1的配置信息：
cluster.name: my-application   #集群名称
node.name: node-1 #单一节点名称,在同一台机器上必须不一样
network.host: 192.168.13.198   #必须为本机的ip地址,默认解析可以使用127.0.0.1或者省略
http.port: 9200  #服务端口号,在同一台机器上必须不一样
transport.tcp.port: 9300 #集群通信端口号,在同一台机器上必须不一样
discovery.zen.ping.unicast.hosts: ["127.0.0.1:9300", "127.0.0.1:9301"]  #设置集群自动发现机器ip集合
 
节点2的配置信息：
cluster.name: my-application   #集群名称
node.name: node-2 #单一节点名称,在同一台机器上必须不一样
network.host: 192.168.13.198   #必须为本机的ip地址,默认解析可以使用127.0.0.1或者省略
http.port: 9201  #服务端口号,在同一台机器上必须不一样
transport.tcp.port: 9301 #集群通信端口号,在同一台机器上必须不一样
discovery.zen.ping.unicast.hosts: ["127.0.0.1:9300", "127.0.0.1:9301"]  #设置集群自动发现机器ip集合



上面两个图都是检查集群状况的.两个node节点都ok
 

注意:如果有多台机器,直接复制就可以了
注意:因为是yml文件,所以键值对中间有一个空格,不能直接写
transport.tcp.port: 9301
transport.tcp.port:(空格)9301

注意:如果出现 failed to send join request to master字样的信息,主服务器节点不用管,但是其他的从节点服务器一定要把data下的文件都删除,这里存放的都是数据文件.













