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

* 前提：

  * 已经创建好 QoS 队列，且该队列下没有其他子队列。

* 操作：

  1. 登录到 Controller 节点；
  1. 获取之前所创建的 QoS 和所要创建过滤器的队列的 ID：

    ```
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

## 测试限速功能

### 相同宿主机上的两台云主机之间的限速

### 不同宿主机上的两台云主机之间的限速
