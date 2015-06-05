# OpenStack组件检测

该命令用于对EayunStack环境中各节点上运行的OpenStack组件进行检测。在不同角色的节点上执行该命令时所检测的组件及检测内容不同，具体见下表：

|节点角色|检测组件|检测内容|
|----|----|----|
|controller|Keystone</br>Glance</br>Nova</br>Neutron</br>Cinder|配置文件正确性检测</br>服务运行状态检测</br>服务与数据库的连通性检测</br>服务可用性检测|
|compute|Nova|配置文件正确性检测</br>服务运行状态检测|
|mongo|Mongo|配置文件正确性检测</br>服务运行状态检测|
|ceph-osd|Ceph|配置文件正确性检测</br>服务运行状态检测|

## 命令格式

```
$ eayunstack doctor stack --help
usage: eayunstack doctor stack [-h] [--profile] [--service] [--controller]
                               [--compute] [--mongo] [--ceph-osd] [-a]
                               [-o FILENAME]

Check OpenStack Compent

optional arguments:
  -h, --help    show this help message and exit
  --profile     Check Profile
  --service     Check Service Status
  --controller  Check All Controller Node
  --compute     Check All Compute Node
  --mongo       Check All Mongo Node
  --ceph-osd    Check All Ceph-osd Node
  -a, --all     Check ALL
  -o FILENAME   Local File To Save Output Info
```

## Controller节点检测

> ###### 注意
> 该命令可以在**Fuel节点**或**Controller节点**上运行。在**Fuel节点**上运行该命令，可以同时对所有Controller节点进行检测。在**Controller节点**上运行该命令，只检测当前节点。

* Fuel节点执行命令

