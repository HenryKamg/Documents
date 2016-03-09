# QoS 功能

## 创建 QoS

### 创建绑定云主机的 QoS

* 前提：

  * 已经创建好**云主机。

* 操作：

  1. 登录到 Controller 节点；
  1. 获取云主机的端口 ID：

    ```
    # neutron port-list
    ```
  1. 从中读取云主机端口 ID 并记录，以云主机端口为 target 创建 QoS：

    ```
    # neutron eayun-qos-create --name <QoS_NAME> --target-type port --target-id <PORT_ID> <DIRECTION: egress or ingress> <RATE> <DEFAULT_RATE>
    ```

* 预期结果：

  * QoS 创建成功：

    ```
    # neutron eayun-qos-create --name coffee-qos-port --target-type port --target-id f2a6b8d5-a16f-4834-bf90-c903e39921bb egress 102400 20480
    Created a new qos:
    +--------------------+--------------------------------------+
    | Field              | Value                                |
    +--------------------+--------------------------------------+
    | burst              |                                      |
    | cburst             |                                      |
    | default_queue_id   | c8bdf555-fbd2-4b54-9f22-298b9583c1bd |
    | description        |                                      |
    | direction          | egress                               |
    | id                 | 1dc3acca-6aac-4d22-9912-941be6d8121c |
    | name               | coffee-qos-port                      |
    | qos_queues         | c8bdf555-fbd2-4b54-9f22-298b9583c1bd |
    | rate               | 102400                               |
    | target_id          | f2a6b8d5-a16f-4834-bf90-c903e39921bb |
    | target_type        | port                                 |
    | tenant_id          | bf87349ae6704a87af75ebe9546d4af6     |
    | unattached_filters |                                      |
    +--------------------+--------------------------------------+
    ```

### 创建绑定路由的 QoS

* 前提：

  * 已经创建好路由。

* 操作：

  1. 登录到 Controller 节点；
  1. 获取所要设置路由限制的路由 ID：

    ```
    # neutron router-list | grep XXX
    ```
  1. 创建绑定路由的 QoS：

    ```
    # neutron eayun-qos-create --name <QoS_NAME> --target-type router --target-id <ROUTER_ID> <DIRECTION: egress or ingress> <RATE> <DEFAULT_RATE>
    ```

* 预期结果：

  * 创建绑定路由的 QoS 成功：

    ```
    # neutron eayun-qos-create --name coffee-qos-router --target-type router --target-id 1b569ef2-4e11-40d6-bbb1-a326ad152a4e egress 102400 20480
    Created a new qos:
    +--------------------+--------------------------------------+
    | Field              | Value                                |
    +--------------------+--------------------------------------+
    | burst              |                                      |
    | cburst             |                                      |
    | default_queue_id   | beb0b287-36fe-4df0-bf02-acb819aad0bf |
    | description        |                                      |
    | direction          | egress                               |
    | id                 | 47f26654-90ec-4311-9f5f-4a04fd07c8e6 |
    | name               | coffee-qos-router                    |
    | qos_queues         | beb0b287-36fe-4df0-bf02-acb819aad0bf |
    | rate               | 102400                               |
    | target_id          | 1b569ef2-4e11-40d6-bbb1-a326ad152a4e |
    | target_type        | router                               |
    | tenant_id          | bf87349ae6704a87af75ebe9546d4af6     |
    | unattached_filters |                                      |
    +--------------------+--------------------------------------+
    ```

## 创建 QoS 队列

### 创建 QoS 下的父队列

* 前提：

  * 已经创建好一个 QoS，基于该 QoS 创建父队列。

* 操作：

  1. 登录到 Controller 节点；
  1. 获取之前所创建的 QoS 的 ID：

    ```
    # neutron eayun-qos-list | grep XXX
    ```
  1. 创建 QoS 下的父队列：

    ```
    # neutron eayun-qos-queue-create <QoS_ID> <RATE>
    ```

* 预期结果：

  * QoS 下的父队列创建成功：

    ```
    # neutron eayun-qos-queue-create 1dc3acca-6aac-4d22-9912-941be6d8121c 20480 --prio 0
    Created a new qos_queue:
    +------------------+--------------------------------------+
    | Field            | Value                                |
    +------------------+--------------------------------------+
    | attached_filters |                                      |
    | burst            |                                      |
    | cburst           |                                      |
    | ceil             |                                      |
    | id               | c28cc6d9-f464-413e-befa-8efc2dc740e6 |
    | parent_id        |                                      |
    | prio             | 0                                    |
    | qos_id           | 1dc3acca-6aac-4d22-9912-941be6d8121c |
    | rate             | 20480                                |
    | subqueues        |                                      |
    | tenant_id        | bf87349ae6704a87af75ebe9546d4af6     |
    +------------------+--------------------------------------+
    ```

> ###### 说明：
> * `--prio` 是可选参数，定义该队列的优先级；
> * `--prio` 优先级为 0-7，数字越小，优先级越高，如果创建时未定义，默认优先级为 7。

### 创建父队列下的子队列

* 前提：

  * 已经创建好 QoS 下的父队列。

* 操作：

  1. 登录到 Controller 节点；
  1. 获取之前所创建的 QoS 和该 QoS 的父队列 ID：

    ```
    # neutron eayun-qos-queue-list | grep XXX
    ```
  1. 创建该 QoS 父队列的子队列：

    ```
    # neutron eayun-qos-queue-create --parent <PARENT_ID> --prio <PRIORITY_NUM> <QoS_ID> <RATE>
    ```

* 预期结果：

  * 父队列下的子队列创建成功：

    ```
    # neutron eayun-qos-queue-create --parent c28cc6d9-f464-413e-befa-8efc2dc740e6 --prio 1 1dc3acca-6aac-4d22-9912-941be6d8121c 10240
    Created a new qos_queue:
    +------------------+--------------------------------------+
    | Field            | Value                                |
    +------------------+--------------------------------------+
    | attached_filters |                                      |
    | burst            |                                      |
    | cburst           |                                      |
    | ceil             |                                      |
    | id               | fd7d83b7-5f5b-449e-bed5-b0c21e10b318 |
    | parent_id        | c28cc6d9-f464-413e-befa-8efc2dc740e6 |
    | prio             | 1                                    |
    | qos_id           | 1dc3acca-6aac-4d22-9912-941be6d8121c |
    | rate             | 10240                                |
    | subqueues        |                                      |
    | tenant_id        | bf87349ae6704a87af75ebe9546d4af6     |
    +------------------+--------------------------------------+
    ```

