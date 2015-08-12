# 灾难恢复模拟场景

#### 场景 No.1: 某个租户所有云主机无法连接外网

* 故障描述：

  登录某个租户的任意一台云主机，ping 公网任意一个 IP 地址，ping 不通。

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
  1. 打开该租户中其中一台云主机的控制台，ping 外网地址，提示："Destination Net Unreachable"。

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

#### 场景 No.2: 云主机无法通过 DHCP 方式获取 IP 地址

* 故障描述：

  登录云主机，查看 IP 地址等网络信息，处于未配置状态。

* 测试准备：

  1. 登录 Controller 节点，执行命令 `pcs resource disable p_neutron-dhcp-agent`；
  1. 创建一台云主机，通过 DHCP 方式为云主机分配 IP 地址；
  1. 打开云主机的控制台，执行 `ip addr` 查看 IP 地址信息，看到没有分配 IP 地址。

* 测试步骤：

  1. 登录到 Controller 节点，查看 dhcp-agent 状态，执行命令 `pcs resource`，查看 p\_neutron-dhcp-agent 服务的状态；
  1. 恢复 dhcp-agent，执行命令 `pcs resource enable p_neutron-dhcp-agent`，重启 dhcp-agent 服务；
  1. 打开云主机控制台，重启网络或通过 DHCP 获取 IP 后，执行 `ip addr` 查看 IP 地址信息。

* 预期结果：

  * 查看 dhcp-agent 状态时，看到其状态为 "Stopped"；
  * 重启 dhcp-agent 后，状态变为 "Started"；
  * 云主机成功通过 DHCP 获取 IP 地址，查看网络信息看到网络已经正确配置。

#### 场景 No.3: 所有租户的所有云主机无法连接外网

* 故障描述：

  登录所有租户的任意一台云主机，ping 公网任意一个 IP 地址，ping 不通。

* 测试准备：

  1. 切断外网

* 测试步骤：

* 预期结果：

* **备注**：

  * 目前环境中只有 1 个交换机，测试影响较大，暂时不进行测试。

#### 场景 No.4: 同一租户下两台云主机网络流量很高，导致所有租户的网络受到影响

* 故障描述：

  登录任意一台云主机，ping 其它节点或外网延迟非常大，丢包率非常高。

* 测试准备：

  暂时无法模拟

* 测试步骤：

* 预期结果：

#### 场景 No.5: 云主机限速时，在该云主机向外发包，其它租户的云主机的网络受到影响

* 故障描述：

  登录任意一台云主机，ping 其它节点或外网延迟非常大，丢包率非常高。

* 测试准备：

  暂时无法模拟

* 测试步骤：

* 预期结果：

#### 场景 No.6: 大于或等于 N/2 台 Controller 节点宕机( N 为 Controller 节点总数)

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

#### 场景 No.7: Compute 节点宕机，环境中可用资源可满足该节点上的云主机重启

* 故障描述：

  Compute 节点宕机，运行在该节点上的云主机宕机，环境中可用资源满足宕掉的云主机重启。

* 测试准备：

  1. 切断一台运行着**从镜像启动和从卷启动**的云主机的 Compute 节点的电源；
  1. 要保证环境中 Compute 节点的可用资源足够恢复该切断电源的 Compute 节点上的云主机。

* 测试步骤：

  1. 登录到剩余 Compute 节点中的一台；
  1. 执行命令 `nova host-evacuate <compute_node_name>`，其中 \<compute\_node\_name\> 为宕机的 Compute 节点的名称；
  1. 等待，确认所有云主机是否恢复成功。

* 预期结果：

  * 所有云主机在其他 Compute 节点上成功恢复。

#### 场景 No.8: Compute 节点宕机，环境中可用资源不能满足该节点上的云主机重启

* 故障描述：

  Compute 节点宕机，运行在该节点上的云主机宕机，环境中可用资源无法满足重新启动宕掉的云主机的需求。

* 测试准备：

  1. 切断一台运行着**从镜像启动和从卷启动**的云主机的 Compute 节点的电源；
  1. 要保证环境中 Compute 节点的可用资源足够恢复该切断电源的 Compute 节点上的云主机。

