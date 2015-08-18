# 灾难场景

```
* 场景N： * * *

* 故障等级：

* 现象描述：

* 故障模拟方案

* 故障原因：
1）
2）
3）
。。。
N）

* 恢复方案：
1）排查方法
2）解决方法

* 预计故障恢复时间

  排查&解决问题所用的总时间
```

#### 场景 No.1：某个租户所有虚拟机无法连接外网

* 故障等级：

* 现象描述：

  * 登录某个租户的任意一台虚拟机，ping公网任意一个IP地址，不通。

* 故障模拟方案

* 故障原因：

  * 路由未连接外网；
  * 或内网、外网的端口状态为 **DOWN**；

* 恢复方案：

  * 排查方法
    
    * 登录到 Controller 节点，执行命令 `neutron router-show <router_name>`，其中 \<router\_name\> 为对应的路由名称，查看该路由的状态；
    * 也可以登录 dashboard 后，点击 【Project】 -> 【Network】 -> 【Routers】，在右侧列出的路由列表中选择对应的路由进入详细页面，查看接口的状态。
    
  * 解决方法

    1. 登录 Controller 节点；
    1. 执行命令 `neutron router-update <router_name> --admin_state_up True`，恢复路由状态为 **UP**；
    1. 执行命令 `neutron router-show <router_name>` 确认路由状态是否恢复正常。

* 预计故障恢复时间

===

#### 场景 No.2：虚拟机无法通过DHCP方式获取IP地址

* 故障等级：

* 现象描述：

  * 登录虚拟机，查看IP地址等网络信息，处于未配置状态。

* 故障模拟方案

* 故障原因：

  * DHCP 代理故障。

* 恢复方案：

  * 排查方法
    
    * 登录 Controller 节点，执行命令 `pcs resource`，查看 p_neutron-dhcp-agent 服务的状态，如果为 "Stopped"，说明 DHCP 代理故障。
    
  * 解决方法

    1. 登录到 Controller 节点，执行命令 `pcs resource enable p_neutron-dhcp-agent`，重启 dhcp-agent 服务；
    1. 打开云主机控制台，重启网络或通过 DHCP 获取 IP 后，执行 `ip addr` 查看 IP 地址信息，确认能够获取到地址。

* 预计故障恢复时间

===

#### 场景 No.3：所有租户的所有虚拟机无法连接外网

* 故障等级：

* 现象描述：

  * 登录所有租户的任意一台虚拟机，ping公网任意一个IP地址，不通。

* 故障模拟方案

* 故障原因：

  * 环境外网被切断。

* 恢复方案：

  * 排查方法
    
    * 检查外网网络是否正常。
    
  * 解决方法

    * 恢复外网网络。

* 预计故障恢复时间

* **备注**：

  目前的环境暂时无法模拟。

===

#### 场景 No.4：同一租户下两台虚拟机网络流量很高，导致所有租户的网络受到影响

* 故障等级：

* 现象描述：

  * 登录任意一台虚拟机，ping其它节点或外网延迟非常大，丢包率非常高。

* 故障模拟方案

* 故障原因：

  * 环境中某一台或多台虚拟机向外发送大量数据包，占用了大量网络带宽。

* 恢复方案：

  * 排查方法
    
    * 
    
  * 解决方法

    * 

* 预计故障恢复时间

* **备注**：

  目前的环境暂时无法模拟。

===

#### 场景 No.5：虚拟机限速时，在该虚拟机向外发包，其它租户的虚拟机的网络受到影响

* 故障等级：

* 现象描述：

  * 登录任意一台虚拟机，ping其它节点或外网延迟非常大，丢包率非常高。

* 故障模拟方案

* 故障原因：

  * 环境中某一台或多台被限速的虚拟机向外发送大量的数据包，占用了大量带宽。

* 恢复方案：

  * 排查方法
    
    * 
    
  * 解决方法

    * 

* 预计故障恢复时间

* **备注**：

  目前的环境暂时无法模拟。

===

#### 场景 No.6(已测试通过)：DashBoard无法访问，监控系统发现大于或等于 N/2 台 Controller 节点宕机（N为Controller节点总数）

* 故障等级：

* 现象描述：

  * DashBoard无法访问，监控系统发现大于或等于 N/2 台 Controller 节点宕机（N为Controller节点总数）

* 故障模拟方案：

  同时切断大于或等于 N/2 台 Controller 节点的电源。

* 故障原因：

  * 环境中 N/2 台 Controller 节点宕机（N为Controller节点总数）

