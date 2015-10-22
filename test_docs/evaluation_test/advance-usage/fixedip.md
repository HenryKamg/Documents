# 多外子网时使用固定 IP 地址

* 场景描述：

  * 能够使用的公网地址有 N 个，且这些公网地址是不连续的。要在 OpenStack 环境中使用其中的特定网络，不希望由 DHCP 来分配。

* 前提：

  * 这些不连续的公网地址已经添加到外网的子网中：

    1. 登录到 OpenStack 管理界面；
    1. 点击左侧导航栏的 【Project】 选项，点击 【Network】 子选项，点击其中的 【Networks】；
    1. 在右侧列表中，选择已创建的**外网**，点击其名称进入详细信息页面，为它创建子网；
    1. 点击详细信息页面列出的子网列表右上角的 【Create Subnet】 按扭；
    1. 在 【Subnet】 标签下，填写 "Subnet Name" 和 "Network Address"，即网络的 CDIR，点击 【Next】 按扭；
    1. 在 【Subnet Detail】 标签下，**取消够选** "Enable DHCP"，取消 DHCP 分配地址；
    1. 点击 【Create】 按扭，创建子网。
  * 已经创建了内网，内网中包含子网；
  * 已经创建了路由，但路由没有设置网关。

* 操作：

  1. 登录到 OpenStack 管理界面；
  1. 点击左侧导航栏的 【Project】 选项，点击 【Network】 子选项，点击其中的 【Routers】；
  1. 在右侧列表中，选择路由，点击其名称进入详细信息页面，为其添加内网接口；
  1. 点击详细信息页面列出的接口列表右上角的 【Add Interface】 按扭；
  1. 在弹出的 【Add Interface】 窗口中，选择 "Subnet" 为内网的子网，在 "IP Address" 中填写子网中的某个 IP 地址（任意），点击窗口下方的 【Add Interface】 按扭，添加内网端口；
  1. 从终端登录到 Controller 节点；
  1. 为路由设置外网接口，执行：

    ```
    # neutron router-gateway-set --external-fixed-ip <EXT_IP_ADDR> <ROUTER_ID> <EXT_NET_ID>
    ```

* 预期结果：

  * 添加内网的接口成功，Interface 列表中显示所添加的接口的信息，"Fixed IPs" 中所显示的是创建内网端口时所指定的内网 IP 地址，该接口的状态为 "ACTIVE"，Admin State 为 "UP"，类型为 "Internal Interface"；
  * 添加外网的接口成功：

    ```
    # neutron router-gateway-set --external-fixed-ip 25.0.1.249 ef78b9ab-cb33-422b-b48d-9d3520d25912 5639fb94-7502-4a4a-8114-94ca65705dd8
    Set gateway for router ef78b9ab-cb33-422b-b48d-9d3520d25912
    ```
  * 登录到 OpenStack 界面后，查看接口列表，看到该路由增加了一个接口，"Fixed IPs" 显示为添加时所用的 IP 地址（在本实验中为 25.0.1.249），接口状态为 "ACTIVE"，Admin State 为 "UP"，类型为 "External Interface"；
  * 用所指定的内网子网创建云主机，该云主机可以通过 25.0.1.249 地址连接到外网。

> ###### 说明：
> * 虽然本实验在创建外网的子网时禁用了 DHCP 服务，但不禁用 DHCP 服务不会对本实验产生影响。
