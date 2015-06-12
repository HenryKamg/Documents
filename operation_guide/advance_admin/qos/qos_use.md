# QoS简单示例
测试场景：

1、新增QoS,带宽为100KB/s，默认队列带宽为20KB/s，方向为进；


2、新增父队列，带宽设置为20KB/s，优先级设为最高“0”；


3、新增两个子队列，带宽分别设置为10KB/S，优先级设置为“1”；


4、在其中一个队列里设置过滤器，匹配上instance A 从instance B出来的TCP流量。


测试步骤：

1、新建QoS

```
neutron eayun-qos-create --name chenyan-qos --target-type port --target-id f3ab7c9f-6182-43f4-ba3e-5662b396137f ingress 102400 20480
Created a new qos:
+--------------------+--------------------------------------+
| Field              | Value                                |
+--------------------+--------------------------------------+
| burst              |                                      |
| cburst             |                                      |
| default_queue_id   | 9d891bd0-9868-4aa7-92b6-bdd731ab4a69 |
| description        |                                      |
| direction          | ingress                              |
| id                 | 25ed775a-e1c5-4a7a-ad58-11cc90534898 |
| name               | chenyan-qos                          |
| qos_queues         | 9d891bd0-9868-4aa7-92b6-bdd731ab4a69 |
| rate               | 102400                               |
| target_id          | f3ab7c9f-6182-43f4-ba3e-5662b396137f |
| target_type        | port                                 |
| tenant_id          | 3846bfe69b4a49948b8056d5f9c76859     |
| unattached_filters |                                      |
+--------------------+--------------------------------------+

```


新建的qos匹配上了port

2、建立一个父队列与两个子队列

a、
创建父队列：

```
neutron eayun-qos-queue-create 25ed775a-e1c5-4a7a-ad58-11cc90534898 20480 --prio 0
Created a new qos_queue:
+------------------+--------------------------------------+
| Field            | Value                                |
+------------------+--------------------------------------+
| attached_filters |                                      |
| burst            |                                      |
| cburst           |                                      |
| ceil             |                                      |
| id               | 87301017-9f16-4d18-815b-6e1434dc6455 |
| parent_id        |                                      |
| prio             | 0                                    |
| qos_id           | 25ed775a-e1c5-4a7a-ad58-11cc90534898 |
| rate             | 20480                                |
| subqueues        |                                      |
| tenant_id        | 3846bfe69b4a49948b8056d5f9c76859     |
+------------------+--------------------------------------+

```
b、
创建子队列

```
 neutron eayun-qos-queue-create --parent 87301017-9f16-4d18-815b-6e1434dc6455 --prio 1 25ed775a-e1c5-4a7a-ad58-11cc90534898 10240
 Created a new qos_queue:
+------------------+--------------------------------------+
| Field            | Value                                |
+------------------+--------------------------------------+
| attached_filters |                                      |
| burst            |                                      |
| cburst           |                                      |
| ceil             |                                      |
| id               | 13805649-1a35-4b35-8bbd-35b4dc6453c3 |
| parent_id        | 87301017-9f16-4d18-815b-6e1434dc6455 |
| prio             | 1                                    |
| qos_id           | 25ed775a-e1c5-4a7a-ad58-11cc90534898 |
| rate             | 10240                                |
| subqueues        |                                      |
| tenant_id        | 3846bfe69b4a49948b8056d5f9c76859     |
+------------------+--------------------------------------+

```
c、
创建子队列上的过滤器：

```
 neutron eayun-qos-filter-create --queue 13805649-1a35-4b35-8bbd-35b4dc6453c3 --protocol 6 --src-port 23 --dst-port 23 --src-addr 172.168.200.4/24 --dst-addr 172.168.200.2/24 25ed775a-e1c5-4a7a-ad58-11cc90534898 104
Created a new qos_filter:
+-----------+--------------------------------------+
| Field     | Value                                |
+-----------+--------------------------------------+
| dst_addr  | 172.168.200.2/24                     |
| dst_port  | 23                                   |
| id        | 1bd698fd-73f9-4e19-9836-ca63c70c3f2b |
| prio      | 104                                  |
| protocol  | 6                                    |
| qos_id    | 25ed775a-e1c5-4a7a-ad58-11cc90534898 |
| queue_id  | 13805649-1a35-4b35-8bbd-35b4dc6453c3 |
| src_addr  | 172.168.200.4/24                     |
| src_port  | 23                                   |
| tenant_id | 3846bfe69b4a49948b8056d5f9c76859     |
+-----------+--------------------------------------+

```


在环境中启动两个相同子网的两台虚拟机，使用网络性能测试工具测试
