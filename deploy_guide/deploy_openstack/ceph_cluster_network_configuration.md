# 配置Ceph Cluster网络

默认配置中，Ceph集群的public/mon/cluster网络全部使用Fuel管理界面中节点网卡配置中所指定的Storage网络，在生产环境中，我们需要修改网络配置，使Ceph集群的cluster网络对应一个独立的EayunStack网络(Ceph Cluster Network)。

### 配置流程

* 登录Fuel节点

* 下载Ceph节点的配置

 ```
 # mkdir /ceph-conf
 # fuel --env EayunStack deployment --download --dir /ceph-conf --node A,B,C
 ```

* 修改Ceph节点配置文件

  * 在 network_scheme 一段之下的 transformation 一节下添加(以用于 ceph cluster network 的网卡名为 ehtX 且不使用 vlan 为例，其它情况需要根据实际情况更改部分内容)

    ```
    # cd /ceph-conf
    # vim 
    - action: add-br
      name: br-ethX
    - action: add-port
      bridge: br-ethX
      name: ethX
    - action: add-br
      name: br-ceph-cluster
    - action: add-patch
      bridges:
      - br-ethX
      - br-ceph-cluster
      trunks:
      - 0
    ```

  * 在 network_scheme 一段之下的 roles 一节下添加

    ```
    roles:
    ...
    ceph_cluster: br-ceph-cluster
    ...
    ```

  * 在 network_scheme 一段之下的 interfaces 一节下添加

    ```
    ethX:
      L2:
        vlan_splinters: 'off'
    ```

  * 在 network_scheme 一段之下的 endpoints 一节下添加(XXX.XXX.XXX.XXX/XX 替换为实际为此接口准备的 IP 地址)

    ```
    br-ceph-cluster:
      IP:
      - XXX.XXX.XXX.XXX/XX
      other_nets: []
    ```

  * 保存并依次配置其它 ceph-osd 节点

* 上传配置文件
 
 ```
 # fuel --env EayunStack deployment --upload --dir /ceph-conf
 ```
