# 集群状态检测

该命令用于对EayunStack环境中的集群进行检测，包括对MySQL，RabbitMQ，Ceph，Haproxy集群的检测。

## 命令格式

```
$ eayunstack doctor cls --help
usage: eayunstack doctor cls [-h] [-n {mysql,rabbitmq,ceph,haproxy}] [-a]
                             [-o FILENAME]

Check cluster

optional arguments:
  -h, --help            show this help message and exit
  -n {mysql,rabbitmq,ceph,haproxy}
                        Cluster Name
  -a, --all             Check ALL
  -o FILENAME           Local File To Save Output Info
```

## MySQL集群检测

> ###### 注意
> 该命令可以在**Fuel节点**或**Controller节点**上运行。在**Fuel节点**上运行该命令，可以同时对所有Controller节点进行检测。在**Controller节点**上运行该命令，只检测当前节点。

* Fuel节点执行命令

```
[fuel]$ eayunstack doctor cls -n mysql
[ INFO  ] ******************** Node: 172.16.100.5  ********************
[ INFO  ] ========== Checking mysql cluster status ==========
[ INFO  ] Mysql cluster check successfully !

[ INFO  ] ******************** Node: 172.16.100.6  ********************
[ INFO  ] ========== Checking mysql cluster status ==========
[ INFO  ] Mysql cluster check successfully !

[ INFO  ] ******************** Node: 172.16.100.7  ********************
[ INFO  ] ========== Checking mysql cluster status ==========
[ INFO  ] Mysql cluster check successfully !
```

* Controller节点执行命令

```
[controller]$ eayunstack doctor cls -n mysql
[ INFO  ] ========== Checking mysql cluster status ==========
[ INFO  ] Mysql cluster check successfully !
```

## RabbitMQ集群检测

> ###### 注意
> 该命令可以在**Fuel节点**或**Controller节点**上运行。在**Fuel节点**上运行该命令，可以同时对所有Controller节点进行检测。在**Controller节点**上运行该命令，只检测当前节点。

* Fuel节点执行命令

```
[fuel]$ eayunstack doctor cls -n rabbitmq
[ INFO  ] ******************** Node: 172.16.100.5  ********************
[ INFO  ] ========== Checking rabbitmq cluster status ==========
[ INFO  ] Rabbitmq cluster check successfully !

[ INFO  ] ******************** Node: 172.16.100.6  ********************
[ INFO  ] ========== Checking rabbitmq cluster status ==========
[ INFO  ] Rabbitmq cluster check successfully !

[ INFO  ] ******************** Node: 172.16.100.7  ********************
[ INFO  ] ========== Checking rabbitmq cluster status ==========
[ INFO  ] Rabbitmq cluster check successfully !
```

* Controller节点执行命令

```
[controller]$ eayunstack doctor cls -n rabbitmq
[ INFO  ] ========== Checking rabbitmq cluster status ==========
[ INFO  ] Rabbitmq cluster check successfully !
```

## Ceph集群检测

> ###### 注意
> 该命令可以在**Fuel节点**或**Controller节点**或**Ceph-osd节点**上运行。在**Fuel节点**上运行该命令，可以同时对所有Controller节点进行检测。在**Controller节点**或**Ceph-osd节**上运行该命令，只检测当前节点。

* Fuel节点执行命令

```
[fuel]$ eayunstack doctor cls -n ceph
[ INFO  ] ******************** Node: 172.16.100.5  ********************
[ INFO  ] ========== Checking ceph cluster status ==========
[ INFO  ] Ceph cluster check successfully !
[ INFO  ] ========== Checking ceph osd status ==========
[ INFO  ] Ceph osd status check successfully !

[ INFO  ] ******************** Node: 172.16.100.6  ********************
[ INFO  ] ========== Checking ceph cluster status ==========
[ INFO  ] Ceph cluster check successfully !
[ INFO  ] ========== Checking ceph osd status ==========
[ INFO  ] Ceph osd status check successfully !

[ INFO  ] ******************** Node: 172.16.100.7  ********************
[ INFO  ] ========== Checking ceph cluster status ==========
[ INFO  ] Ceph cluster check successfully !
[ INFO  ] ========== Checking ceph osd status ==========
[ INFO  ] Ceph osd status check successfully !
```

* Controller节点执行命令

```
[controller]$ eayunstack doctor cls -n ceph
[ INFO  ] ========== Checking ceph cluster status ==========
[ INFO  ] Ceph cluster check successfully !
[ INFO  ] ========== Checking ceph osd status ==========
[ INFO  ] Ceph osd status check successfully !
```

