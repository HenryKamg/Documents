# 灾难恢复模拟场景

##### 场景 No.1: 某个租户所有虚拟机无法连接外网

* 故障描述：

  登录某个租户的任意一台虚拟机，ping 公网任意一个 IP 地址，ping 不通。

* 测试准备：

  1. 登录要测试的租户的 dashboard；
  1. 点击 【Project】 下的 【Network】 选项卡，展开后，点击 【Routers】 标签；
  1. 在右侧的路由列表中，选择与外网连接的路由，点击 【Actions】 中的 【Clear Gateway】

  1. 登录到 controller 节点，找到要测试的租户的连接外网的 qrouter；

    ```
    # neutron router-list | grep test-router
    qrouter-1b569ef2-4e11-40d6-bbb1-a326ad152a4e

    # ip netns exec qrouter-1b569ef2-4e11-40d6-bbb1-a326ad152a4e ip link
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    2: ip_vti0: <NOARP> mtu 1500 qdisc noop state DOWN mode DEFAULT
        link/ipip 0.0.0.0 brd 0.0.0.0
    234: qr-f59b4609-0d: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN mode DEFAULT
        link/ether fa:16:3e:09:cb:8b brd ff:ff:ff:ff:ff:ff
    236: qg-da206956-01: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN mode DEFAULT
        link/ether fa:16:3e:7d:ab:fc brd ff:ff:ff:ff:ff:ff

    # ip netns exec qrouter-1b569ef2-4e11-40d6-bbb1-a326ad152a4e ip link del qg-da206956-01
    ```
  1. 打开该租户中其中一台虚拟机的控制台，ping 外网地址，提示："Destination Net Unreachable"。

* 测试步骤：

  1. 登录 Controller 节点；
  1. 执行命令：

    ```
    # neutron router-update test-router --admin_state_up True
    ```

* 预期结果：

  * 登录到 dashboard 后，点击 【Project】 -> 【Network】 -> 【Routers】，在右侧列出的路由列表中选择 test-router 进入详细页面；
  * 看到 (da206956-01) 的接口状态为 **DOWN**；
  * 恢复后，接口状态为 **UP**；
  * 在云主机中 ping 外网地址，可以 ping 通，网络恢复正常。

* **备注**：在该场景下，发现云主机无法 ping 通外网时，应先检查以下内容：

  1. 路由是否连接了外网？如果未连接，连接即可；
  1. 内网、外网的端口状态是否都为 "ACTIVE"？如果不是，将状态 update 为 ACTIVE 即可；
  1. 如果以上均没有问题，则问题与平台本身无关。

##### 场景 No.2: 虚拟机无法通过 DHCP 方式获取 IP 地址

* 故障描述：

  登录虚拟机，查看 IP 地址等网络信息，处于未配置状态。

* 测试准备：

  1. 登录 Controller 节点，执行命令：

    ```
    # pcs resource ...

    ```
  1. 创建一台云主机，通过 DHCP 方式为云主机分配 IP 地址；
  1. 打开云主机的控制台，执行 `ip addr` 查看 IP 地址信息，看到没有分配 IP 地址。


* 测试步骤：

  1. 登录到 Controller 节点，查看 dhcp-agent 状态。。。
  1. 恢复 dhcp-agent。。。。

* 预期结果：

  * 

##### 场景 No.3: 所有租户的所有虚拟机无法连接外网

* 故障描述：

  登录所有租户的任意一台虚拟机，ping 公网任意一个 IP 地址，ping 不通。

* 测试准备：

  1. 切断外网

* 测试步骤：

* 预期结果：

##### 场景 No.4: 同一租户下两台虚拟机网络流量很高，导致所有租户的网络受到影响

* 故障描述：

  登录任意一台虚拟机，ping 其它节点或外网延迟非常大，丢包率非常高。

* 测试准备：

* 测试步骤：

* 预期结果：

##### 场景 No.5: 虚拟机限速时，在该虚拟机向外发包，其它租户的虚拟机的网络受到影响