```
[fuel]$ eayunstack doctor stack --controller
[ INFO  ] *************** Role: controller Node: 172.16.100.7  ***************
[ INFO  ] Checking "Keystone" Component
          Profile: /etc/keystone/keystone.conf
[ INFO  ] Checking "Glance" Component
          Profile: /etc/glance/glance-api.conf
          Profile: /etc/glance/glance-registry.conf
[ INFO  ] Checking "Nova" Component
          Profile: /etc/nova/nova.conf
[ INFO  ] Checking "Neutron" Component
          Profile: /etc/neutron/neutron.conf
[ INFO  ] Checking "Cinder" Component
          Profile: /etc/cinder/cinder.conf
[ INFO  ] Checking "Keystone" Component
[ INFO  ] -Service Status
          Service openstack-keystone is running ...
          Service openstack-keystone is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Glance" Component
[ INFO  ] -Service Status
          Service openstack-glance-api is running ...
          Service openstack-glance-api is enabled ...
          Service openstack-glance-registry is running ...
          Service openstack-glance-registry is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Nova" Component
[ INFO  ] -Service Status
          Service openstack-nova-api is running ...
          Service openstack-nova-api is enabled ...
          Service openstack-nova-conductor is running ...
          Service openstack-nova-conductor is enabled ...
          Service openstack-nova-scheduler is running ...
          Service openstack-nova-scheduler is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Neutron" Component
[ INFO  ] -Service Status
          Service neutron-server is running ...
          Service neutron-server is enabled ...
          Service neutron-ovs-cleanup is running ...
          Service neutron-ovs-cleanup is enabled ...
          Service openvswitch is running ...
          Service openvswitch is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Cinder" Component
[ INFO  ] -Service Status
          Service openstack-cinder-api is running ...
          Service openstack-cinder-api is enabled ...
          Service openstack-cinder-scheduler is running ...
          Service openstack-cinder-scheduler is enabled ...
          Service openstack-cinder-volume is running ...
          Service openstack-cinder-volume is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.

[ INFO  ] *************** Role: controller Node: 172.16.100.5  ***************
[ INFO  ] Checking "Keystone" Component
          Profile: /etc/keystone/keystone.conf
[ INFO  ] Checking "Glance" Component
          Profile: /etc/glance/glance-api.conf
          Profile: /etc/glance/glance-registry.conf
[ INFO  ] Checking "Nova" Component
          Profile: /etc/nova/nova.conf
[ INFO  ] Checking "Neutron" Component
          Profile: /etc/neutron/neutron.conf
[ INFO  ] Checking "Cinder" Component
          Profile: /etc/cinder/cinder.conf
[ INFO  ] Checking "Keystone" Component
[ INFO  ] -Service Status
          Service openstack-keystone is running ...
          Service openstack-keystone is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Glance" Component
[ INFO  ] -Service Status
          Service openstack-glance-api is running ...
          Service openstack-glance-api is enabled ...
          Service openstack-glance-registry is running ...
          Service openstack-glance-registry is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Nova" Component
[ INFO  ] -Service Status
          Service openstack-nova-api is running ...
          Service openstack-nova-api is enabled ...
          Service openstack-nova-conductor is running ...
          Service openstack-nova-conductor is enabled ...
          Service openstack-nova-scheduler is running ...
          Service openstack-nova-scheduler is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Neutron" Component
[ INFO  ] -Service Status
          Service neutron-server is running ...
          Service neutron-server is enabled ...
          Service neutron-ovs-cleanup is running ...
          Service neutron-ovs-cleanup is enabled ...
          Service openvswitch is running ...
          Service openvswitch is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Cinder" Component
[ INFO  ] -Service Status
          Service openstack-cinder-api is running ...
          Service openstack-cinder-api is enabled ...
          Service openstack-cinder-scheduler is running ...
          Service openstack-cinder-scheduler is enabled ...
          Service openstack-cinder-volume is running ...
          Service openstack-cinder-volume is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.

[ INFO  ] *************** Role: controller Node: 172.16.100.4  ***************
[ INFO  ] Checking "Keystone" Component
          Profile: /etc/keystone/keystone.conf
[ INFO  ] Checking "Glance" Component
          Profile: /etc/glance/glance-api.conf
          Profile: /etc/glance/glance-registry.conf
[ INFO  ] Checking "Nova" Component
          Profile: /etc/nova/nova.conf
[ INFO  ] Checking "Neutron" Component
          Profile: /etc/neutron/neutron.conf
[ INFO  ] Checking "Cinder" Component
          Profile: /etc/cinder/cinder.conf
[ INFO  ] Checking "Keystone" Component
[ INFO  ] -Service Status
          Service openstack-keystone is running ...
          Service openstack-keystone is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Glance" Component
[ INFO  ] -Service Status
          Service openstack-glance-api is running ...
          Service openstack-glance-api is enabled ...
          Service openstack-glance-registry is running ...
          Service openstack-glance-registry is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Nova" Component
[ INFO  ] -Service Status
          Service openstack-nova-api is running ...
          Service openstack-nova-api is enabled ...
          Service openstack-nova-conductor is running ...
          Service openstack-nova-conductor is enabled ...
          Service openstack-nova-scheduler is running ...
          Service openstack-nova-scheduler is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Neutron" Component
[ INFO  ] -Service Status
          Service neutron-server is running ...
          Service neutron-server is enabled ...
          Service neutron-ovs-cleanup is running ...
          Service neutron-ovs-cleanup is enabled ...
          Service openvswitch is running ...
          Service openvswitch is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Cinder" Component
[ INFO  ] -Service Status
          Service openstack-cinder-api is running ...
          Service openstack-cinder-api is enabled ...
          Service openstack-cinder-scheduler is running ...
          Service openstack-cinder-scheduler is enabled ...
          Service openstack-cinder-volume is running ...
          Service openstack-cinder-volume is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.

```

* Controller节点执行命令

