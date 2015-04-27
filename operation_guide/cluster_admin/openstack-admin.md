### 常用管理命令
由上面简介， 除了 neutron 的部分服务，大部分 OpenStack 服务都是由 systemd 管理的，用 haproxy 来做负载均衡，对于这些大部分的服务，相关的管理命令为：
```
# systemctl start [服务名] #启动服务
# systemctl stop [服务名] #关闭服务
# systemctl restart [服务名] #重启服务
```

除此之外，一些和各个服务相关的命令显示在下面：
#### keystone
##### 列出各个服务的 API 地址：
```
[root@node-1 ~]# keystone endpoint-list
+----------------------------------+-----------+---------------------------------------+-------------------------------------------+-------------------------------------------+----------------------------------+
|                id                |   region  |               publicurl               |                internalurl                |                  adminurl                 |            service_id            |
+----------------------------------+-----------+---------------------------------------+-------------------------------------------+-------------------------------------------+----------------------------------+
| 056375a459954f32a442feb1c25cb791 | RegionOne |  http://25.0.0.2:8773/services/Cloud  |  http://172.16.101.2:8773/services/Cloud  |  http://172.16.101.2:8773/services/Admin  | 89bb5e12c7844f78b30106e4ac66dfc8 |
| 08671aaca84c41cb9d0177c4e307c2ee | RegionOne | http://25.0.0.2:8776/v1/%(tenant_id)s | http://172.16.101.2:8776/v1/%(tenant_id)s | http://172.16.101.2:8776/v1/%(tenant_id)s | dfcc03186d014827be57cdfee1e9b39a |
| 0964d483057b490db376b91b4db690c1 | RegionOne |       http://25.0.0.2:5000/v2.0       |       http://172.16.101.2:5000/v2.0       |       http://172.16.101.2:35357/v2.0      | c67a0f60122e48a990413047cbf86e3e |
| 772e46eb4ee74255b5c59838200880f5 | RegionOne |          http://25.0.0.2:8777         |          http://172.16.101.2:8777         |          http://172.16.101.2:8777         | 31d82ea106e14a1eb208bacfa3d429bf |
| 92036ff4f9bc4c268bc329ef1ebb573d | RegionOne |         http://25.0.0.2:9696/         |         http://172.16.101.2:9696/         |         http://172.16.101.2:9696/         | 9149496e7e3d4df7bbc105ff649a681e |
| a1a338113fd24c459c660a67312769af | RegionOne | http://25.0.0.2:8776/v2/%(tenant_id)s | http://172.16.101.2:8776/v2/%(tenant_id)s | http://172.16.101.2:8776/v2/%(tenant_id)s | 3e5a0937bac543f9990305cde8d4ea77 |
| d18c99467746404b8a13971941351a16 | RegionOne | http://25.0.0.2:8774/v2/%(tenant_id)s | http://172.16.101.2:8774/v2/%(tenant_id)s | http://172.16.101.2:8774/v2/%(tenant_id)s | dd6c7d017edd4e5eaec2d73cbd05df98 |
| ec3ce0807cd04d83846d3f00d28b1021 | RegionOne |          http://25.0.0.2:9292         |          http://172.16.101.2:9292         |          http://172.16.101.2:9292         | ebe9e523e5974cefaed6ebc62b4d94e3 |
| f3f898e963db4cca85c16a0b02448604 | RegionOne | http://25.0.0.2:8004/v1/%(tenant_id)s | http://172.16.101.2:8004/v1/%(tenant_id)s | http://172.16.101.2:8004/v1/%(tenant_id)s | 8f7a2951a90f4c778d4adbae0e759a81 |
| f68316be515b45a2b478cbbbf4d6b7d4 | RegionOne |        http://25.0.0.2:8000/v1/       |        http://172.16.101.2:8000/v1/       |        http://172.16.101.2:8000/v1/       | 6f2735fa26f34cdfa9292fe6d1bb050b |
+----------------------------------+-----------+---------------------------------------+-------------------------------------------+-------------------------------------------+----------------------------------+

```

##### 刷新过期 token

目前 keystone 的 token 是存储在mysql数据库中，OpenStack 不会负责清理这些 token，如果长期使用，会发现用户登录 Horzion 登录变慢，mysql CPU 占用较高，Mysql 数据库变大。这时候要考虑清理 keystone 数据库中 token 表，所幸 keystone 提供了一个指令来清理这些过期 token。
```
# keystone-manage token_flush
```
PS：目前我们的 eayunstack 已经集成了脚本来自动清理过期 token。

#### glance
基本管理同上。

#### nova
基本管理同上。

注意：如果重启了计算节点的 libvirt，那么需要重启相应的计算节点的 nova-comupte 服务

nova service-list

#### neutron

dnsmasq

neutron agent-list

#### cinder

cinder service-list

eqlx, ceph

#### horzion
