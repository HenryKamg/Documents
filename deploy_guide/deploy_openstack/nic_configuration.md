# 配置节点网卡

发现并增加所有节点后，需要配置各节点的网卡角色。

## Controller节点

* 勾选全部**Controller节点**，点击**网络配置**按钮。

  ![openstack_install_451](../images/openstack_install_451.png)

 > ###### 注意
 > Controller节点需要连接“Admin(PXE)”、“Private”、”管理“、”存储“、”公开“网络。

* 配置网卡角色，如下图所示。

  ![openstack_install_452](../images/openstack_install_452.png)

## Compute节点

* 勾选全部**Compute节点**，点击**网络配置**按钮。

  ![openstack_install_453](../images/openstack_install_453.png)
 > ###### 注意
 > Compute节点需要连接“Admin(PXE)”、“Private”、”管理“、”存储“、”公开“网络。

* 配置网卡角色，如下图所示。

  ![openstack_install_454](../images/openstack_install_454.png)

## Mongo节点

* 勾选全部**Mongo节点**，点击**网络配置**按钮。

  ![openstack_install_455](../images/openstack_install_455.png)
 > ###### 注意
 > Mongo节点需要连接“Admin(PXE)”、“Private”、”管理“、”存储“、”公开“网络。

* 配置网卡角色，如下图所示。

  ![openstack_install_456](../images/openstack_install_456.png)

## Ceph-osd节点

* 勾选全部**Ceph-osd节点**，点击**网络配置**按钮。

  ![openstack_install_457](../images/openstack_install_457.png)
 > ###### 注意
 > Ceph-osd节点需要连接“Admin(PXE)”、“Private”、”管理“、”存储“、”公开“网络。

* 配置网卡角色，如下图所示。

  ![openstack_install_458](../images/openstack_install_458.png)