```
[controller]$ eayunstack doctor stack --controller
[ INFO  ] Checking "Keystone" Component
          Profile: /etc/keystone/keystone.conf
[ INFO  ] Checking "Glance" Component
          Profile: /etc/glance/glance-api.conf
          Profile: /etc/glance/glance-registry.conf
[ INFO  ] Checking "Nova" Component
          Profile: /etc/nova/nova.conf
[ INFO  ] Checking "Neutron" Component
          Profile: /etc/neutron/neutron.conf
[ INFO  ] Checking "Cinder" Component
          Profile: /etc/cinder/cinder.conf
[ INFO  ] Checking "Keystone" Component
[ INFO  ] -Service Status
          Service openstack-keystone is running ...
          Service openstack-keystone is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Glance" Component
[ INFO  ] -Service Status
          Service openstack-glance-api is running ...
          Service openstack-glance-api is enabled ...
          Service openstack-glance-registry is running ...
          Service openstack-glance-registry is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Nova" Component
[ INFO  ] -Service Status
          Service openstack-nova-api is running ...
          Service openstack-nova-api is enabled ...
          Service openstack-nova-conductor is running ...
          Service openstack-nova-conductor is enabled ...
          Service openstack-nova-scheduler is running ...
          Service openstack-nova-scheduler is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Neutron" Component
[ INFO  ] -Service Status
          Service neutron-server is running ...
          Service neutron-server is enabled ...
          Service neutron-ovs-cleanup is running ...
          Service neutron-ovs-cleanup is enabled ...
          Service openvswitch is running ...
          Service openvswitch is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Cinder" Component
[ INFO  ] -Service Status
          Service openstack-cinder-api is running ...
          Service openstack-cinder-api is enabled ...
          Service openstack-cinder-scheduler is running ...
          Service openstack-cinder-scheduler is enabled ...
          Service openstack-cinder-volume is running ...
          Service openstack-cinder-volume is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
```

## Compute节点检测

> ###### 注意
> 该命令可以在**Fuel节点**或**Compute节点**上运行。在**Fuel节点**上运行该命令，可以同时对所有Compute节点进行检测。在**Compute节点**上运行该命令，只检测当前节点。

* Fuel节点执行命令

```
[fuel]$ eayunstack doctor stack --compute
[ INFO  ] *************** Role: compute    Node: 172.16.100.12 ***************
[ INFO  ] Checking "Nova" Component
          Profile: /etc/nova/nova.conf
[ INFO  ] Checking "Nova" Component
[ INFO  ] -Service Status
          Service openstack-nova-compute is running ...
          Service openstack-nova-compute is enabled ...

[ INFO  ] *************** Role: compute    Node: 172.16.100.6  ***************
[ INFO  ] Checking "Nova" Component
          Profile: /etc/nova/nova.conf
[ INFO  ] Checking "Nova" Component
[ INFO  ] -Service Status
          Service openstack-nova-compute is running ...
          Service openstack-nova-compute is enabled ...

```

* Compute节点执行命令

```
[compute]$ eayunstack doctor stack --compute
[ INFO  ] Checking "Nova" Component
          Profile: /etc/nova/nova.conf
[ INFO  ] Checking "Nova" Component
[ INFO  ] -Service Status
          Service openstack-nova-compute is running ...
          Service openstack-nova-compute is enabled ...
```

## Mongo节点检测

> ###### 注意
> 该命令可以在**Fuel节点**或**Mongo节点**上运行。在**Fuel节点**上运行该命令，可以同时对所有Mongo节点进行检测。在**Mongo节点**上运行该命令，只检测当前节点。

* Fuel节点执行命令

```
[fuel]$ eayunstack doctor stack --mongo
[ INFO  ] *************** Role: mongo      Node: 172.16.100.11 ***************
[ INFO  ] Checking "Mongo" Component
          Profile: /etc/mongodb.conf
[ INFO  ] Checking "Mongo" Component
[ INFO  ] -Service Status
          Service mongod is running ...
          Service mongod is enabled ...

```

* Mongo节点执行命令

```
[mongo]$ eayunstack doctor stack --mongo
[ INFO  ] Checking "Mongo" Component
          Profile: /etc/mongodb.conf
[ INFO  ] Checking "Mongo" Component
[ INFO  ] -Service Status
          Service mongod is running ...
          Service mongod is enabled ...
```

## Ceph-osd节点检测

> ###### 注意
> 该命令可以在**Fuel节点**或**Ceph-osd节点**上运行。在**Fuel节点**上运行该命令，可以同时对所有Ceph-osd节点进行检测。在**Ceph-osd节点**上运行该命令，只检测当前节点。

* Fuel节点执行命令