* 恢复方案：

  * 排查方法
    
    * 根据监控系统确认当前运行的 Controller 节点数量是否小于 N/2 台（N为Controller节点总数）
    
  * 解决方法

    * 重新启动所有宕机的 Controller 节点
    * 等待大约5分钟后，在任意一台 Controller 节点上使用 ```# pcs resource```命令确认 pacemaker 集群中所有资源处于 Started 状态。如下所示：
    ```
    # pcs resource
     vip__public	(ocf::mirantis:ns_IPaddr2):	Started 
     Clone Set: clone_ping_vip__public [ping_vip__public]
         Started: [ node-5.eayun.com node-6.eayun.com node-8.eayun.com ]
     vip__management	(ocf::mirantis:ns_IPaddr2):	Started 
     Clone Set: clone_p_openstack-heat-engine [p_openstack-heat-engine]
         Started: [ node-5.eayun.com node-6.eayun.com node-8.eayun.com ]
     p_openstack-ceilometer-central	(ocf::mirantis:ceilometer-agent-central):	Started 
     p_openstack-ceilometer-alarm-evaluator	(ocf::mirantis:ceilometer-alarm-evaluator):	Started 
     Clone Set: clone_p_neutron-openvswitch-agent [p_neutron-openvswitch-agent]
         Started: [ node-5.eayun.com node-6.eayun.com node-8.eayun.com ]
     p_neutron-dhcp-agent	(ocf::mirantis:neutron-agent-dhcp):	Started 
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
    * 如有某些资源在某个节点处于 Stoped 状态，可使用```pcs resource ban 资源名 节点主机名```及```pcs resource clear 资源名 节点主机名```尝试启动该资源。
    * 如果某些资源在某个节点处于 unmanaged 状态，可登陆该节点，使用```pcs resource cleanup 资源名```尝试重新启动该资源。

* 预计故障恢复时间

===

#### 场景 No.7：环境中多台云主机同时宕机，监控系统发现 Compute 节点宕机

***测试时boot-from-image类型的虚拟机迁移失败，原因为compute节点断电后ceph中存在关于该虚拟机的rbd client。该类型的虚拟机迁移成功的前提是在compute节点断电后约10分钟后，确认对应 rbd client消失后，执行迁移即可成功。该问题还需要讨论研究。***

* 故障等级：

* 现象描述：

  * 环境中多台云主机宕机，监控系统发现 Compute 节点宕机

* 故障模拟方案

  切断一台 Compute 节点电源。

* 故障原因：

  * Compute 节点宕机

* 恢复方案：

  * 排查方法
    
    * 通过监控系统确认 Compute 节点已经宕机
    
  * 解决方法
 
    * 执行命令```nova host-evacuate 宕机节点主机名```，将运行在宕机的 Compute 节点上的所有云主机迁移到其他节点
    * 确认所有虚拟机已迁移成功

* 预计故障恢复时间

===

#### No.8：某些虚拟机出现磁盘I/O错误，Ceph集群报错

* 故障等级：

* 现象描述：

  * 某些虚拟机出现磁盘I/O错误，Ceph集群报错。

* 故障模拟方案：

  备份某个rbd，然后找到这个 rbd 对应的 object 列表，删除（或者 mv）其中一个 object （包括这个 object 的所有镜像）。同时切断三台或三台以上 Ceph-osd 节点的电源。

* 故障原因：

  * 大于或等于三台 Ceph-osd 节点宕机，rbd中有object丢失或损坏。

* 恢复方案：

  * 排查方法
    
    * 通过监控系统确认大于或等于三台 Ceph-osd 节点宕机
    
  * 解决方法

    * 将 Ceph-osd 节点重启
    * 确认是否有 object 无法恢复，如有 object 无法恢复，恢复无法恢复的 object。

* 预计故障恢复时间

===

#### 场景 No.9（已测试通过）：Ceilometer 服务不可用，报数据库连接错误。

* 故障等级：

* 现象描述：

  * Ceilometer 服务不可用，报数据库连接错误。

* 故障模拟方案：

  切断 Mongo 节点电源

* 故障原因：

  * Mongo节点宕机

* 恢复方案：

  * 排查方法
    
    * 通过监控系统确认 Mongo 节点已经宕机
    * 登陆任意 Controller 节点，在 /var/log/ceilometer/api.log 日志中，发现类似如下错误日志：
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
    
  * 解决方法

    * 重启 Mongo 节点，确认 mongod 服务正常运行

* 预计故障恢复时间

===

#### 场景 No.10（已测试通过）：所有 OpenStack 节点NTP同步失败

* 故障等级：

* 现象描述：

  * 所有 OpenStack 节点NTP同步失败。

* 故障模拟方案:

  停止 Fuel 节点 NTP 服务```# systemctl stop ntpd```

