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

### 相同宿主机上的两台云主机之间的限速

* 场景描述：

  有一个内网，在这个内网里有两台虚拟机需要通信，instanceA 和 instanceB；其中 instanceA 作为这个内网的 FTP 服务器需要向 instnceB 提供服务。在 instanceA 上设置QoS，带宽为 100KB/s，默认队列的保证带宽为 10KB/s。现在让 instanceA 的 FTP 保证 40KB/s。

* 前提：

  * 创建一个 QoS，带宽为 100KB/s，默认队列带宽为 10KB/s，方向为上传（输出），指向 instanceA 的端口：

    ```
    # neutron eayun-qos-create --name coffee-test-port --target-type port --target-id f2a6b8d5-a16f-4834-bf90-c903e39921bb egress 102400 10240
    Created a new qos:
    +--------------------+--------------------------------------+
    | Field              | Value                                |
    +--------------------+--------------------------------------+
    | burst              |                                      |
    | cburst             |                                      |
    | default_queue_id   | 7076470e-6d5a-43e6-8b2f-298ff787b543 |
    | description        |                                      |
    | direction          | egress                               |
    | id                 | a43338d7-4fd6-432e-910c-1d5f84ed5f53 |
    | name               | coffee-test-port                     |
    | qos_queues         | 7076470e-6d5a-43e6-8b2f-298ff787b543 |
    | rate               | 102400                               |
    | target_id          | f2a6b8d5-a16f-4834-bf90-c903e39921bb |
    | target_type        | port                                 |
    | tenant_id          | bf87349ae6704a87af75ebe9546d4af6     |
    | unattached_filters |                                      |
    +--------------------+--------------------------------------+
    ```
  * 创建 QoS 下的队列 queueA，速度限制为 40KB/s：

    ```
    # neutron eayun-qos-queue-create a43338d7-4fd6-432e-910c-1d5f84ed5f53 40960 --ceil 102400 --prio 0
    Created a new qos_queue:
    +------------------+--------------------------------------+
    | Field            | Value                                |
    +------------------+--------------------------------------+
    | attached_filters |                                      |
    | burst            |                                      |
    | cburst           |                                      |
    | ceil             | 102400                               |
    | id               | 2ca88d47-278a-4fa7-9e1f-e15807ec4f12 |
    | parent_id        |                                      |
    | prio             | 0                                    |
    | qos_id           | a43338d7-4fd6-432e-910c-1d5f84ed5f53 |
    | rate             | 40960                                |
    | subqueues        |                                      |
    | tenant_id        | bf87349ae6704a87af75ebe9546d4af6     |
    +------------------+--------------------------------------+
    ```
  * 创建过滤器，匹配从 instanceA 向外提供的 FTP 流量，指向 queueA：

    ```
    # neutron eayun-qos-filter-create --queue 2ca88d47-278a-4fa7-9e1f-e15807ec4f12 --protocol 6 --src-port 21 --src-addr 172.16.200.0/24 a43338d7-4fd6-432e-910c-1d5f84ed5f53 100
    Created a new qos_filter:
    +-----------+--------------------------------------+
    | Field     | Value                                |
    +-----------+--------------------------------------+
    | dst_addr  |                                      |
    | dst_port  |                                      |
    | id        | 3fe2a418-1003-4735-9c03-dfe1bcbdc42c |
    | prio      | 100                                  |
    | protocol  | 17                                   |
    | qos_id    | a43338d7-4fd6-432e-910c-1d5f84ed5f53 |
    | queue_id  | 2ca88d47-278a-4fa7-9e1f-e15807ec4f12 |
    | src_addr  | 172.16.200.0/24                      |
    | src_port  | 21                                   |
    | tenant_id | bf87349ae6704a87af75ebe9546d4af6     |
    +-----------+--------------------------------------+
    ```
  * instanceA 和 instanceB 中都已经安装了 iperf3 网络性能测试工具。
  * instanceC 也安装了 iperf3，用于模拟其他流量占用带宽的情况。

