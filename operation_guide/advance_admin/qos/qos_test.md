# QoS测试
创建好QoS之后就是测试其性能(采用iperf作为网络性能测试工具)

总共两种测试情况，是根据QoS绑定的类型不同而确定的

1.
若QoS绑定路由，则测试需在不同的宿主机上的两个虚拟机上一个作为性能测试的server，一个做client。

2.
创建过滤器针对，需要测试的流量过滤，测试TCP协议的5001端口，将iperf服务端作为目的地址，示例为：
```
neutron eayun-qos-filter-create --queue ba4fe297-89dd-48f1-9de0-c2ef6433f40c --protocol 6 --dst-port 5001 --dst-addr 172.168.200.27/22 36bbd6f7-0682-4bb5-a9a4-39978b78be6b 202
Created a new qos_filter:
+-----------+--------------------------------------+
| Field     | Value                                |
+-----------+--------------------------------------+
| dst_addr  | 172.168.200.27/22                    |
| dst_port  | 5001                                 |
| id        | 940ad573-2240-4848-913b-1462122f803d |
| prio      | 202                                  |
| protocol  | 6                                    |
| qos_id    | 36bbd6f7-0682-4bb5-a9a4-39978b78be6b |
| queue_id  | ba4fe297-89dd-48f1-9de0-c2ef6433f40c |
| src_addr  |                                      |
| src_port  |                                      |
| tenant_id | 3846bfe69b4a49948b8056d5f9c76859     |
+-----------+--------------------------------------+

```

3.
在iperf的服务端执行命令：
```
iperf -s -i 1 -t 10 -p 5001
```

在iperf客户端执行命令：
```
iperf -c 172.168.200.27 -i 1 -t 10 -p 5001
```

4.
得到测试结果为：
服务端：
![server_result](../Picture/server.png)

客户端：
![client_result](../Picture/client.png)

可以看到已经成匹配了过滤器，测试成功