* 测试步骤：

  1. 登录到剩余 Compute 节点中的一台；
  1. 执行命令 `nova host-evacuate <compute_node_name>`，其中 \<compute\_node\_name\> 为宕机的 Compute 节点的名称；
  1. 等待，确认所有云主机是否恢复成功。

* 预期结果：

#### 场景 No.9: 某些云主机出现磁盘 I/O 错误，Ceph 集群报错

* 故障描述：

  某些云主机出现磁盘 I/O 错误，Ceph 集群报错。

* 测试准备：

  1. 同时切断三台或三台以上 Ceph-osd 节点的电源。

* 测试步骤：

* 预期结果：

#### 场景 No.10: Ceilometer 服务不可用，报数据库连接错误

* 故障描述：

  Ceilometer 服务不可用，报数据库连接错误。

* 测试准备：

  1. 切断 Mongo 节点的电源；
  1. 登录任意 Controller 节点，在 /var/log/ceilometer/api.log 日志中看到如下错误信息：

    ```
    2015-08-10 10:07:30.347 2816 ERROR wsme.api [-] Server-side error: "could not connect to 172.16.101.11:27017: [Errno 113] EHOSTUNREACH". Detail:
    Traceback (most recent call last):
    File "/usr/lib/python2.7/site-packages/wsmeext/pecan.py", line 77, in callfunction
    result = f(self, *args, **kwargs)
    File "/usr/lib/python2.7/site-packages/ceilometer/api/controllers/v2.py", line 2226, in get_all
    for m in pecan.request.alarm_storage_conn.get_alarms(**kwargs)]
    File "/usr/lib/python2.7/site-packages/ceilometer/alarm/storage/pymongo_base.py", line 200, in _retrieve_alarms
    for alarm in alarms:
    File "/usr/lib64/python2.7/site-packages/pymongo/cursor.py", line 814, in next
    if len(self.__data) or self._refresh():
    File "/usr/lib64/python2.7/site-packages/pymongo/cursor.py", line 763, in _refresh
    self.__uuid_subtype))
    File "/usr/lib64/python2.7/site-packages/pymongo/cursor.py", line 700, in __send_message
    **kwargs)
    File "/usr/lib64/python2.7/site-packages/pymongo/mongo_client.py", line 985, in _send_message_with_response
    sock_info = self.__socket()
    File "/usr/lib64/python2.7/site-packages/pymongo/mongo_client.py", line 720, in __socket
    host, port = self.__find_node()
    File "/usr/lib64/python2.7/site-packages/pymongo/mongo_client.py", line 713, in __find_node
    raise AutoReconnect(', '.join(errors))
    AutoReconnect: could not connect to 172.16.101.11:27017: [Errno 113] EHOSTUNREACH
    ```

* 测试步骤：

  1. 确认 Mongo 节点已经宕机；
  1. 重启 Mongo 节点，重启后，登录到 Mongo 节点，确认 mongod 服务的状态，执行命令 `systemctl status mongod`；
  1. 登录到 Controller 节点，确认 Ceilometer 代理的状态，执行命令 `pcs resource`。

* 预期结果：

  * Mongo 节点启动后，mongod 服务状态为 "active"；
  * Ceilometer 代理的状态为 "Started"；
  * Ceilometer 服务恢复正常，可以使用。

* **备注**：

  * 如果登录到 Controller 节点进行确认，Ceilometer 代理没有正常启动，请使用相关命令重启该服务；
  * Ceilometer 在 Controller 节点上的代理没有启动不会影响 Ceilometer 的正常**使用**，但会影响**数据的收集**。

#### 场景 No.11: 所有 OpenStack 节点 NTP 同步失败

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

#### 场景 No.12: MySQL 集群故障

* 故障描述：

  任意 OpenStack 组件连接数据库失败，日志中报数据库连接错误。

* 测试准备：

* 测试步骤：

* 预期结果：

#### 场景 No.13: RabbitMQ 集群故障

* 故障描述：

  任意 OpenStack 组件连接 RabbitMQ 失败，日志中报 rabbitmq 连接错误。

###### RabbitMQ 集群的单个节点故障