## 创建过滤器

### 创建基于 QoS 的过滤器

* 前提：

  * 已经创建好 QoS。

* 操作：

  1. 登录到 Controller 节点；
  1. 获取所要创建过滤器的 QoS 的 ID：

    ```
    # neutron eayun-qos-list | grep XXX
    ```
  1. 创建该 QoS 的过滤器：

    ```
    # neutron eayun-qos-filter-create --protocol <PROTOCOL_NUM>\
    --dst-port <PORT_NUM> --dst-addr <ADDR_CDIR> <QoS_ID> <PRIO>
    ```

* 预期结果：

  * 基于 QoS 的过滤器创建成功：

    ```
    # neutron eayun-qos-filter-create --protocol 5 --dst-port 5201 --dst-addr 172.16.200.0/24 cfd12bf4-62dc-420b-bca9-1dd41e8f4da2 100
    Created a new qos_filter:
    +-----------+--------------------------------------+
    | Field     | Value                                |
    +-----------+--------------------------------------+
    | dst_addr  | 172.16.200.0/24                      |
    | dst_port  | 5201                                 |
    | id        | 165f3edd-feb4-4b7c-a04f-85db678edc4b |
    | prio      | 100                                  |
    | protocol  | 5                                    |
    | qos_id    | cfd12bf4-62dc-420b-bca9-1dd41e8f4da2 |
    | queue_id  |                                      |
    | src_addr  |                                      |
    | src_port  |                                      |
    | tenant_id | bf87349ae6704a87af75ebe9546d4af6     |
    +-----------+--------------------------------------+
    ```

### 创建基于队列的过滤器

* 前提：

  * 已经创建好 QoS 队列，且该队列下没有其他子队列。

* 操作：

  1. 登录到 Controller 节点；
  1. 获取之前所创建的 QoS 和所要创建过滤器的队列的 ID：

    ```
    # neutron eayun-qos-queue-list | grep XXX
    ```
  1. 创建该 QoS 队列的过滤器：

    ```
    # neutron eayun-qos-filter-create --queue <QUEUE_ID> --protocol <PROTOCOL_NUM>\
    --dst-port <PORT_NUM> --dst-addr <ADDR_CDIR> <QoS_ID> <PRIO>
    ```

* 预期结果：

  * 过滤器创建成功：

    ```
    # neutron eayun-qos-filter-create --queue fd7d83b7-5f5b-449e-bed5-b0c21e10b318 --protocol 5\
    --dst-port 5001 --dst-addr 172.16.200.0/24 1dc3acca-6aac-4d22-9912-941be6d8121c 100
    Created a new qos_filter:
    +-----------+--------------------------------------+
    | Field     | Value                                |
    +-----------+--------------------------------------+
    | dst_addr  | 172.16.200.0/24                      |
    | dst_port  | 5001                                 |
    | id        | ab22540e-b99c-499d-93aa-018de003a255 |
    | prio      | 100                                  |
    | protocol  | 5                                    |
    | qos_id    | 1dc3acca-6aac-4d22-9912-941be6d8121c |
    | queue_id  | fd7d83b7-5f5b-449e-bed5-b0c21e10b318 |
    | src_addr  |                                      |
    | src_port  |                                      |
    | tenant_id | bf87349ae6704a87af75ebe9546d4af6     |
    +-----------+--------------------------------------+
    ```

## 删除操作

### 删除 QoS

* 前提：

  * 环境中已经创建了 QoS 并在其下创建了队列，创建了队列对应的过滤器。

* 操作：

  1. 登录到 Controller 节点；
  1. 获取所要删除的 QoS 的 ID：

    ```
    # neutron eayun-qos-list | grep XXX
    ```
  1. 删除 QoS：

    ```
    # neutron eayun-qos-delete <QoS_ID>
    ```
  1. 验证 QoS 和其下资源是否被删除。

* 预期结果：

  * 成功删除 QoS：

    ```
    # neutron eayun-qos-delete a43338d7-4fd6-432e-910c-1d5f84ed5f53
    Deleted qos: a43338d7-4fd6-432e-910c-1d5f84ed5f53
    ```
  * QoS 下的队列和过滤器均被删除，没有输出内容：

    ```
    # neutron eayun-qos-queue-list

    # neutron eayun-qos-filter-list

    ```

### 删除队列

* 前提：

  * 环境中已经创建了 QoS 并在其下创建了队列，创建了队列对应的过滤器。

* 操作：

  1. 登录到 Controller 节点；
  1. 获取所要删除的队列的 ID：

    ```
    # neutron eayun-qos-queue-list
    ```
  1. 删除队列：

    ```
    # neutron eayun-qos-queue-delete <QUEUE_ID>
    ```
  1. 验证其他资源是否被删除。