* 操作：

  1. 访问 instanceA，在 instanceA 中执行 `iperf3 -s`；
  1. 访问 instanceB，在 instanceB 中执行 `iperf3 -c <IP_OF_instanceA> -u -R -f K -b 800K -l 1500`，记录测试结果 data1，此时流量的方向为 isntanceA -> instanceB，端口为默认端口 5201；
  1. 访问 instanceB，在 instanceB 中执行 `iperf3 -s`；
  1. 访问 instanceA，在 instanceA 中执行 `iperf3 -c <IP_OF_instanceB> -u -R -f K -b 800K -l 1500`，记录测试结果 data2，此时流量的方向为 instanceB -> instanceA，端口为默认端口 5201；
  1. 访问 instanceA，在 instanceA 中执行 `iperf3 -s -p 21`；
  1. 访问 instanceB，在 instanceB 中执行 `iperf3 -c <IP_OF_instanceA> -u -R -f K -p 21 -b 800K -l 1500`，记录测试结果 data3，此时流量的方向为 instanceA -> instanceB，端口为 21；
  1. 访问 instanceC，在 instanceC 中执行 `iperf3 -s`；
  1. 访问 instanceA，在 instanceA 中执行 `iperf3 -c <IP_OF_instanceC> -u -f K -t 30 -b 800K -l 1500`，记录测试结果 data4，此时流量方向为 instanceA -> instanceC，端口为默认端口 5201；
  1. 当 instanceA -> instanceC 大概执行了 10s 时，访问 instanceB，再次在 instanceB 中执行 `iperf3 -c <IP_OF_instanceA> -u -R -f K -p 21 -b 800K -l 1500`，记录测试结果 data5，此时流量的方向为 instanceA -> instanceB，端口为 21；
  1. 分别比较 data1 和 data2、data3 和 data1、data5 和 data4、data5 和 data3。