* 测试准备：

  1. 切断 1 台 Controller 节点的管理网络；

* 测试步骤：

  1. 登录到 Controller 节点，确认 RabbitMQ 集群服务状态，执行命令 `pcs resource`；
  1. 进一步确认集群中节点的状态，执行命令 `rabbitmqctl cluster_status`；
  1. 找到故障节点后，恢复该节点，执行命令 `pcs resource ban p_rabbitmq-server <node_name>` 及 `pcs resource clear p_rabbitmq-server <node_name>`；
  1. 登录刚恢复的故障节点，重启 OpenStack 的各服务：

    ```
    pcs resource disable/enable clone_p_neutron-lbaas-agent
    pcs resource disable/enable clone_p_neutron-lbaas-agent
    pcs resource disable/enable clone_p_neutron-l3-agent
    pcs resource disable/enable clone_p_neutron-metadata-agent
    pcs resource disable/enable p_neutron-dhcp-agent
    pcs resource disable/enable clone_p_neutron-openvswitch-agent
    pcs resource disable/enable clone_p_openstack-heat-engine
    systemctl restart neutron-server openstack-nova-api openstack-nova-cert\
    openstack-nova-conductor openstack-nova-consoleauth openstack-nova-novncproxy\
    openstack-nova-objectstore openstack-nova-scheduler openstack-cinder-api\
    openstack-cinder-volume openstack-cinder-scheduler openstack-heat-api-cfn\
    openstack-heat-api-cloudwatch openstack-heat-api openstack-keystone\
    openstack-glance-api openstack-glance-registry
    ```

* 预期结果：

  * 确认集群状态时，发现有 1 台节点不在 Started 列表中，显示如下(本实验切断了 node-5 的管理网络)：

    ```
    # pcs resource
    ...
     Clone Set: clone_p_rabbitmq-server [p_rabbitmq-server]
         Started: [ node-6.eayun.com node-8.eayun.com ]    # node-5 不在列表中
    ...

    # rabbitmqctl cluster_status
    Cluster status of node 'rabbit@node-6' ...
    [{nodes,[{disc,['rabbit@node-5','rabbit@node-6','rabbit@node-8']}]},
     {running_nodes,['rabbit@node-8','rabbit@node-6']},    # node-5 不在列表中
     {cluster_name,<<"rabbit@node-6.eayun.com">>},
     {partitions,[]}]
    ...done.

    ```
  * 节点恢复后，执行命令 `pcs resource`，看到 p_rabbitmq-server 的 Started 列表中包含了所有 Controller 节点，显示如下：

    ```
    # pcs resource
    ...
     Clone Set: clone_p_rabbitmq-server [p_rabbitmq-server]
         Started: [ node-5.eayun.com node-6.eayun.com node-8.eayun.com ]
    ...
    
    # rabbitmqctl cluster_status
    Cluster status of node 'rabbit@node-6' ...
    [{nodes,[{disc,['rabbit@node-5','rabbit@node-6','rabbit@node-8']}]},
     {running_nodes,['rabbit@node-5','rabbit@node-8','rabbit@node-6']},
     {cluster_name,<<"rabbit@node-6.eayun.com">>},
     {partitions,[]}]
    ...done.
    ```
  * 集群恢复并重启服务后，组件连接 RabbitMQ 正常，日志中不出现报错现象。

* **备注**：

  * 导致 RabbitMQ 集群故障的可能有很多种，在此仅模拟了其中一种情况；
  * 无论故障原因为何，对于 RabbitMQ 集群故障的恢复方法是一样的。

###### RabbitMQ 集群的多个节点故障

* 测试准备：

  1. 切断大于 1 台数目的 Controller 节点的管理网络。