* 预期结果：

  * 队列被成功删除：

    ```
    # neutron eayun-qos-queue-delete 0a96635d-0016-424b-a9f8-da41da91261a
    Deleted qos_queue: 0a96635d-0016-424b-a9f8-da41da91261a
    ```
  * QoS 和过滤器均没有被删除：

    ```
    # neutron eayun-qos-filter-list
    +--------------------------------------+--------------------------------------+----------+------+----------+----------+----------+-----------------+----------+
    | id                                   | qos_id                               | queue_id | prio | protocol | src_port | dst_port | src_addr        | dst_addr |
    +--------------------------------------+--------------------------------------+----------+------+----------+----------+----------+-----------------+----------+
    | 44cb3d98-aeab-4c5d-809c-e6c484c1f219 | 31df80a8-5cf8-4ba5-a021-b4ab9cce875d |          |  100 |        4 |       21 |          | 172.16.200.0/24 |          |
    +--------------------------------------+--------------------------------------+----------+------+----------+----------+----------+-----------------+----------+

    # neutron eayun-qos-list
    +--------------------------------------+------------------+-------------+-----------+-------------+--------------------------------------+--------+-------+--------+--------------------------------------+
    | id                                   | name             | description | direction | target_type | target_id                            |   rate | burst | cburst | default_queue_id                     |
    +--------------------------------------+------------------+-------------+-----------+-------------+--------------------------------------+--------+-------+--------+--------------------------------------+
    | 31df80a8-5cf8-4ba5-a021-b4ab9cce875d | coffee-test-port |             | egress    | port        | f2a6b8d5-a16f-4834-bf90-c903e39921bb | 100000 |       |        | 829bcc90-c22f-4c3d-afc3-0b115a653d67 |
    +--------------------------------------+------------------+-------------+-----------+-------------+--------------------------------------+--------+-------+--------+--------------------------------------+
    ```
  * 可重新创建队列后，将该过滤器指向新创建的队列，使用如下命令完成：

    ```
    # neutron eayun-qos-filter-update --queue <NEW_QUEUE_ID> <FILTER_ID>
    ```

> #### 注意：
> * 如果删除的是父队列，那么该父队列下的子队列将被删除。

### 删除过滤器

* 前提：

  * 环境中已经创建了 QoS 并在其下创建了队列，创建了队列对应的过滤器。

* 操作：

  1. 登录到 Controller 节点；
  1. 获取所要删除的过滤器的 ID：

    ```
    # neutron eayun-qos-filter-list
    ```
  1. 删除过滤器：

    ```
    # neutron eayun-qos-filter-delete <FILTER_ID>
    ```
  1. 验证其他资源是否被删除。

* 预期结果：

  * 过滤器被成功删除：

    ```
    # neutron eayun-qos-filter-delete 44cb3d98-aeab-4c5d-809c-e6c484c1f219
    Deleted qos_filter: 44cb3d98-aeab-4c5d-809c-e6c484c1f219
    ```
  * QoS 和队列均未被删除：

    ```
    # neutron eayun-qos-list
    +--------------------------------------+------------------+-------------+-----------+-------------+--------------------------------------+--------+-------+--------+--------------------------------------+
    | id                                   | name             | description | direction | target_type | target_id                            |   rate | burst | cburst | default_queue_id                     |
    +--------------------------------------+------------------+-------------+-----------+-------------+--------------------------------------+--------+-------+--------+--------------------------------------+
    | 31df80a8-5cf8-4ba5-a021-b4ab9cce875d | coffee-test-port |             | egress    | port        | f2a6b8d5-a16f-4834-bf90-c903e39921bb | 100000 |       |        | 829bcc90-c22f-4c3d-afc3-0b115a653d67 |
    +--------------------------------------+------------------+-------------+-----------+-------------+--------------------------------------+--------+-------+--------+--------------------------------------+

    # neutron eayun-qos-queue-list
    +--------------------------------------+--------------------------------------+-----------+------+-------+--------+-------+--------+
    | id                                   | qos_id                               | parent_id | prio |  rate | ceil   | burst | cburst |
    +--------------------------------------+--------------------------------------+-----------+------+-------+--------+-------+--------+
    | 36613f65-3cd1-43c5-b564-bfdb6fe7f7e3 | 31df80a8-5cf8-4ba5-a021-b4ab9cce875d |           |      | 40000 |        |       |        |
    | 829bcc90-c22f-4c3d-afc3-0b115a653d67 | 31df80a8-5cf8-4ba5-a021-b4ab9cce875d |           | 7    | 10000 | 100000 |       |        |
    +--------------------------------------+--------------------------------------+-----------+------+-------+--------+-------+--------+
    ```

## 测试限速功能

### 同一网络上的两台云主机之间的限速

* 场景描述：

  有一个内网，在这个内网里有两台虚拟机需要通信，instanceA 和 instanceB；其中 instanceA 作为这个内网的 FTP 服务器需要向 instnceB 提供服务。在 instanceA 上设置QoS，带宽为 100KB/s，默认队列的保证带宽为 10KB/s。现在让 instanceA 的 FTP 保证 40KB/s。

