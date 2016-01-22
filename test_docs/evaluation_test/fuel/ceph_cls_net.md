# 配置 Ceph Cluster 网络

Ceph 网络需要单独配置，以使 Ceph 集群的网络使用对应的独立网卡。

* 前提：

  Ceph 机器上设置了集群使用的网卡。

* 操作：

  1. 登录到 Fuel 节点中；
  1. 获取所要修改的环境的 ID：

    ```
    (fuel)# fuel environment --name EayunStack
    id | status      | name       | mode       | release_id | changes                                                                  | pending_release_id
    ---|-------------|------------|------------|------------|--------------------------------------------------------------------------|-------------------
    1  | operational | EayunStack | ha_compact | 1          | [{u'node_id': 3, u'name': u'disks'}, {u'node_id': 4, u'name': u'disks'}] | None              
    ```
  1. 获取 Ceph-OSD 节点的 ID：

    ```
    (fuel)# fuel node
    id | status | name             | cluster | ip            | mac               | roles      | pending_roles | online | group_id
    ---|--------|------------------|---------|---------------|-------------------|------------|---------------|--------|---------
    1  | ready  | Untitled (4e:cf) | 1       | 172.16.100.9  | 1e:61:86:e1:c0:43 | compute    |               | True   | 1       
    9  | ready  | Untitled (e3:52) | 1       | 172.16.100.19 | 2a:9f:b0:66:fb:42 | controller |               | True   | 1       
    3  | ready  | Untitled (10:9e) | 1       | 172.16.100.13 | fa:15:62:7e:84:4c | ceph-osd   |               | True   | 1       
    4  | ready  | Untitled (a9:54) | 1       | 172.16.100.15 | 4e:46:7a:a5:a1:42 | ceph-osd   |               | True   | 1       
    2  | ready  | Untitled (05:6a) | 1       | 172.16.100.12 | 8e:38:3a:8f:23:4f | compute    |               | True   | 1       
    8  | ready  | Untitled (c6:52) | 1       | 172.16.100.17 | 96:d7:f7:08:41:45 | controller |               | True   | 1       
    5  | ready  | Untitled (09:e6) | 1       | 172.16.100.14 | 92:8f:60:f7:e6:45 | ceph-osd   |               | True   | 1       
    6  | ready  | Untitled (63:f1) | 1       | 172.16.100.16 | d6:cd:f6:d6:1d:49 | mongo      |               | True   | 1       
    7  | ready  | Untitled (e3:b7) | 1       | 172.16.100.18 | 9e:13:2f:92:ca:42 | controller |               | True   | 1       
    ```
  1. 上述所获得的 Ceph-OSD 的 ID 为 3, 4, 5，则配置 ceph cluster 网络如下：

    ```
    (fuel)# eayunstack fuel ceph_cluster_network --env 1 --cidr 172.16.200.0/24 --nic_mappings 3:eth4,4:eth4,5:eth4
    ```

* 预期结果：

  * Ceph Cluster 网络设置成功；
  * Ceph 集群使用所设置的独立网络作为 cluster 网络。
