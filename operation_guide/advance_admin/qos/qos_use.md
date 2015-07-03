# QoS简单创建


1、新建QoS
(绑定到虚拟机端口，新建的qos匹配上了虚拟机的neutron port)

```
neutron eayun-qos-create --name chenyan-qos --target-type port --target-id f3ab7c9f-6182-43f4-ba3e-5662b396137f egress 102400 20480
Created a new qos:
+--------------------+--------------------------------------+
| Field              | Value                                |
+--------------------+--------------------------------------+
| burst              |                                      |
| cburst             |                                      |
| default_queue_id   | 9d891bd0-9868-4aa7-92b6-bdd731ab4a69 |
| description        |                                      |
| direction          | egress                              |
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

参数说明：

1)<code>--name</code>是可选选项，填写你需要名字

2)<code>--target-type</code>是可选选项，指的是需要绑定的类型，可以是router或者port(注意：若绑定的是router，测试需要在两个不同宿主机上的两台虚拟机之间进行测试；若绑定的是虚拟机port则需要在同一个内网中的两台虚拟机之间进行测试)

3）<code>--target-id</code>填写需绑定的neutron id ，可以是路由器的neutron端口可以是虚拟机的neutron端口使用命令<code>neutron port-list</code>查看获取

4)<code>DIRECTION</code>是必须选项，ingress或者egress，输入或者输出

5)<code>RATE</code>是必须选项，QoS总带宽大小

6)<code>DEFAULT_RATE</code>是必须选项，QoS默认队列的带宽大小

注意其他可选选项使用命令查看<code>neutron eayun-qos-create -h</code>



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


参数说明：

1)<code>--prio</code>可选选项，指定队列优先级，优先级只能从0到7，数字越小越优先，不设置默认优先级为7

2)<code>QOS-ID</code>，必须选项，该QoS Queue所属的QoS的ID

3)<code>RATE</code>，该队列保证的带宽大小


其他可选选项使用命令<code>
neutron eayun-qos-queue-create -h</code>查看


b、
创建子队列

创建子队列的意义：子队列可以共享父队列的带宽，使有限的带宽发挥出更多的作用。

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

参数说明：

1)<code>--parent</code>，指定该子队列之上的父队列的ID

2)<code>--prio</code>，指定该队列优先级，从0到7，数字越小优先级越高，不设置优先级默认为7

3)<code>QOS-ID</code>，必须选项，该QoS Queue所属的QoS的ID

4)<code>RATE</code>，该队列保证的带宽大小


其他可选选项使用命令<code>
neutron eayun-qos-queue-create -h</code>查看

c、
创建子队列上的过滤器：

过滤器只能建立在没有子队列的队列中，也就是说没有下一层的队列中，一个队列可以匹配多个过滤器，一个过滤器只能在一个队列中。

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

参数说明：

1)<code>--queue</code>，指向该过滤器要绑定的队列的ID

2)<code>--protocol</code>，匹配的IP子协议编号，从1到255

3)<code>--src-port</code>，匹配的源端口

4)<code>--dst-port</code>，匹配的目的端口

5)<code>--src-addr</code>，匹配的源地址CIDR

6)<code>--dst-addr</code>，匹配的目的地址CIDR

7)<code>QOS</code>，该过滤器所属的QoS的ID

8)<code>PRIO</code>，该filter的优先级，数字从1-65535数字越高越优先



其他参数获取使用命令查看<code>neutron eayun-qos-filter-create -h</code>