* 故障原因：

  * Fuel 节点 NTP 服务停止，无法向 OpenStack 节点提供 NTP 服务

* 恢复方案：

  * 排查方法
    
    * 登陆 Fuel 节点，查看 NTP 服务状态```systemctl status ntpd```
    
  * 解决方法

    * 重启 NTP 服务，使 NTP 服务恢复 active (running) 状态。

* 预计故障恢复时间

#### 场景 No.11：MySQL 集群故障

* 故障等级：

* 现象描述：

  * 任意 OpenStack 组件连接数据库失败，日志中报数据库连接错误。

* 故障模拟方案：

  

* 故障原因：

  * 

* 恢复方案：

  * 排查方法
    
    * 
    
  * 解决方法

    * 

* 预计故障恢复时间

===

#### 场景 No.12：RabbitMQ 集群故障

* 故障等级：

* 现象描述：

  * 任意 OpenStack 组件连接 RabbitMQ 失败，日志中报 rabbitmq 连接错误。

* 故障模拟方案：

  通过人为切断某些 Controller 节点的管理网络来破坏 RabbitMQ 集群内部通讯，从而打乱集群。

* 故障原因：

  * RabbitMQ 集群各节点间无法正常通讯。

* 恢复方案：

  * 排查方法
    
    * 在 Controller 节点查看 RabbitMQ 集群状态，执行命令 `pcs resource`，如果集群状态正常，将看到集群内的所有节点均在 "Started" 列表中，输出如下：

    ```
    # pcs resource
    ...
     Clone Set: clone_p_rabbitmq-server [p_rabbitmq-server]
         Started: [ node-5.eayun.com node-6.eayun.com node-8.eayun.com ]
    ...
    ```
    * 如果想要进一步查看集群状态，可以在 Controller 节点执行命令 `rabbitmqctl cluster_status`，集群状态正常时，所有集群内的节点均在 "running_nodes" 列表中，输出如下：

    ```
    # rabbitmqctl cluster_status
    Cluster status of node 'rabbit@node-6' ...
    [{nodes,[{disc,['rabbit@node-5','rabbit@node-6','rabbit@node-8']}]},
     {running_nodes,['rabbit@node-5','rabbit@node-8','rabbit@node-6']},
     {cluster_name,<<"rabbit@node-6.eayun.com">>},
     {partitions,[]}]
    ...done.
    ```

    > ###### 说明：
    > 当集群状态异常时，通过上述命令查看集群状态，可以看到故障节点不在 "Started" 或 "running_nodes" 列表中。

  * 解决方法

    * 判断哪台 Controller 节点故障，恢复故障节点的网络环境后，重启其上的 RabbitMQ 服务，执行命令 `pcs resource ban p_rabbitmq-server <node_name>` 及 `pcs resource clear p_rabbitmq-server <node_name>`；
    * 集群重启后，重启故障节点上的所有 OpenStack 服务：

    ```
    # pcs resource disable/enable clone_p_neutron-lbaas-agent
    # pcs resource disable/enable clone_p_neutron-lbaas-agent
    # pcs resource disable/enable clone_p_neutron-l3-agent
    # pcs resource disable/enable clone_p_neutron-metadata-agent
    # pcs resource disable/enable p_neutron-dhcp-agent
    # pcs resource disable/enable clone_p_neutron-openvswitch-agent
    # pcs resource disable/enable clone_p_openstack-heat-engine
    # openstack-service restart
    ```

* **备注**：

  RabbitMQ 集群故障的原因可能很多(管理网络断开是其中之一)，但最终表现为集群异常。故障原因可能包括：

  * 某台 Controller 节点与其他 Controller 节点无法通信(管理网络异常)；
  * RabbitMQ 相关进程异常；
  * 。。。

* 预计故障恢复时间

===

#### 场景 No.13：Ceph 集群故障，数据丢失

* 故障等级：

* 现象描述：

  * Ceph 集群故障，数据丢失

* 故障模拟方案

因为 Ceph 集群中的 object 都对应文件系统的文件，可以通过删除（或者 mv）其中一个 object （包括这个 object 的所有镜像）来实现，当然这样大体的方案，具体测试还需要一些准备，比如确定只针对一个 rbd 来进行测试，首先要对这个 rbd 进行备份，然后找到这个 rbd 对应的 object 列表，选择其中一个 object 进行破坏性测试（如上）。

* 故障原因：

  * 

* 恢复方案：

  * 排查方法
    
    * 
    
  * 解决方法

    * 

* 预计故障恢复时间