* 前提：

  * 已经创建了同一个内网中的三个虚拟机，名称分别为 instance[A-C]。
  * instanceA 和 instanceB 中都已经安装了 iperf3 网络性能测试工具。
  * instanceC 也安装了 iperf3，用于模拟其他流量占用带宽的情况。
  * 创建一个 QoS，带宽为 100KB/s，默认队列带宽为 10KB/s，方向为上传（输出），指向 instanceA 的端口：

    ```
    # neutron eayun-qos-create --name apporc-test-port --target-type port --target-id 7ec66d70-76ad-4f22-b01b-bed6e636247a egress 102400 10240             
    Created a new qos:
    +--------------------+--------------------------------------+
    | Field              | Value                                |
    +--------------------+--------------------------------------+
    | burst              |                                      |
    | cburst             |                                      |
    | default_queue_id   | 12c7295c-5dfd-4f5e-8d75-41938471e808 |
    | description        |                                      |
    | direction          | egress                               |
    | id                 | 055c053f-8b87-43b2-9b5e-38b925fdae86 |
    | name               | apporc-test-port                     |
    | qos_queues         | 12c7295c-5dfd-4f5e-8d75-41938471e808 |
    | rate               | 102400                               |
    | target_id          | 7ec66d70-76ad-4f22-b01b-bed6e636247a |
    | target_type        | port                                 |
    | tenant_id          | 30187482c96749f6a1eccd6acd76f45d     |
    | unattached_filters |                                      |
    +--------------------+--------------------------------------+
    ```
  * 创建 QoS 下的队列 queueA，带宽为 40KB/s：

    ```
    # neutron eayun-qos-queue-create 055c053f-8b87-43b2-9b5e-38b925fdae86 40960 --ceil 102400 --prio 0                                                     
    Created a new qos_queue:
    +------------------+--------------------------------------+
    | Field            | Value                                |
    +------------------+--------------------------------------+
    | attached_filters |                                      |
    | burst            |                                      |
    | cburst           |                                      |
    | ceil             | 102400                               |
    | id               | 50fcccc9-2406-4172-97e2-9cba3a28cd39 |
    | parent_id        |                                      |
    | prio             | 0                                    |
    | qos_id           | 055c053f-8b87-43b2-9b5e-38b925fdae86 |
    | rate             | 40960                                |
    | subqueues        |                                      |
    | tenant_id        | 30187482c96749f6a1eccd6acd76f45d     |
    +------------------+--------------------------------------+
    ```
  * 创建过滤器，匹配从 instanceA 向外提供的 FTP 流量, 方便起见，假定 ftp 端口为 21，协议 udp，指向 queueA：

    ```
    # neutron eayun-qos-filter-create --queue 50fcccc9-2406-4172-97e2-9cba3a28cd39 --protocol 17 --src-port 21 --src-addr 10.10.10.0/24 055c053f-8b87-43b2-9
    b5e-38b925fdae86 100                                                                                                                                                                           
    Created a new qos_filter:
    +-----------+--------------------------------------+
    | Field     | Value                                |
    +-----------+--------------------------------------+
    | dst_addr  |                                      |
    | dst_port  |                                      |
    | id        | 4ce9084f-7957-4e16-9f63-3dc77ca99c80 |
    | prio      | 100                                  |
    | protocol  | 6                                    |
    | qos_id    | 055c053f-8b87-43b2-9b5e-38b925fdae86 |
    | queue_id  | 50fcccc9-2406-4172-97e2-9cba3a28cd39 |
    | src_addr  | 10.10.10.0/24                        |
    | src_port  | 21                                   |
    | tenant_id | 30187482c96749f6a1eccd6acd76f45d     |
    +-----------+--------------------------------------+
    ```

* 操作：

  1. 访问 instanceA，在 instanceA 中执行 `iperf3 -s`；
  1. 访问 instanceB，在 instanceB 中执行 `iperf3 -c <IP_OF_instanceA> -u -R -f K -b 1M`，记录测试结果 data1，此时流量的方向为 isntanceA -> instanceB，端口为默认端口 5201；
  1. 访问 instanceC，在 instanceC 中执行 `iperf3 -s`；
  1. 访问 instanceB，在 instanceB 中执行 `iperf3 -c <IP_OF_instanceC> -u -R -f K -b 0`，记录测试结果 data2，此时流量的方向为 instanceC -> instanceB，端口为默认端口 5201；
  1. 访问 instanceA，在 instanceA 中执行 `iperf3 -s -p 21`；
  1. 访问 instanceB，在 instanceB 中执行 `iperf3 -c <IP_OF_instanceA> -u -R -f K -p 21 -b 1M`，记录测试结果 data3，此时流量的方向为 instanceA -> instanceB，端口为 21；
  1. 访问 instanceC，在 instanceC 中执行 `iperf3 -c <IP_OF_instanceA> -u -R -f K -t 30 -b 800K`，记录测试结果 data4，此时流量方向为 instanceA -> instanceC，端口为默认端口 5201；
  1. 当 instanceA -> instanceC 大概执行了 10s 时，访问 instanceB，再次在 instanceB 中执行 `iperf3 -c <IP_OF_instanceA> -u -R -f K -p 21 -b 800K`，记录测试结果 data5，此时流量的方向为 instanceA -> instanceB，端口为 21；
  1. 分别比较 data1 和 data2、data3 和 data1、data5 和 data4、data5 和 data3。