```
[fuel]$ eayunstack doctor stack --ceph
[ INFO  ] *************** Role: ceph-osd   Node: 172.16.100.10 ***************
[ INFO  ] Checking "Ceph_osd" Component
          Profile: /etc/ceph/ceph.conf
[ INFO  ] Checking "Ceph_osd" Component
[ INFO  ] -Service Status
          Service ceph is running ...
          Service ceph is enabled ...

[ INFO  ] *************** Role: ceph-osd   Node: 172.16.100.9  ***************
[ INFO  ] Checking "Ceph_osd" Component
          Profile: /etc/ceph/ceph.conf
[ INFO  ] Checking "Ceph_osd" Component
[ INFO  ] -Service Status
          Service ceph is running ...
          Service ceph is enabled ...

[ INFO  ] *************** Role: ceph-osd   Node: 172.16.100.8  ***************
[ INFO  ] Checking "Ceph_osd" Component
          Profile: /etc/ceph/ceph.conf
[ INFO  ] Checking "Ceph_osd" Component
[ INFO  ] -Service Status
          Service ceph is running ...
          Service ceph is enabled ...

[ INFO  ] *************** Role: ceph-osd   Node: 172.16.100.13 ***************
[ INFO  ] Checking "Ceph_osd" Component
          Profile: /etc/ceph/ceph.conf
[ INFO  ] Checking "Ceph_osd" Component
[ INFO  ] -Service Status
          Service ceph is running ...
          Service ceph is enabled ...

```

* Ceph-osd节点执行命令

```
[ceph-osd]$ eayunstack doctor stack --ceph
[ INFO  ] Checking "Ceph_osd" Component
          Profile: /etc/ceph/ceph.conf
[ INFO  ] Checking "Ceph_osd" Component
[ INFO  ] -Service Status
          Service ceph is running ...
          Service ceph is enabled ...
```

## 单独检测配置文正确性

该命令可以单独检测配置文件的正确性，例如只检测Controller节点上各组件的配置文件。

```
[controller]$ eayunstack doctor stack --controller --profile
[ INFO  ] Checking "Keystone" Component
          Profile: /etc/keystone/keystone.conf
[ INFO  ] Checking "Glance" Component
          Profile: /etc/glance/glance-api.conf
          Profile: /etc/glance/glance-registry.conf
[ INFO  ] Checking "Nova" Component
          Profile: /etc/nova/nova.conf
[ INFO  ] Checking "Neutron" Component
          Profile: /etc/neutron/neutron.conf
[ INFO  ] Checking "Cinder" Component
          Profile: /etc/cinder/cinder.conf

```

## 单独检测服务运行状态

该命令可以单独检测服务运行状态，例如只检测Controller节点上各组件服务的运行状态。

```
[controller]$ eayunstack doctor stack --controller --service
[ INFO  ] Checking "Keystone" Component
[ INFO  ] -Service Status
          Service openstack-keystone is running ...
          Service openstack-keystone is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Glance" Component
[ INFO  ] -Service Status
          Service openstack-glance-api is running ...
          Service openstack-glance-api is enabled ...
          Service openstack-glance-registry is running ...
          Service openstack-glance-registry is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Nova" Component
[ INFO  ] -Service Status
          Service openstack-nova-api is running ...
          Service openstack-nova-api is enabled ...
          Service openstack-nova-conductor is running ...
          Service openstack-nova-conductor is enabled ...
          Service openstack-nova-scheduler is running ...
          Service openstack-nova-scheduler is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Neutron" Component
[ INFO  ] -Service Status
          Service neutron-server is running ...
          Service neutron-server is enabled ...
          Service neutron-ovs-cleanup is running ...
          Service neutron-ovs-cleanup is enabled ...
          Service openvswitch is running ...
          Service openvswitch is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Cinder" Component
[ INFO  ] -Service Status
          Service openstack-cinder-api is running ...
          Service openstack-cinder-api is enabled ...
          Service openstack-cinder-scheduler is running ...
          Service openstack-cinder-scheduler is enabled ...
          Service openstack-cinder-volume is running ...
          Service openstack-cinder-volume is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
```

## 检测所有检测对象

> ###### 注意
> 该命令需要在Fuel节点上执行