* Ceph-osd节点执行命令

```
[ceph-osd]$ eayunstack doctor cls -n ceph
[ INFO  ] ========== Checking ceph cluster status ==========
[ INFO  ] Ceph cluster check successfully !
[ INFO  ] ========== Checking ceph osd status ==========
[ INFO  ] Ceph osd status check successfully !
```

## Haproxy

> ###### 注意
> 该命令可以在**Fuel节点**或**Controller节点**上运行。在**Fuel节点**上运行该命令，可以同时对所有Controller节点进行检测。在**Controller节点**上运行该命令，只检测当前节点。

* Fuel节点执行命令

```
[fuel]$ eayunstack doctor cls -n haproxy
[ INFO  ] ******************** Node: 172.16.100.5  ********************
[ INFO  ] ========== Checking haproxy cluster status ==========
[ INFO  ] Haproxy cluster check successfully !

[ INFO  ] ******************** Node: 172.16.100.6  ********************
[ INFO  ] ========== Checking haproxy cluster status ==========
[ INFO  ] Haproxy cluster check successfully !

[ INFO  ] ******************** Node: 172.16.100.7  ********************
[ INFO  ] ========== Checking haproxy cluster status ==========
[ INFO  ] Haproxy cluster check successfully !
```

* Controller节点执行命令

```
[controller]$ eayunstack doctor cls -n haproxy
[ INFO  ] ========== Checking haproxy cluster status ==========
[ INFO  ] Haproxy cluster check successfully !
```

## 检测所有检测对象

> ###### 注意
> 该命令可以在**Fuel节点**或**Controller节点**上运行。在**Fuel节点**上运行该命令，可以同时对所有Controller节点进行检测。在**Controller节点**上运行该命令，只检测当前节点。

* Fuel节点执行命令

```
[fuel]$ eayunstack doctor cls -a
[ INFO  ] ******************** Node: 172.16.100.5  ********************
[ INFO  ] ========== Checking rabbitmq cluster status ==========
[ INFO  ] Rabbitmq cluster check successfully !
[ INFO  ] ========== Checking mysql cluster status ==========
[ INFO  ] Mysql cluster check successfully !
[ INFO  ] ========== Checking haproxy cluster status ==========
[ INFO  ] Haproxy cluster check successfully !
[ INFO  ] ========== Checking ceph cluster status ==========
[ INFO  ] Ceph cluster check successfully !
[ INFO  ] ========== Checking ceph osd status ==========
[ INFO  ] Ceph osd status check successfully !

[ INFO  ] ******************** Node: 172.16.100.6  ********************
[ INFO  ] ========== Checking rabbitmq cluster status ==========
[ INFO  ] Rabbitmq cluster check successfully !
[ INFO  ] ========== Checking mysql cluster status ==========
[ INFO  ] Mysql cluster check successfully !
[ INFO  ] ========== Checking haproxy cluster status ==========
[ INFO  ] Haproxy cluster check successfully !
[ INFO  ] ========== Checking ceph cluster status ==========
[ INFO  ] Ceph cluster check successfully !
[ INFO  ] ========== Checking ceph osd status ==========
[ INFO  ] Ceph osd status check successfully !

[ INFO  ] ******************** Node: 172.16.100.7  ********************
[ INFO  ] ========== Checking rabbitmq cluster status ==========
[ INFO  ] Rabbitmq cluster check successfully !
[ INFO  ] ========== Checking mysql cluster status ==========
[ INFO  ] Mysql cluster check successfully !
[ INFO  ] ========== Checking haproxy cluster status ==========
[ INFO  ] Haproxy cluster check successfully !
[ INFO  ] ========== Checking ceph cluster status ==========
[ INFO  ] Ceph cluster check successfully !
[ INFO  ] ========== Checking ceph osd status ==========
[ INFO  ] Ceph osd status check successfully !
```

* Controller节点执行命令

```
[controller]$ eayunstack doctor cls -a
[ INFO  ] ========== Checking rabbitmq cluster status ==========
[ INFO  ] Rabbitmq cluster check successfully !
[ INFO  ] ========== Checking mysql cluster status ==========
[ INFO  ] Mysql cluster check successfully !
[ INFO  ] ========== Checking haproxy cluster status ==========
[ INFO  ] Haproxy cluster check successfully !
[ INFO  ] ========== Checking ceph cluster status ==========
[ INFO  ] Ceph cluster check successfully !
[ INFO  ] ========== Checking ceph osd status ==========
[ INFO  ] Ceph osd status check successfully !
```




