* 故障描述：

  登录任意一台虚拟机，ping 其它节点或外网延迟非常大，丢包率非常高。

* 测试准备：

* 测试步骤：

* 预期结果：

##### 场景 No.6: 大于或等于 N/2 台 Controller 节点宕机( N 为 Controller 节点总数)

* 故障描述：

  * MySQL 集群故障
  * Dashboard 无法访问

* 测试准备：

  1. 切断 2 台 Controller 节点的电源；

* 测试步骤：

  1. 重启所有宕机的 Controller 节点；
  1. 等待大约 5 分钟，在任意一台 Controller 节点上执行命令 `pcs resource`；
  1. 查看输出的信息，确认 pacemaker 集群中所有资源处于 "Started" 状态；
  1. 如果某些资源在某个节点处于 "Stop" 状态，可以使用 `pcs resource ban <resource_name> <node_name>` 及 `pcs resource clear <resource_name> <node_name>` 尝试重启该资源；
  1. 如果某些资源在某个节点处于 "unmanaged" 状态，可登录该节点，使用 `pcs resource cleanup <resource_name>` 尝试重启该资源。

* 预期结果：

  * 节点重启后，如果没问题，所有资源的状态应为 "Started"，执行 `pcs resource` 结果如下：

    ```
    # pcs resource
    vip__public    (ocf::mirantis:ns_IPaddr2): Started 
    Clone Set: clone_ping_vip__public [ping_vip__public]
    Started: [ node-5.eayun.com node-6.eayun.com node-8.eayun.com ]
    vip__management    (ocf::mirantis:ns_IPaddr2): Started 
    Clone Set: clone_p_openstack-heat-engine [p_openstack-heat-engine]
    Started: [ node-5.eayun.com node-6.eayun.com node-8.eayun.com ]
    p_openstack-ceilometer-central (ocf::mirantis:ceilometer-agent-central):   Started 
    p_openstack-ceilometer-alarm-evaluator (ocf::mirantis:ceilometer-alarm-evaluator): Started 
    Clone Set: clone_p_neutron-openvswitch-agent [p_neutron-openvswitch-agent]
    Started: [ node-5.eayun.com node-6.eayun.com node-8.eayun.com ]
    p_neutron-dhcp-agent   (ocf::mirantis:neutron-agent-dhcp): Started 
    Clone Set: clone_p_neutron-metadata-agent [p_neutron-metadata-agent]
    Started: [ node-5.eayun.com node-6.eayun.com node-8.eayun.com ]
    Clone Set: clone_p_neutron-l3-agent [p_neutron-l3-agent]
    Started: [ node-5.eayun.com node-6.eayun.com node-8.eayun.com ]
    Clone Set: clone_p_mysql [p_mysql]
    Started: [ node-5.eayun.com node-6.eayun.com node-8.eayun.com ]
    Clone Set: clone_p_rabbitmq-server [p_rabbitmq-server]
    Started: [ node-5.eayun.com node-6.eayun.com node-8.eayun.com ]
    Clone Set: clone_p_haproxy [p_haproxy]
    Started: [ node-5.eayun.com node-6.eayun.com node-8.eayun.com ]
    Clone Set: clone_p_neutron-lbaas-agent [p_neutron-lbaas-agent]
    Started: [ node-5.eayun.com node-6.eayun.com node-8.eayun.com ]
    ```
  * 如果某些资源在某个节点处于 "Stop" 状态，使用 `pcs resource ban <resource_name> <node_name>` 及 `pcs resource clear <resource_name> <node_name>` 尝试重启该资源后，该资源将重启，状态为 "Started"；
  * 如果某些资源在某个节点处于 "unmanaged" 状态，登录该节点，使用 `pcs resource cleanup <resource_name>` 尝试重启该资源后，该资源将重启，状态为 "Started"。

