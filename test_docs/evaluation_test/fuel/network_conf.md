# OpenStack 网络配置

* 前提：

  登录到 Fuel 的管理界面，已经创建了一个 OpenStack 环境，对该环境进行配置。

* 操作：

  1. 点击进入 OpenStack 环境的详细页面，点击上方的【网络】标签；
  1. 对以下内容依次进行配置：

    1. 在【公开】栏，配置 public 网络：

      * 填写 【IP 范围】的【开始】和【结束】 IP 地址；
      * 填写地址段对应的 【CIDR】；
      * 填写公网的【网关】。

    1. 在【管理】栏，配置 management 网络：

      * 填写地址段 【CIDR】；
      * 勾选【使用 VLAN 标记】，填写数值为 "4"。

    1. 在【存储】栏，配置 storage 网络：

      * 填写地址段 【CIDR】；
      * 不勾选【使用 VLAN 标记】。

    1. 在 【Neutron L2 配置】栏：

      * 填写 【VLAN IP range】 的【开始】和【结束】 IP 地址；
      * 在【基础 MAC 地址】填写 MAC 地址的起始地址。

    1. 在 【Neutron L3 配置】栏：

      * 在 【Internal network CIDR】 填写内网 IP 地址范围；
      * 在 【Internal network gateway】 填写内网网关；
      * 在 【Floating IP ranges】 填写【开始】和【结束】的 IP 地址，为分配浮动 IP 地址的范围；
      * 在 【DNS Servers】 填写 DNS 服务器地址。

  1. 点击页面下方的【保存网络】按钮，保存网络配置。

* 预期结果

  配置成功保存，将以该配置部署 OpenStack 环境的网络。