* 预期结果：

  * 比较 data1 和 data2，看到 data1 的带宽速度明显比 data2 的带宽速度高很多(不要参照最终统计值)；

    ```
    # instanceA -> instanceB

    $ iperf3 -c 10.10.10.8 -u -R -f K -b 1M
    Connecting to host 10.10.10.8, port 5201
    Reverse mode, remote host 10.10.10.8 is sending
    [  4] local 10.10.10.9 port 55713 connected to 10.10.10.8 port 5201
    [ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
    [  4]   0.00-1.00   sec   104 KBytes   104 KBytes/sec  18.718 ms  0/13 (0%)  
    [  4]   1.00-2.00   sec  96.0 KBytes  96.0 KBytes/sec  30.415 ms  0/12 (0%)  
    [  4]   2.00-3.00   sec  96.0 KBytes  96.0 KBytes/sec  35.347 ms  0/12 (0%)  
    [  4]   3.00-4.00   sec   104 KBytes   104 KBytes/sec  36.074 ms  0/13 (0%)  
    [  4]   4.00-5.00   sec  96.0 KBytes  96.0 KBytes/sec  41.047 ms  0/12 (0%)  
    [  4]   5.00-6.00   sec  96.0 KBytes  96.0 KBytes/sec  40.724 ms  0/12 (0%)  
    [  4]   6.00-7.00   sec  96.0 KBytes  96.0 KBytes/sec  40.565 ms  0/12 (0%)  
    [  4]   7.00-8.00   sec  96.0 KBytes  96.0 KBytes/sec  39.854 ms  0/12 (0%)  
    [  4]   8.00-9.00   sec  96.0 KBytes  96.0 KBytes/sec  39.387 ms  0/12 (0%)  
    [  4]   9.00-10.00  sec  96.0 KBytes  96.0 KBytes/sec  39.002 ms  0/12 (0%)  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
    [  4]   0.00-10.00  sec  1.20 MBytes   122 KBytes/sec  40.225 ms  0/153 (0%)  
    [  4] Sent 153 datagrams

    iperf Done.

    # instanceC -> instanceB

    $ iperf3 -c 10.10.10.24 -u -R -f K -b 0
    Connecting to host 10.10.10.24, port 5201
    Reverse mode, remote host 10.10.10.24 is sending
    [  4] local 10.10.10.9 port 41633 connected to 10.10.10.24 port 5201
    [ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
    [  4]   0.00-1.00   sec   286 MBytes  292514 KBytes/sec  0.024 ms  1405/37966 (3.7%)  
    [  4]   1.00-2.00   sec   292 MBytes  298671 KBytes/sec  0.023 ms  51/37383 (0.14%)  
    [  4]   2.00-3.00   sec   295 MBytes  302414 KBytes/sec  0.303 ms  2/37803 (0.0053%)  
    [  4]   3.00-4.00   sec   295 MBytes  302084 KBytes/sec  0.057 ms  2/37763 (0.0053%)  
    [  4]   4.00-5.00   sec   295 MBytes  302159 KBytes/sec  0.022 ms  51/37817 (0.13%)  
    [  4]   5.00-6.00   sec   298 MBytes  304794 KBytes/sec  0.032 ms  4/38103 (0.01%)  
    [  4]   6.00-7.00   sec   292 MBytes  299502 KBytes/sec  0.024 ms  6/37443 (0.016%)  
    [  4]   7.00-8.00   sec   294 MBytes  301444 KBytes/sec  0.024 ms  8/37685 (0.021%)  
    [  4]   8.00-9.00   sec   294 MBytes  300901 KBytes/sec  0.023 ms  34/37643 (0.09%)  
    [  4]   9.00-10.00  sec   295 MBytes  302195 KBytes/sec  0.023 ms  0/37775 (0%)  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
    [  4]   0.00-10.00  sec  2.88 GBytes  301999 KBytes/sec  0.023 ms  1563/377500 (0.41%)  
    [  4] Sent 377500 datagrams
    [SUM]  0.0-10.0 sec  1563 datagrams received out-of-order

    iperf Done.
    ```
  * 比较 data3 和 data1，看到 data3 和 data1 的速度是基本一致的。

    ```
    # instanceA -> instanceB : port 21

    $ iperf3 -c 10.10.10.8 -u -R -p 21 -f K -b 1M
    Connecting to host 10.10.10.8, port 21
    Reverse mode, remote host 10.10.10.8 is sending
    [  4] local 10.10.10.9 port 51557 connected to 10.10.10.8 port 21
    [ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
    [  4]   0.00-1.00   sec   104 KBytes   104 KBytes/sec  18.857 ms  0/13 (0%)  
    [  4]   1.00-2.00   sec  96.0 KBytes  96.0 KBytes/sec  30.402 ms  0/12 (0%)  
    [  4]   2.00-3.00   sec  96.0 KBytes  96.0 KBytes/sec  36.275 ms  0/12 (0%)  
    [  4]   3.00-4.00   sec  96.0 KBytes  96.0 KBytes/sec  38.105 ms  0/12 (0%)  
    [  4]   4.00-5.00   sec  96.0 KBytes  96.0 KBytes/sec  37.957 ms  0/12 (0%)  
    [  4]   5.00-6.00   sec  96.0 KBytes  96.0 KBytes/sec  38.507 ms  0/12 (0%)  
    [  4]   6.00-7.00   sec  96.0 KBytes  96.0 KBytes/sec  38.610 ms  0/12 (0%)  
    [  4]   7.00-8.00   sec   104 KBytes   104 KBytes/sec  37.157 ms  0/13 (0%)  
    [  4]   8.00-9.00   sec  96.0 KBytes  96.0 KBytes/sec  38.425 ms  0/12 (0%)  
    [  4]   9.00-10.00  sec  96.0 KBytes  96.0 KBytes/sec  42.153 ms  0/12 (0%)  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
    [  4]   0.00-10.00  sec  1.20 MBytes   122 KBytes/sec  42.153 ms  0/122 (0%)  
    [  4] Sent 122 datagrams

    iperf Done.
    ```
  * 比较 data5 和 data4，看到开始执行时，instanceA -> instanceC 的带宽大概为 100KB/s，当 instanceA -> instanceB 开始执行后，instanceA -> instanceC 的带宽减小为大概 10KB/s，而 instanceA -> instanceB 的带宽为大概 90KB/s：

    ```
    # instanceA -> instanceC

    $ iperf3 -c 10.10.10.8 -t 30 -u -R -f K -b 800K
    Connecting to host 10.10.10.8, port 5201
    Reverse mode, remote host 10.10.10.8 is sending
    [  4] local 10.10.10.24 port 59296 connected to 10.10.10.8 port 5201
    [ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
    [  4]   0.00-1.00   sec   104 KBytes   104 KBytes/sec  70.472 ms  0/13 (0%)  
    [  4]   1.00-2.00   sec  96.0 KBytes  96.0 KBytes/sec  47.480 ms  0/12 (0%)  
    [  4]   2.00-3.00   sec  96.0 KBytes  96.0 KBytes/sec  37.286 ms  0/12 (0%)  
    [  4]   3.00-4.00   sec  96.0 KBytes  96.0 KBytes/sec  32.209 ms  0/12 (0%)  
    [  4]   4.00-5.00   sec  96.0 KBytes  96.0 KBytes/sec  29.287 ms  0/12 (0%)  
    [  4]   5.00-6.00   sec  96.0 KBytes  96.0 KBytes/sec  31.892 ms  0/12 (0%)  
    [  4]   6.00-7.00   sec  96.0 KBytes  96.0 KBytes/sec  30.489 ms  0/12 (0%)  
    [  4]   7.00-8.00   sec  24.0 KBytes  24.0 KBytes/sec  32.127 ms  0/3 (0%)  
    [  4]   8.00-9.00   sec  16.0 KBytes  16.0 KBytes/sec  121.170 ms  0/2 (0%)  
    [  4]   9.00-10.00  sec  8.00 KBytes  8.00 KBytes/sec  119.311 ms  0/1 (0%)  
    [  4]  10.00-11.00  sec  8.00 KBytes  8.00 KBytes/sec  157.146 ms  0/1 (0%)  
    [  4]  11.00-12.00  sec  8.00 KBytes  8.00 KBytes/sec  192.606 ms  0/1 (0%)  
    [  4]  12.00-13.00  sec  8.00 KBytes  8.00 KBytes/sec  225.857 ms  0/1 (0%)  
    [  4]  13.00-14.00  sec  16.0 KBytes  16.0 KBytes/sec  292.498 ms  0/2 (0%)  
    [  4]  14.00-15.00  sec  8.00 KBytes  8.00 KBytes/sec  319.507 ms  0/1 (0%)  
    [  4]  15.00-16.00  sec  8.00 KBytes  8.00 KBytes/sec  344.824 ms  0/1 (0%)  
    [  4]  16.00-17.00  sec  8.00 KBytes  8.00 KBytes/sec  369.523 ms  0/1 (0%)  
    [  4]  17.00-18.00  sec  8.00 KBytes  8.00 KBytes/sec  393.170 ms  0/1 (0%)  
    [  4]  18.00-19.00  sec  16.0 KBytes  16.0 KBytes/sec  439.165 ms  0/2 (0%)  
    [  4]  19.00-20.00  sec  56.0 KBytes  56.0 KBytes/sec  314.108 ms  0/7 (0%)  
    [  4]  20.00-21.00  sec  96.0 KBytes  96.0 KBytes/sec  159.737 ms  0/12 (0%)  
    [  4]  21.00-22.00  sec  96.0 KBytes  96.0 KBytes/sec  88.186 ms  0/12 (0%)  
    [  4]  22.00-23.00  sec  96.0 KBytes  96.0 KBytes/sec  58.941 ms  0/12 (0%)  
    [  4]  23.00-24.00  sec  96.0 KBytes  96.0 KBytes/sec  41.155 ms  0/12 (0%)  
    [  4]  24.00-25.00  sec  96.0 KBytes  96.0 KBytes/sec  36.172 ms  0/12 (0%)  
    [  4]  25.00-26.00  sec  96.0 KBytes  96.0 KBytes/sec  31.791 ms  0/12 (0%)  
    [  4]  26.00-27.00  sec  96.0 KBytes  96.0 KBytes/sec  29.539 ms  0/12 (0%)  
    [  4]  27.00-28.00  sec   104 KBytes   104 KBytes/sec  30.633 ms  0/13 (0%)  
    [  4]  28.00-29.00  sec  88.0 KBytes  88.0 KBytes/sec  32.189 ms  0/11 (0%)  
    [  4]  29.00-30.00  sec   104 KBytes   104 KBytes/sec  29.937 ms  0/13 (0%)  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
    [  4]   0.00-30.00  sec  2.87 MBytes  97.9 KBytes/sec  30.745 ms  0/339 (0%)  
    [  4] Sent 339 datagrams

    iperf Done.

    # instanceA -> instanceB : port 21

    $ iperf3 -c 10.10.10.8 -u -R -p 21 -f K -b 800K
    Connecting to host 10.10.10.8, port 21
    Reverse mode, remote host 10.10.10.8 is sending
    [  4] local 10.10.10.9 port 41900 connected to 10.10.10.8 port 21
    [ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
    [  4]   0.00-1.00   sec   144 KBytes   144 KBytes/sec  56.520 ms  2/20 (10%)  
    [  4]   1.00-2.00   sec  88.0 KBytes  88.0 KBytes/sec  48.014 ms  0/11 (0%)  
    [  4]   2.00-3.00   sec  88.0 KBytes  88.0 KBytes/sec  38.932 ms  0/11 (0%)  
    [  4]   3.00-4.00   sec  96.0 KBytes  96.0 KBytes/sec  37.167 ms  0/12 (0%)  
    [  4]   4.00-5.00   sec  88.0 KBytes  88.0 KBytes/sec  35.552 ms  0/11 (0%)  
    [  4]   5.00-6.00   sec  80.0 KBytes  80.0 KBytes/sec  40.777 ms  0/10 (0%)  
    [  4]   6.00-7.00   sec  88.0 KBytes  88.0 KBytes/sec  39.691 ms  0/11 (0%)  
    [  4]   7.00-8.00   sec  88.0 KBytes  88.0 KBytes/sec  35.726 ms  0/11 (0%)  
    [  4]   8.00-9.00   sec  88.0 KBytes  88.0 KBytes/sec  35.826 ms  0/11 (0%)  
    [  4]   9.00-10.00  sec  88.0 KBytes  88.0 KBytes/sec  35.225 ms  0/11 (0%)  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
    [  4]   0.00-10.00  sec  1.05 MBytes   107 KBytes/sec  38.291 ms  2/134 (1.5%)  
    [  4] Sent 134 datagrams

    iperf Done.
    ```
  * 比较 data5 和 data3，看到 data3 是在网络中只有 instanceA -> instanceB 的情况，它使用了接近 100KB/s 的带宽；当网络中使用了 instanceA -> instanceC 带宽后，instanceA -> instanceB 的带宽被重新分配，获得了大概 90KB/s 的带宽：
  * 带宽分配是由于我们设置了队列的优先级为 0，高于默认队列，FTP 的带宽保证为 40KB/s，而默认带宽保证为 10KB/s，当网络中没有其他流量时，100KB/s 可以全部分配给 FTP 使用，当网络中有其他流量，由于 FTP 队列的优先级高于默认队列，那么空闲的流量将全部分配给 FTP 使用，重新分配带宽后 FTP 带宽和默认带宽为 90KB/s 和 10KB/s。