* **备注**：

  * 本次测试针对 EayunStack 现有的测试环境进行测试，架构为 3 台 Controller 节点，因此测试准备中切断 2 台 Controller 节点的电源。

##### 场景 No.7: Compute 节点宕机，环境中可用资源可满足该节点上的虚拟机重启

* 故障描述：

  Compute 节点宕机，运行在该节点上的虚拟机宕机，环境中可用资源满足宕掉的虚拟机重启。

* 测试准备：

  1. 切断一台运行着云主机的 Compute 节点的电源；
  1. 要保证环境中 Compute 节点的可用资源足够恢复该切断电源的 Compute 节点上的云主机。

* 测试步骤：

* 预期结果：

##### 场景 No.8: Compute 节点宕机，环境中可用资源不能满足该节点上的虚拟机重启

* 故障描述：

  Compute 节点宕机，运行在该节点上的虚拟机宕机，环境中可用资源无法满足重新启动宕掉的虚拟机的需求。

* 测试准备：

  1. 切断一台运行着云主机的 Compute 节点的电源；
  1. 剩下的环境中的 Compute 节点的可用资源无法满足恢复该切断电源的 Compute 节点上的云主机。

* 测试步骤：

* 预期结果：

##### 场景 No.9: 某些虚拟机出现磁盘 I/O 错误，Ceph 集群报错

* 故障描述：

  某些虚拟机出现磁盘 I/O 错误，Ceph 集群报错。

* 测试准备：

  1. 同时切断三台或三台以上 Ceph-osd 节点的电源。

* 测试步骤：

* 预期结果：

##### 场景 No.10: Ceilometer 服务不可用，报数据库连接错误

* 故障描述：

  Ceilometer 服务不可用，报数据库连接错误。

* 测试准备：

  1. 切断 Mongo 节点的电源。

* 测试步骤：

* 预期结果：

##### 场景 No.11: 所有 OpenStack 节点 NTP 同步失败

* 故障描述：

  所有 OpenStack 节点 NTP 同步失败，Fuel Master 节点宕机或 NTP 服务停止。

* 测试准备：

  1. 停止 Fuel Master 节点的 NTP 服务，执行命令 `systemctl stop ntpd`。

* 测试步骤：

  1. 登录 Fuel Master 节点；
  1. 执行命令 `systemctl status ntpd` 查看 NTP 服务的状态，看到状态为 "Inactive"；
  1. 重启 NTP 服务，执行命令 `systemctl restart ntpd`。

* 预期结果：

  * NTP 服务恢复；
  * 执行命令 `systemctl status ntpd` 查看 NTP 服务的状态，看到状态为 "Active"；
  * OpenStack 节点 NTP 同步成功。

* **备注**：

  * 如果故障原因为 Fuel Master 节点宕机，重启 Fuel Master 节点，并确认 NTP 服务状态为 "Active" 即可；
  * 若重启后 NTP 服务异常，可根据测试步骤中的操作恢复 NTP 服务。

##### 场景 No.12: MySQL 集群故障

* 故障描述：

  任意 OpenStack 组件连接数据库失败，日志中报数据库连接错误。

* 测试准备：

* 测试步骤：

* 预期结果：

##### 场景 No.13: RabbitMQ 集群故障

* 故障描述：

  任意 OpenStack 组件连接 RabbitMQ 失败，日志中报 rabbitmq 连接错误。

* 测试准备：

  1. 切断 1 台 Controller 节点的管理网络；

* 测试步骤：

* 预期结果：

##### 场景 No.14: Ceph 集群故障，数据未丢失

* 故障描述：

  Ceph 集群故障，数据未丢失。

* 测试准备：

  1. 登录到 Ceph-osd 节点；
  1. 关闭 osd 实例(即实例对应的后台服务)：

    ```
    xxx
    ```

* 测试步骤：

* 预期结果：

##### 场景 No.15: Ceph 集群故障，数据丢失

* 故障描述：

  Ceph 集群故障，数据丢失。

* 测试准备：

* 测试步骤：

* 预期结果：