* 测试步骤：

  1. 登录到 Controller 节点，确认 RabbitMQ 集群服务状态，执行命令 `pcs resource`；
  1. 进一步确认集群中节点的状态，执行命令 `rabbitmqctl cluster_status`；
  1. 找到故障节点后，依次停止所有故障节点上的 RabbitMQ 资源，执行命令 `pcs resource ban p_rabbitmq-server <node_name>`，将其中的 \<node\_name\> 替换为各个故障节点的名称；
  1. (如果所有 Controller 节点管理网络故障，那么)**首先恢复其中一台节点**，执行命令 `pcs resource clear p_rabbitmq-server <first_node_name>`；
  1. 执行命令 `pcs resource`，确认第一台节点是否恢复，确认恢复后，继续执行命令 `pcs resource clear p_rabbitmq-server <node_name>`，恢复其他故障节点；
  1. 恢复完成后，确认集群状态，执行命令 `rabbitmqctl cluster_status`；
  1. 登录恢复的故障节点，重启 OpenStack 的各服务：

    ```
    pcs resource disable/enable clone_p_neutron-lbaas-agent
    pcs resource disable/enable clone_p_neutron-lbaas-agent
    pcs resource disable/enable clone_p_neutron-l3-agent
    pcs resource disable/enable clone_p_neutron-metadata-agent
    pcs resource disable/enable p_neutron-dhcp-agent
    pcs resource disable/enable clone_p_neutron-openvswitch-agent
    pcs resource disable/enable clone_p_openstack-heat-engine
    systemctl restart neutron-server openstack-nova-api openstack-nova-cert\
    openstack-nova-conductor openstack-nova-consoleauth openstack-nova-novncproxy\
    openstack-nova-objectstore openstack-nova-scheduler openstack-cinder-api\
    openstack-cinder-volume openstack-cinder-scheduler openstack-heat-api-cfn\
    openstack-heat-api-cloudwatch openstack-heat-api openstack-keystone\
    openstack-glance-api openstack-glance-registry
    ```

* 预期结果：

  * 确认集群状态时，发现有 N 台节点不在 Started 列表中，显示如下

    ```
    # pcs resource
    ...
     Clone Set: clone_p_rabbitmq-server [p_rabbitmq-server]
         Started: [ node-8.eayun.com ]    # node-5 和 node-6 不在列表中
    ...

    # rabbitmqctl cluster_status
    Cluster status of node 'rabbit@node-8' ...
    [{nodes,[{disc,['rabbit@node-5','rabbit@node-6','rabbit@node-8']}]},
     {running_nodes,['rabbit@node-8']},    # node-5 和 node-6 不在列表中
     {cluster_name,<<"rabbit@node-8.eayun.com">>},
     {partitions,[]}]
    ...done.
    ```
  * 所有节点恢复后，执行命令 `pcs resource`，看到 p\_rabbitmq-server 的 Started 列表中包含了所有 Controller 节点；

    ```
    # pcs resource
    ...
     Clone Set: clone_p_rabbitmq-server [p_rabbitmq-server]
         Started: [ node-5.eayun.com node-6.eayun.com node-8.eayun.com ]
    ...
    
    # rabbitmqctl cluster_status
    Cluster status of node 'rabbit@node-8' ...
    [{nodes,[{disc,['rabbit@node-5','rabbit@node-6','rabbit@node-8']}]},
     {running_nodes,['rabbit@node-5','rabbit@node-8','rabbit@node-6']},
     {cluster_name,<<"rabbit@node-8.eayun.com">>},
     {partitions,[]}]
    ...done.
    ```
  * 集群恢复并重启服务后，组件连接 RabbitMQ 正常，日志中不出现报错现象。

* **注意**：

  * 多台 RabbitMQ 节点故障的情况中，由于选举机制，必需先恢复 1 台节点后，再恢复其他故障节点，否则可能导致集群故障。

* **说明**：

  * 由于目前环境仅有 3 台 Controller 节点，切断多台 Controller 节点的管理网络的表现与多台 Controller 节点宕机相同，因此不作重复测试。

#### 场景 No.14: Ceph 集群故障，数据未丢失

* 故障描述：

  Ceph 集群故障，数据未丢失。

* 测试准备：

  1. 登录到 Ceph-osd 节点；
  1. 关闭 osd 实例(即实例对应的后台服务)，执行命令 `/etc/init.d/ceph stop osd.0`；

* 测试步骤：

* 预期结果：

#### 场景 No.15: Ceph 集群故障，数据丢失

* 故障描述：

  Ceph 集群故障，数据丢失。

* 测试准备：

* 测试步骤：

* 预期结果：

