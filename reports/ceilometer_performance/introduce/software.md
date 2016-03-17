# Ceilometer 软件支撑

## 数据库软件

Ceilometer 所收集数据存储在数据库中，支持的数据库包括（MongoDB, MySQL, PostgreSQL, HBase, DB2)。

EayunStack 平台通过 Fuel 安装，安装时，我们所选择的数据库为 MongoDB。

## Ceilometer 模块软件

* **openstack-ceilometer-common**: 提供 Ceilometer 数据与消费。
* **openstack-ceilometer-collector**: Ceilometer 的核心组件，监听 Message Bus，将收集到的数据写入数据库，同时对收集到的其它服务发来的 notification 消息本地处理，然后重新发送到 Message Bus 中去，随后再被其收集。
* **openstack-ceilometer-api**: 提供 Ceilometer API 服务。
* **openstack-ceilometer-alar**: 提供 Ceilometer 警告通知与警告评估。
* **openstack-ceilometer-notification**: 提供 Ceilometer 通告代理，并将 EayunStack 服务的各种数据推送到收集中心。
* **openstack-ceilometer-central**: Central Agent 代理，运行在控制节点上，它主要收集其它服务 (Image, Volume, Network) 信息。

## 计算节点需要安装的软件

* **openstack-ceilometer-compute**: 提供 openstack compute 代理与 compute 服务，每一个计算节点都运行一个 Compute Agent，该 Agent 通过 Stevedore 管理 pollster 插件，获取虚拟机 CPU, Disk IO, Network IO, Instance 消息。