> #### 注意：
> * 创建 QoS 时会自动创建一个默认队列，这个默认队列的优先级为 7，因此，在创建队列时，队列应设置为 0-7 的优先级，不应小于默认队列的优先级；
> * 如果创建队列时，队列的优先级有以下情况：
>   * 与默认队列相同：那么，空闲的流量将按比例分配。如若在本例中 FTP 队列的优先级与默认队列相同，重新分配带宽后，FTP 和默认队列的带宽将分别为 80KB/s 和 20KB/s；
>   * 高于默认队列（如本例）：那么，空闲的流量优先分配给所创建的队列；
>   * 一般不会设置低于默认队列的情况。

> #### 注意：
> * 创建队列时，--protocol 表示所使用的协议号，使用时根据实际情况设置所要使用的协议号。
> * 详情请看：https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers

> ###### 说明：
> * iperf3 的计算数据有些不对的地方，测试结果只需要观察过程的输出带宽即可；
> * 由于设置的 -b 参数和 -l 参数会影响带宽，很难找到准确的 -b 和 -l 参数值，但是该影响不大，不会影响测试结果。

### 不同网络上的两台云主机之间的限速

* 场景描述：

  2 个不同的网络（各自有子网和路由）。其中一个网络中，同时有 A 和 B 两个 instance 需要对外提供 HTTP 服务，另外 instanceA 上面还要对外提供 FTP 服务。在连接着这个内网的路由上设置了一个 QoS，带宽为 100KB/s，默认队列的保证带宽（给未归类的其它流量用）为 10KB/s。现在希望 instanceA 能够使用 60KB/s 的带宽上传，其中 HTTP 保证 40KB/s，FTP 保证 20KB/s，instance B 使用 30KB/s 的带宽上传，全部给 HTTP 服务。

