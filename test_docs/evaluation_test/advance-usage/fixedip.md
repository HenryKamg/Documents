# 多外子网时使用固定 IP 地址

* 场景描述：

  * 能够使用的公网地址有 N 个，且这些公网地址是不连续的。要在 OpenStack 环境中使用其中的特定网络，不希望由 DHCP 来分配。

* 前提：

  * 这些不连续的公网地址已经添加到外网的子网中：

    1. 登录到 OpenStack 管理界面（使用管理员用户登录）；
    1. 点击左侧导航栏的 【Project】 选项，点击 【Network】 子选项，点击其中的 【Networks】；
    1. 在右侧列表中，选择已创建的**外网**，点击其名称进入详细信息页面，为它创建子网；
    1. 点击详细信息页面列出的子网列表右上角的 【Create Subnet】 按扭；
    1. 在 【Subnet】 标签下，填写 "Subnet Name" 和 "Network Address"，即网络的 CDIR，点击 【Next】 按扭；
    1. 在 【Subnet Detail】 标签下，**取消勾选** "Enable DHCP"，取消 DHCP 分配地址；
    1. 点击 【Create】 按扭，创建子网。
  * 租户中已经创建了内网，内网中包含子网；
  * 租户已经创建了路由，但路由没有设置网关；
  * 租户已经创建了虚拟机。

* 操作：

  1. 从终端登录到 Controller 节点；
  1. 为路由设置外网接口，执行（使用管理员用户执行）：

    ```
    # neutron router-gateway-set --external-fixed-ip <EXT_IP_ADDR> <ROUTER_ID> <EXT_NET_ID>
    # neutron floatingip-create --floating-ip-address <FLOATING_IP_ADDR> --tenant-id <TENANT_ID> <EXT_NET_ID>
    ```
  1. 登录到 OpenStack 管理界面（使用租户用启登录）；
  1. 点击左侧导航栏的 【Project】 选项，点击 【Compute】 子选项，点击其中的 【Instances】；
  1. 在右侧列表中，找到需要使用新建浮动 IP 地址的虚拟机，在 【Actions】 的下拉菜单中选择 【Associate Floating IP】；
  1. 在出现的 【Manage Floating IP Associations】 对话框中，【IP Address】中选择之前创建的浮动 IP 地址，【Port to be associate】中选择虚拟机的某一网卡。

* 预期结果：

  * 可以通过 `router-gateway-set` 中 `--external-fixed-ip` 参数指定的 IP 地址访问租户路由；
  * 可以通过绑定后的浮动 IP 地址访问虚拟机。

> ###### 说明：
> * 虽然本实验在创建外网的子网时禁用了 DHCP 服务，但不禁用 DHCP 服务不会对本实验产生影响；
> * `neutron router-gateway-set` 使用 `--external-fixed-ip` 参数以及 `neutron floatingip-create` 使用 `--floating-ip-address` 都需要管理员用户。