```
[fuel]# eayunstack doctor stack -a
[ INFO  ] *************** Role: controller Node: 172.16.100.7  ***************
[ INFO  ] Checking "Keystone" Component
          Profile: /etc/keystone/keystone.conf
[ INFO  ] Checking "Glance" Component
          Profile: /etc/glance/glance-api.conf
          Profile: /etc/glance/glance-registry.conf
[ INFO  ] Checking "Nova" Component
          Profile: /etc/nova/nova.conf
[ INFO  ] Checking "Neutron" Component
          Profile: /etc/neutron/neutron.conf
[ INFO  ] Checking "Cinder" Component
          Profile: /etc/cinder/cinder.conf
[ INFO  ] Checking "Keystone" Component
[ INFO  ] -Service Status
          Service openstack-keystone is running ...
          Service openstack-keystone is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Glance" Component
[ INFO  ] -Service Status
          Service openstack-glance-api is running ...
          Service openstack-glance-api is enabled ...
          Service openstack-glance-registry is running ...
          Service openstack-glance-registry is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Nova" Component
[ INFO  ] -Service Status
          Service openstack-nova-api is running ...
          Service openstack-nova-api is enabled ...
          Service openstack-nova-conductor is running ...
          Service openstack-nova-conductor is enabled ...
          Service openstack-nova-scheduler is running ...
          Service openstack-nova-scheduler is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Neutron" Component
[ INFO  ] -Service Status
          Service neutron-server is running ...
          Service neutron-server is enabled ...
          Service neutron-ovs-cleanup is running ...
          Service neutron-ovs-cleanup is enabled ...
          Service openvswitch is running ...
          Service openvswitch is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Cinder" Component
[ INFO  ] -Service Status
          Service openstack-cinder-api is running ...
          Service openstack-cinder-api is enabled ...
          Service openstack-cinder-scheduler is running ...
          Service openstack-cinder-scheduler is enabled ...
          Service openstack-cinder-volume is running ...
          Service openstack-cinder-volume is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.

[ INFO  ] *************** Role: controller Node: 172.16.100.5  ***************
[ INFO  ] Checking "Keystone" Component
          Profile: /etc/keystone/keystone.conf
[ INFO  ] Checking "Glance" Component
          Profile: /etc/glance/glance-api.conf
          Profile: /etc/glance/glance-registry.conf
[ INFO  ] Checking "Nova" Component
          Profile: /etc/nova/nova.conf
[ INFO  ] Checking "Neutron" Component
          Profile: /etc/neutron/neutron.conf
[ INFO  ] Checking "Cinder" Component
          Profile: /etc/cinder/cinder.conf
[ INFO  ] Checking "Keystone" Component
[ INFO  ] -Service Status
          Service openstack-keystone is running ...
          Service openstack-keystone is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Glance" Component
[ INFO  ] -Service Status
          Service openstack-glance-api is running ...
          Service openstack-glance-api is enabled ...
          Service openstack-glance-registry is running ...
          Service openstack-glance-registry is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Nova" Component
[ INFO  ] -Service Status
          Service openstack-nova-api is running ...
          Service openstack-nova-api is enabled ...
          Service openstack-nova-conductor is running ...
          Service openstack-nova-conductor is enabled ...
          Service openstack-nova-scheduler is running ...
          Service openstack-nova-scheduler is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Neutron" Component
[ INFO  ] -Service Status
          Service neutron-server is running ...
          Service neutron-server is enabled ...
          Service neutron-ovs-cleanup is running ...
          Service neutron-ovs-cleanup is enabled ...
          Service openvswitch is running ...
          Service openvswitch is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Cinder" Component
[ INFO  ] -Service Status
          Service openstack-cinder-api is running ...
          Service openstack-cinder-api is enabled ...
          Service openstack-cinder-scheduler is running ...
          Service openstack-cinder-scheduler is enabled ...
          Service openstack-cinder-volume is running ...
          Service openstack-cinder-volume is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.

[ INFO  ] *************** Role: controller Node: 172.16.100.4  ***************
[ INFO  ] Checking "Keystone" Component
          Profile: /etc/keystone/keystone.conf
[ INFO  ] Checking "Glance" Component
          Profile: /etc/glance/glance-api.conf
          Profile: /etc/glance/glance-registry.conf
[ INFO  ] Checking "Nova" Component
          Profile: /etc/nova/nova.conf
[ INFO  ] Checking "Neutron" Component
          Profile: /etc/neutron/neutron.conf
[ INFO  ] Checking "Cinder" Component
          Profile: /etc/cinder/cinder.conf
[ INFO  ] Checking "Keystone" Component
[ INFO  ] -Service Status
          Service openstack-keystone is running ...
          Service openstack-keystone is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Glance" Component
[ INFO  ] -Service Status
          Service openstack-glance-api is running ...
          Service openstack-glance-api is enabled ...
          Service openstack-glance-registry is running ...
          Service openstack-glance-registry is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Nova" Component
[ INFO  ] -Service Status
          Service openstack-nova-api is running ...
          Service openstack-nova-api is enabled ...
          Service openstack-nova-conductor is running ...
          Service openstack-nova-conductor is enabled ...
          Service openstack-nova-scheduler is running ...
          Service openstack-nova-scheduler is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Neutron" Component
[ INFO  ] -Service Status
          Service neutron-server is running ...
          Service neutron-server is enabled ...
          Service neutron-ovs-cleanup is running ...
          Service neutron-ovs-cleanup is enabled ...
          Service openvswitch is running ...
          Service openvswitch is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.
[ INFO  ] Checking "Cinder" Component
[ INFO  ] -Service Status
          Service openstack-cinder-api is running ...
          Service openstack-cinder-api is enabled ...
          Service openstack-cinder-scheduler is running ...
          Service openstack-cinder-scheduler is enabled ...
          Service openstack-cinder-volume is running ...
          Service openstack-cinder-volume is enabled ...
[ INFO  ] -DB Connectivity
          Check Sucessfully.
[ INFO  ] -Service Availability
          Check Successfully.

[ INFO  ] *************** Role: compute    Node: 172.16.100.12 ***************
[ INFO  ] Checking "Nova" Component
          Profile: /etc/nova/nova.conf
[ INFO  ] Checking "Nova" Component
[ INFO  ] -Service Status
          Service openstack-nova-compute is running ...
          Service openstack-nova-compute is enabled ...

[ INFO  ] *************** Role: compute    Node: 172.16.100.6  ***************
[ INFO  ] Checking "Nova" Component
          Profile: /etc/nova/nova.conf
[ INFO  ] Checking "Nova" Component
[ INFO  ] -Service Status
          Service openstack-nova-compute is running ...
          Service openstack-nova-compute is enabled ...

[ INFO  ] *************** Role: mongo      Node: 172.16.100.11 ***************
[ INFO  ] Checking "Mongo" Component
          Profile: /etc/mongodb.conf
[ INFO  ] Checking "Mongo" Component
[ INFO  ] -Service Status
          Service mongod is running ...
          Service mongod is enabled ...

[ INFO  ] *************** Role: ceph-osd   Node: 172.16.100.10 ***************
[ INFO  ] Checking "Ceph_osd" Component
          Profile: /etc/ceph/ceph.conf
[ INFO  ] Checking "Ceph_osd" Component
[ INFO  ] -Service Status
          Service ceph is running ...
          Service ceph is enabled ...

[ INFO  ] *************** Role: ceph-osd   Node: 172.16.100.9  ***************
[ INFO  ] Checking "Ceph_osd" Component
          Profile: /etc/ceph/ceph.conf
[ INFO  ] Checking "Ceph_osd" Component
[ INFO  ] -Service Status
          Service ceph is running ...
          Service ceph is enabled ...

[ INFO  ] *************** Role: ceph-osd   Node: 172.16.100.8  ***************
[ INFO  ] Checking "Ceph_osd" Component
          Profile: /etc/ceph/ceph.conf
[ INFO  ] Checking "Ceph_osd" Component
[ INFO  ] -Service Status
          Service ceph is running ...
          Service ceph is enabled ...

[ INFO  ] *************** Role: ceph-osd   Node: 172.16.100.13 ***************
[ INFO  ] Checking "Ceph_osd" Component
          Profile: /etc/ceph/ceph.conf
[ INFO  ] Checking "Ceph_osd" Component
[ INFO  ] -Service Status
          Service ceph is running ...
          Service ceph is enabled ...

```