* 前提：

  * 创建 2 个网络，net_1 和 net_2 ，每个网络分别创建对应的子网（ subnet_1 属于 net_1 ，subnet_2 属于 net_2 ）以及路由（ router_1 连接 subnet_1 ，网关指向外网网络； router_2 连接 subnet_2 ，网关指向外网网络 ）；
  * 创建了 3 个虚拟机，名称分别为 instance[A-C] ，连接到 subnet_1 ；
  * 创建了另外 1 个虚拟机，名称分别为 instance[D] ，连接到 subnet_2 ；
  * 为 4 个虚拟机分配 floatingip ；
  * 四个虚拟机中，都安装了 iperf3 工具。
  * 在 router_1 上创建 QoS，带宽设置为 100KB/s，默认队列带宽为 10KB/s，方向为上传：

    ```
    # neutron eayun-qos-create --name zc-testing-router-qos --target-type router --target-id d2b8621f-2c7e-47aa-b692-a39603e6a2ab egress 102400 10240
    Created a new qos:
    +--------------------+--------------------------------------+
    | Field              | Value                                |
    +--------------------+--------------------------------------+
    | burst              |                                      |
    | cburst             |                                      |
    | default_queue_id   | 2faa3f70-d180-4792-b635-fa0ce6a79bdc |
    | description        |                                      |
    | direction          | egress                               |
    | id                 | c1a155f8-ff84-48c1-abf0-721b4672592b |
    | name               | zc-testing-router-qos                |
    | qos_queues         | 2faa3f70-d180-4792-b635-fa0ce6a79bdc |
    | rate               | 102400                               |
    | target_id          | d2b8621f-2c7e-47aa-b692-a39603e6a2ab |
    | target_type        | router                               |
    | tenant_id          | 7b8bc72da97b463182d1ed6666d4b323     |
    | unattached_filters |                                      |
    +--------------------+--------------------------------------+
    ```
  * 在该 QoS 下创建队列 queueA，带宽设置为 60KB/s，提供给 instanceA 使用：

    ```
    # neutron eayun-qos-queue-create c1a155f8-ff84-48c1-abf0-721b4672592b 61440 --ceil 102400 --prio 0
    Created a new qos_queue:
    +------------------+--------------------------------------+
    | Field            | Value                                |
    +------------------+--------------------------------------+
    | attached_filters |                                      |
    | burst            |                                      |
    | cburst           |                                      |
    | ceil             | 102400                               |
    | id               | 94e028a1-c6d4-469a-b670-82571502e6e5 |
    | parent_id        |                                      |
    | prio             | 0                                    |
    | qos_id           | c1a155f8-ff84-48c1-abf0-721b4672592b |
    | rate             | 61440                                |
    | subqueues        |                                      |
    | tenant_id        | 0644b0d9525e4cf7824656c98e9a3ebf     |
    +------------------+--------------------------------------+
    ```
  * 在 queueA 下创建两个队列 queueA-1 和 queueA-2，速度分别设置为 40KB/s 和 20KB/s，分别提供给 HTTP 和 FTP 使用：

    （注意：子队列的 --ceil 参数需要设置才可能出现实际占用带宽的变化）

    ```
    # neutron eayun-qos-queue-create --parent 94e028a1-c6d4-469a-b670-82571502e6e5 c1a155f8-ff84-48c1-abf0-721b4672592b 40960 --ceil 102400 --prio 0
    Created a new qos_queue:
    +------------------+--------------------------------------+
    | Field            | Value                                |
    +------------------+--------------------------------------+
    | attached_filters |                                      |
    | burst            |                                      |
    | cburst           |                                      |
    | ceil             | 102400                               |
    | id               | cea1544c-b91c-4cac-86e9-5d5b2782c966 |
    | parent_id        | 94e028a1-c6d4-469a-b670-82571502e6e5 |
    | prio             | 0                                    |
    | qos_id           | c1a155f8-ff84-48c1-abf0-721b4672592b |
    | rate             | 40960                                |
    | subqueues        |                                      |
    | tenant_id        | 0644b0d9525e4cf7824656c98e9a3ebf     |
    +------------------+--------------------------------------+

    # neutron eayun-qos-queue-create --parent 94e028a1-c6d4-469a-b670-82571502e6e5 c1a155f8-ff84-48c1-abf0-721b4672592b 20480 --ceil 102400 --prio 0
    Created a new qos_queue:
    +------------------+--------------------------------------+
    | Field            | Value                                |
    +------------------+--------------------------------------+
    | attached_filters |                                      |
    | burst            |                                      |
    | cburst           |                                      |
    | ceil             | 102400                               |
    | id               | 6977edb9-ef18-4deb-80f2-1276b4ebcd7e |
    | parent_id        | 94e028a1-c6d4-469a-b670-82571502e6e5 |
    | prio             | 0                                    |
    | qos_id           | c1a155f8-ff84-48c1-abf0-721b4672592b |
    | rate             | 20480                                |
    | subqueues        |                                      |
    | tenant_id        | 0644b0d9525e4cf7824656c98e9a3ebf     |
    +------------------+--------------------------------------+
    ```
  * 在 QoS 下创建队列 queueB，带宽设置为 30KB/s，提供给 instanceB 使用，即 instanceB 的 HTTP 服务使用：

    ```
    # neutron eayun-qos-queue-create c1a155f8-ff84-48c1-abf0-721b4672592b 30720 --ceil 102400 --prio 0
    Created a new qos_queue:
    +------------------+--------------------------------------+
    | Field            | Value                                |
    +------------------+--------------------------------------+
    | attached_filters |                                      |
    | burst            |                                      |
    | cburst           |                                      |
    | ceil             | 102400                               |
    | id               | 3b1f1ba1-e750-4518-924f-c9fdf4e51912 |
    | parent_id        |                                      |
    | prio             | 0                                    |
    | qos_id           | c1a155f8-ff84-48c1-abf0-721b4672592b |
    | rate             | 30720                                |
    | subqueues        |                                      |
    | tenant_id        | 0644b0d9525e4cf7824656c98e9a3ebf     |
    +------------------+--------------------------------------+
    ```
  * 创建过滤器，匹配从 instanceA 向外的 HTTP 流量，指向 queueA-1：

    ```
    # neutron eayun-qos-filter-create --queue cea1544c-b91c-4cac-86e9-5d5b2782c966 --protocol 6 --src-port 80 --src-addr 25.0.0.209/32 c1a155f8-ff84-48c1-abf0-721b4672592b 100
    Created a new qos_filter:
    +-----------+--------------------------------------+
    | Field     | Value                                |
    +-----------+--------------------------------------+
    | dst_addr  |                                      |
    | dst_port  |                                      |
    | id        | 081735ed-7a8d-4ef1-8c8d-51a5b5f8daea |
    | prio      | 100                                  |
    | protocol  | 6                                    |
    | qos_id    | c1a155f8-ff84-48c1-abf0-721b4672592b |
    | queue_id  | cea1544c-b91c-4cac-86e9-5d5b2782c966 |
    | src_addr  | 25.0.0.209/32                        |
    | src_port  | 80                                   |
    | tenant_id | 0644b0d9525e4cf7824656c98e9a3ebf     |
    +-----------+--------------------------------------+
    ```
  * 创建过滤器，匹配从 instanceA 向外的 FTP 流量，指向 queueA-2：

    ```
    # neutron eayun-qos-filter-create --queue 6977edb9-ef18-4deb-80f2-1276b4ebcd7e --protocol 6 --src-port 21 --src-addr 25.0.0.209/32 c1a155f8-ff84-48c1-abf0-721b4672592b 101
    Created a new qos_filter:
    +-----------+--------------------------------------+
    | Field     | Value                                |
    +-----------+--------------------------------------+
    | dst_addr  |                                      |
    | dst_port  |                                      |
    | id        | 2cbcfc10-e646-4ce9-a868-9ca4c226e0cd |
    | prio      | 101                                  |
    | protocol  | 6                                    |
    | qos_id    | c1a155f8-ff84-48c1-abf0-721b4672592b |
    | queue_id  | 6977edb9-ef18-4deb-80f2-1276b4ebcd7e |
    | src_addr  | 25.0.0.209/32                        |
    | src_port  | 21                                   |
    | tenant_id | 0644b0d9525e4cf7824656c98e9a3ebf     |
    +-----------+--------------------------------------+
    ```
  * 创建过滤器，匹配从 instanceB 向外的 HTTP 流量，执行 queueB：

    ```
    # neutron eayun-qos-filter-create --queue 3b1f1ba1-e750-4518-924f-c9fdf4e51912 --protocol 6 --src-port 80 --src-addr 25.0.0.210/32 c1a155f8-ff84-48c1-abf0-721b4672592b 102
    Created a new qos_filter:
    +-----------+--------------------------------------+
    | Field     | Value                                |
    +-----------+--------------------------------------+
    | dst_addr  |                                      |
    | dst_port  |                                      |
    | id        | 648a7f12-5bc1-4ad5-a600-cb79638855e5 |
    | prio      | 102                                  |
    | protocol  | 6                                    |
    | qos_id    | c1a155f8-ff84-48c1-abf0-721b4672592b |
    | queue_id  | 3b1f1ba1-e750-4518-924f-c9fdf4e51912 |
    | src_addr  | 25.0.0.210/32                        |
    | src_port  | 80                                   |
    | tenant_id | 0644b0d9525e4cf7824656c98e9a3ebf     |
    +-----------+--------------------------------------+
    ```

