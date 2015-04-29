### 服务管理
目前在 EayunStack 的环境中，monitor的服务如下：

| 组件 | 服务名 | 运行的节点 |
| -- | -- | -- |
| mon | mon.node-1 | node-1 |
| mon | mon.node-2 | node-2 |
| mon | mon.node-3 | node-3 |

osd 由于对应的是硬盘，用 ceph osd tree 来查找服务和服务名

#### 管理一个 Monitor

登录到 Montior 所在的节点，从上表找到服务名（比如mon.node-1）
```
# [root@node-1 ~]# service ceph status mon.node-1 ### 查看monitor状态
# [root@node-1 ~]# service ceph start mon.node-1 ### 启动monitor
# [root@node-1 ~]# service ceph stop mon.node-1 ### 停止monitor
# [root@node-1 ~]# service ceph restart mon.node-1 ### 重启monitor
```

#### 管理一个 OSD
用 ceph osd tree 查找到需要管理的osd的主机名，登录到该主机。
```
# [root@node-1 ~]# service ceph status mon.node-1 ### 查看monitor状态
# [root@node-1 ~]# service ceph start mon.node-1 ### 启动monitor
# [root@node-1 ~]# service ceph stop mon.node-1 ### 停止monitor
# [root@node-1 ~]# service ceph restart mon.node-1 ### 重启monitor
```
#### 管理集群中所有 Monitor
#### 管理集群中所有 OSD
#### 管理整个集群

### 检查集群状态

### 检查 Monitor 状态

### 检查 OSD 状态