* 预期结果：

  * 比较 data1 和 data2，看到 data1 的带宽速度明显比 data2 的带宽速度高很多；

    ```
    # instanceA -> instanceB
    # iperf3 -c 172.16.200.186 -u -R -f K -b 800K -l 1500
    Connecting to host 172.16.200.186, port 5201
    Reverse mode, remote host 172.16.200.186 is sending
    [  4] local 172.16.200.188 port 33712 connected to 172.16.200.186 port 5201
    [ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
    [  4]   0.00-1.00   sec  92.3 KBytes  92.3 KBytes/sec  23.917 ms  0/63 (0%)  
    [  4]   1.00-2.00   sec  93.8 KBytes  93.8 KBytes/sec  24.200 ms  0/64 (0%)  
    [  4]   2.00-3.00   sec  95.2 KBytes  95.2 KBytes/sec  25.160 ms  0/65 (0%)  
    [  4]   3.00-4.00   sec  93.8 KBytes  93.8 KBytes/sec  26.990 ms  0/64 (0%)  
    [  4]   4.00-5.00   sec  95.2 KBytes  95.2 KBytes/sec  23.820 ms  0/65 (0%)  
    [  4]   5.00-6.00   sec  93.8 KBytes  93.8 KBytes/sec  25.466 ms  0/64 (0%)  
    [  4]   6.00-7.00   sec  95.2 KBytes  95.2 KBytes/sec  26.503 ms  0/65 (0%)  
    [  4]   7.00-8.00   sec  93.8 KBytes  93.7 KBytes/sec  23.976 ms  0/64 (0%)  
    [  4]   8.00-9.00   sec  95.2 KBytes  95.2 KBytes/sec  24.954 ms  0/65 (0%)  
    [  4]   9.00-10.00  sec  93.8 KBytes  93.7 KBytes/sec  26.826 ms  0/64 (0%)  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
    [  4]   0.00-10.00  sec   977 KBytes  97.7 KBytes/sec  24.238 ms  0/667 (0%)  
    [  4] Sent 667 datagrams

    iperf Done.

    # instanceB -> instanceA
    # iperf3 -c 172.16.200.188 -u -R -f K -b 800K -l 1500
    Connecting to host 172.16.200.188, port 5201
    Reverse mode, remote host 172.16.200.188 is sending
    [  4] local 172.16.200.186 port 35386 connected to 172.16.200.188 port 5201
    [ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
    [  4]   0.00-1.00   sec  98.1 KBytes  98.1 KBytes/sec  0.097 ms  0/67 (0%)  
    [  4]   1.00-2.00   sec  98.1 KBytes  98.1 KBytes/sec  0.013 ms  0/67 (0%)  
    [  4]   2.00-3.00   sec  98.1 KBytes  98.1 KBytes/sec  0.009 ms  0/67 (0%)  
    [  4]   3.00-4.00   sec  96.7 KBytes  96.7 KBytes/sec  0.008 ms  0/66 (0%)  
    [  4]   4.00-5.00   sec  98.1 KBytes  98.1 KBytes/sec  0.010 ms  0/67 (0%)  
    [  4]   5.00-6.00   sec  98.1 KBytes  98.1 KBytes/sec  0.009 ms  0/67 (0%)  
    [  4]   6.00-7.00   sec  96.7 KBytes  96.7 KBytes/sec  0.015 ms  0/66 (0%)  
    [  4]   7.00-8.00   sec  98.1 KBytes  98.1 KBytes/sec  0.010 ms  0/67 (0%)  
    [  4]   8.00-9.00   sec  98.1 KBytes  98.1 KBytes/sec  0.013 ms  0/67 (0%)  
    [  4]   9.00-10.00  sec  96.7 KBytes  96.7 KBytes/sec  0.012 ms  0/66 (0%)  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
    [  4]   0.00-10.00  sec   977 KBytes  97.7 KBytes/sec  0.012 ms  0/667 (0%)  
    [  4] Sent 667 datagrams

    iperf Done.
    ```
  * 比较 data3 和 data1，看到 data3 和 data1 的速度。。。

    ```
    # instanceA -> instanceB : port 21
    # iperf3 -c 172.16.200.186 -u -R -f K -b 800K -l 1500 -p 21
    Connecting to host 172.16.200.186, port 21
    Reverse mode, remote host 172.16.200.186 is sending
    [  4] local 172.16.200.188 port 34192 connected to 172.16.200.186 port 21
    [ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
    [  4]   0.00-1.00   sec  90.8 KBytes  90.8 KBytes/sec  24.587 ms  0/62 (0%)  
    [  4]   1.00-2.00   sec  95.2 KBytes  95.2 KBytes/sec  24.212 ms  0/65 (0%)  
    [  4]   2.00-3.00   sec  95.2 KBytes  95.2 KBytes/sec  25.166 ms  0/65 (0%)  
    [  4]   3.00-4.00   sec  87.9 KBytes  87.9 KBytes/sec  25.276 ms  0/60 (0%)  
    [  4]   4.00-5.00   sec  95.2 KBytes  95.2 KBytes/sec  26.276 ms  0/65 (0%)  
    [  4]   5.00-6.00   sec  95.2 KBytes  95.2 KBytes/sec  27.598 ms  0/65 (0%)  
    [  4]   6.00-7.00   sec  93.8 KBytes  93.7 KBytes/sec  24.840 ms  0/64 (0%)  
    [  4]   7.00-8.00   sec  95.2 KBytes  95.2 KBytes/sec  25.799 ms  0/65 (0%)  
    [  4]   8.00-9.00   sec  95.2 KBytes  95.2 KBytes/sec  26.986 ms  0/65 (0%)  
    [  4]   9.00-10.00  sec  93.8 KBytes  93.7 KBytes/sec  24.375 ms  0/64 (0%)  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
    [  4]   0.00-10.00  sec   977 KBytes  97.7 KBytes/sec  24.375 ms  0/640 (0%)  
    [  4] Sent 640 datagrams
 
    iperf Done.
    ```
  * 比较 data5 和 data4，看到开始执行时，instanceA -> instanceB 的带宽大概为 100KB/s，当 instanceA -> instanceB 开始执行后，instanceA -> instanceC 的带宽减小为大概 10KB/s，而 instanceA -> instanceB 的带宽为大概 90KB/s：

    ```
    # instanceA -> instanceC
    Accepted connection from 172.16.200.186, port 33902
    [  5] local 172.16.200.187 port 5201 connected to 172.16.200.186 port 41588
    [ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
    [  5]   0.00-1.00   sec  85.0 KBytes  85.0 KBytes/sec  24.567 ms  0/58 (0%)  
    [  5]   1.00-2.00   sec  93.8 KBytes  93.8 KBytes/sec  27.586 ms  0/64 (0%)  
    [  5]   2.00-3.00   sec  95.2 KBytes  95.2 KBytes/sec  24.254 ms  0/65 (0%)  
    [  5]   3.00-4.00   sec  93.8 KBytes  93.8 KBytes/sec  25.803 ms  0/64 (0%)  
    [  5]   4.00-5.00   sec  95.2 KBytes  95.2 KBytes/sec  27.003 ms  0/65 (0%)  
    [  5]   5.00-6.00   sec  93.8 KBytes  93.8 KBytes/sec  24.365 ms  0/64 (0%)  
    [  5]   6.00-7.00   sec  95.2 KBytes  95.2 KBytes/sec  25.456 ms  0/65 (0%)  
    [  5]   7.00-8.00   sec  93.8 KBytes  93.7 KBytes/sec  27.106 ms  0/64 (0%)  
    [  5]   8.00-9.00   sec  95.2 KBytes  95.2 KBytes/sec  23.970 ms  0/65 (0%)  
    [  5]   9.00-10.00  sec  93.8 KBytes  93.7 KBytes/sec  25.587 ms  0/64 (0%)  
    [  5]  10.00-11.00  sec  95.2 KBytes  95.2 KBytes/sec  26.828 ms  0/65 (0%)  
    [  5]  11.00-12.00  sec  93.8 KBytes  93.7 KBytes/sec  24.224 ms  0/64 (0%)  
    [  5]  12.00-13.00  sec  63.0 KBytes  63.0 KBytes/sec  33.128 ms  0/43 (0%)  
    [  5]  13.00-14.00  sec  8.79 KBytes  8.79 KBytes/sec  66.299 ms  0/6 (0%)  
    [  5]  14.00-15.00  sec  10.3 KBytes  10.3 KBytes/sec  92.569 ms  0/7 (0%)  
    [  5]  15.00-16.00  sec  8.79 KBytes  8.79 KBytes/sec  106.652 ms  0/6 (0%)  
    [  5]  16.00-17.00  sec  10.3 KBytes  10.3 KBytes/sec  118.644 ms  0/7 (0%)  
    [  5]  17.00-18.00  sec  8.79 KBytes  8.79 KBytes/sec  123.969 ms  0/6 (0%)  
    [  5]  18.00-19.00  sec  10.3 KBytes  10.3 KBytes/sec  129.273 ms  0/7 (0%)  
    [  5]  19.00-20.00  sec  8.79 KBytes  8.79 KBytes/sec  131.185 ms  0/6 (0%)  
    [  5]  20.00-21.00  sec  10.3 KBytes  10.3 KBytes/sec  133.478 ms  0/7 (0%)  
    [  5]  21.00-22.00  sec  8.79 KBytes  8.79 KBytes/sec  135.247 ms  0/6 (0%)  
    [  5]  22.00-23.00  sec  8.79 KBytes  8.79 KBytes/sec  141.486 ms  0/6 (0%)  
    [  5]  23.00-24.00  sec  10.3 KBytes  10.3 KBytes/sec  142.044 ms  0/7 (0%)  
    [  5]  24.00-25.00  sec  8.79 KBytes  8.79 KBytes/sec  141.576 ms  0/6 (0%)  
    [  5]  25.00-26.00  sec  10.3 KBytes  10.3 KBytes/sec  142.099 ms  0/7 (0%)  
    [  5]  26.00-27.00  sec  8.79 KBytes  8.79 KBytes/sec  141.614 ms  0/6 (0%)  
    [  5]  27.00-28.00  sec  10.3 KBytes  10.3 KBytes/sec  141.839 ms  0/7 (0%)  
    [  5]  28.00-29.00  sec  17.6 KBytes  17.6 KBytes/sec  104.814 ms  0/12 (0%)  
    [  5]  29.00-30.00  sec  93.8 KBytes  93.7 KBytes/sec  27.384 ms  0/64 (0%)  
    [  5]  30.00-31.00  sec  95.2 KBytes  95.2 KBytes/sec  28.104 ms  0/65 (0%)  
    [  5]  31.00-32.00  sec  93.8 KBytes  93.8 KBytes/sec  25.208 ms  0/64 (0%)  
    [  5]  32.00-33.00  sec  95.2 KBytes  95.2 KBytes/sec  26.528 ms  0/65 (0%)  
    [  5]  33.00-34.00  sec  93.8 KBytes  93.8 KBytes/sec  23.831 ms  0/64 (0%)  
    [  5]  34.00-35.00  sec  95.2 KBytes  95.2 KBytes/sec  24.865 ms  0/65 (0%)  
    [  5]  35.00-36.00  sec  93.8 KBytes  93.7 KBytes/sec  26.512 ms  0/64 (0%)  
    [  5]  36.00-37.00  sec  95.2 KBytes  95.2 KBytes/sec  27.826 ms  0/65 (0%)  
    [  5]  37.00-38.00  sec  93.8 KBytes  93.7 KBytes/sec  25.017 ms  0/64 (0%)  
    [  5]  38.00-39.00  sec  95.2 KBytes  95.2 KBytes/sec  26.226 ms  0/65 (0%)  
    [  5]  39.00-40.00  sec  93.8 KBytes  93.8 KBytes/sec  28.107 ms  0/64 (0%)  
    [  5]  40.00-41.00  sec  95.2 KBytes  95.2 KBytes/sec  23.781 ms  0/65 (0%)  
    [  5]  41.00-42.00  sec  95.2 KBytes  95.2 KBytes/sec  25.689 ms  0/65 (0%)  
    [  5]  42.00-43.00  sec  95.2 KBytes  95.2 KBytes/sec  26.097 ms  0/65 (0%)  
    [  5]  43.00-44.00  sec  92.3 KBytes  92.3 KBytes/sec  24.927 ms  0/63 (0%)  
    [  5]  44.00-45.00  sec  95.2 KBytes  95.2 KBytes/sec  28.104 ms  32/97 (33%)  
    [  5]  45.00-45.18  sec  16.1 KBytes  89.0 KBytes/sec  24.465 ms  0/11 (0%)  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
    [  5]   0.00-45.18  sec  2.85 MBytes  64.6 KBytes/sec  24.465 ms  32/1994 (1.6%)  

    # instanceA -> instanceB : port 21
    # iperf3 -c 172.16.200.186 -u -R -f K -b 800K -l 1500 -p 21
    Connecting to host 172.16.200.186, port 21
    Reverse mode, remote host 172.16.200.186 is sending
    [  4] local 172.16.200.188 port 39619 connected to 172.16.200.186 port 21
    [ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
    [  4]   0.00-1.00   sec   144 KBytes   144 KBytes/sec  28.935 ms  203/301 (67%)  
    [  4]   1.00-2.00   sec  86.4 KBytes  86.4 KBytes/sec  27.881 ms  0/59 (0%)  
    [  4]   2.00-3.00   sec  85.0 KBytes  85.0 KBytes/sec  24.524 ms  0/58 (0%)  
    [  4]   3.00-4.00   sec  86.4 KBytes  86.4 KBytes/sec  25.384 ms  0/59 (0%)  
    [  4]   4.00-5.00   sec  82.0 KBytes  82.0 KBytes/sec  27.733 ms  0/56 (0%)  
    [  4]   5.00-6.00   sec  86.4 KBytes  86.4 KBytes/sec  25.519 ms  0/59 (0%)  
    [  4]   6.00-7.00   sec  85.0 KBytes  85.0 KBytes/sec  25.048 ms  0/58 (0%)  
    [  4]   7.00-8.00   sec  85.0 KBytes  85.0 KBytes/sec  30.636 ms  0/58 (0%)  
    [  4]   8.00-9.00   sec  86.4 KBytes  86.4 KBytes/sec  26.126 ms  0/59 (0%)  
    [  4]   9.00-10.00  sec  85.0 KBytes  85.0 KBytes/sec  23.683 ms  0/58 (0%)  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
    [  4]   0.00-10.00  sec  1.35 MBytes   139 KBytes/sec  26.123 ms  203/947 (21%)  
    [  4] Sent 947 datagrams

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

### 不同宿主机上的两台云主机之间的限速

* 场景描述：

  有一个内网，同时有 A 和 B 两个 instance 需要对外提供 HTTP 服务，另外 instanceA 上面还要对外提供 FTP 服务。我在连接着这个内网的路由上设置了一个 QoS，带宽为 100KB/s，默认队列的保证带宽（给未归类的其它流量用）为 10KB/s。我现在希望 instanceA 能够使用 60KB/s 的带宽上传，其中 HTTP 保证 40KB/s，FTP 保证 20KB/s，instance B 使用 30KB/s 的带宽上传，全部给 HTTP 服务。

* 前提：

  * 创建 QoS，带宽设置为 100KB/s，默认队列带宽为 10KB/s，方向为上传，指向该内网的路由：
  * 在该 QoS 下创建队列 queueA，带宽设置为 60KB/s，提供给 instanceA 使用：
  * 在 queueA 下创建两个队列 queueA-1 和 queueA-2，速度分别设置为 40KB/s 和 20KB/s，分别提供给 HTTP 和 FTP 使用：
  * 在 QoS 下创建队列 queueB，带宽设置为 30KB/s，提供给 instanceB 使用，即 instanceB 的 HTTP 服务使用：
  * 创建过滤器，匹配从 instanceA 向外的 HTTP 流量，指向 queueA-1：
  * 创建过滤器，匹配从 instanceA 向外的 FTP 流量，指向 queueA-2：
  * 创建过滤器，匹配从 instanceB 向外的 HTTP 流量，执行 queueB：

* 操作：

* 预期结果：