* 操作：

    测试脚本：

    ```
    #!/bin/bash
    # test.sh

    iperf3 -c 25.0.0.209 -R -f K -p 80 -b 800K -t 60 > data1 &
    sleep 10
    iperf3 -c 25.0.0.209 -R -f K -p 21 -b 800K -t 40 > data2 &
    sleep 10
    iperf3 -c 25.0.0.210 -R -f K -p 80 -b 800K -t 40 > data3 &
    sleep 10
    iperf3 -c 25.0.0.211 -R -f K -b 800K -t 30 > data4 &
    ```

    注意：测试过程中，instance[A-D] 上不要连入 ssh，其上操作执行后即应退出 ssh，因为会影响测试数据。
    1. 访问 instanceA，在 instanceA 上执行 `iperf3 -s -p 80 -D`;
    1. 访问 instanceA，在 instanceA 上执行 `iperf3 -s -p 21 -D`;
    1. 访问 instanceB, 在 instanceB 上执行 `iperf3 -s -p 80 -D`;
    1. 访问 instanceC, 在 instanceC 上执行 `iperf3 -s -D`;
    1. 访问 instanceD, 在 instanceD 上执行 `./test.sh`;
* 预期结果：

    由于测试精度不高，以下速度值近似即可
    1. data1 中速度变化依次为 100KB/s -> 66KB/s -> 44KB/s -> 40KB/s -> 60KB/s
       左右。
    2. data2 中速度变化依次为 33KB/s -> 22KB/s -> 20KB/s
    3. data3 中速度变化依次为 33KB/s -> 30KB/s
    4. data4 中速度大概为 10KB/s
