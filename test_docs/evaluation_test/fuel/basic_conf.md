# OpenStack 基本配置

* 前提：

  登录到 Fuel 的管理界面，已经创建了一个 OpenStack 环境，对该环境进行配置。

* 操作：

  1. 点击进入 OpenStack 环境的详细页面，点击上方的【设置】标签；
  1. 对以下内容依次进行配置：

    1. 在 【Access】 栏，进行访问设置：

      * 填写 username 为 "admin"，密码为 "admin"；
      * 设置管理租户为 "admin"，填写管理员租户的邮箱。

    1. 在 【Additional Components】 栏，选择额外组件：勾选 【Install Ceilometer】；
    1. 在 【Common】 栏，进行通用配置：

      * 勾选 【OpenStack debug logging】 和 【Nova Quotas】；
      * 在 【Hypervisor type】 处，选择类型为 "KVM"；
      * 在 【Scheduler driver】 处，使用默认配置；
      * 【Public key】 置空；
      * 勾选 "Disable generic offload on physical nics"；

    1. 在 【Kernel parameters】 栏，设置内核参数：添加 "console=ttyS0,9600 console=tty0"；
    1. 在 【Mellanox neutron components】 栏，使用默认设置；
    1. 在 【Syslog】 栏，设置远程主机名和端口，选择传输协议为 TCP；
    1. 在 【VLAN Splinters】 栏，使用默认配置；
    1. 在 【Public network assignment】 栏，不作设置；
    1. 在 【Storage】 栏，配置存储：

      * 勾选以下内容：

        * Ceph RBD for volumes(Cinder)
        * Ceph RBD for images(Glance)
        * Ceph RBD for ephemeral volumes(Nova)

      * 将 【Ceph object replication】 设置为 3。

    1. 【Zabbix】 不进行配置；
    1. 在 【Provision】 栏，使用默认设置；
    1. 在 【Upstream DNS】 栏，填写 DNS 服务器地址为："114.114.114.114" 和 "8.8.8.8"，用"," 隔开；
    1. 在 【Upstream NTP】 栏，填写 NTP 服务器地址："0.pool.ntp.org" 和 "1.pool.ntp.org"，用 "," 隔开。

  1. 已上内容设置完成后，点击页面下方的【保存设置】按钮。

* 预期结果：

  配置成功保存，将以该配置部署 OpenStack 环境。

