# 从快照创建云主机

## 创建 Linux 云主机

* 前提：

  * 环境中已经有一个云主机的快照；
  * 环境中已经创建提供给给云主机用的内网租户网络；
  * 用户登录到 OpenStack 管理界面。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Instances】 选项；
  1. 在右侧将列出该租户的云主机列表，点击列表右上角的 【Launch Instance】 按钮；
  1. 在弹出的【Launch Instance】 窗口中，在 Details 标签下，选择 Availability Zone 为 "nova"；
  1. 填写 Instance Name 为 "centos_vm"，选择 Flavor 为 "m1.small"，输入 Instance Count 为 "1"；
  1. 在 Instance Boot Source 处选择 "Boot from snapshot"，从镜像启动云主机，在下方出现的 Instance Snapshot 中选择 "centos-7.0_snapshot" 快照；
  1. 在 Details 标签下，点击网络 "net04" 后的 【+】 图标，为云主机选择该网络；
  1. 其他配置保持默认，点击窗口下方的 【Launch Instance】 按钮。

* 预期结果：

  * 云主机成功创建；
  * 云主机状态变为 "Active" 后，可以打开控制台查看云主机；
  * 为云主机分配了 IP 地址，可以通过 SSH 的方式连接到云主机中。

## 创建 Windows 云主机

* 前提：

  * 环境中已经有一个云主机的快照；
  * 环境中已经创建提供给给云主机用的内网租户网络；
  * 用户登录到 OpenStack 管理界面。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Instances】 选项；
  1. 在右侧将列出该租户的云主机列表，点击列表右上角的 【Launch Instance】 按钮；
  1. 在弹出的【Launch Instance】 窗口中，在 Details 标签下，选择 Availability Zone 为 "nova"；
  1. 填写 Instance Name 为 "windows_vm"，选择 Flavor 为 "m1.small"，输入 Instance Count 为 "1"；
  1. 在 Instance Boot Source 处选择 "Boot from snapshot"，从镜像启动云主机，在下方出现的 Instance Snapshot 中选择 "..." 快照；
  1. 在 Details 标签下，点击网络 "net04" 后的 【+】 图标，为云主机选择该网络；
  1. 其他配置保持默认，点击窗口下方的 【Launch Instance】 按钮。

* 预期结果：

  * 云主机成功创建；
  * 云主机状态变为 "Active" 后，可以打开控制台查看云主机；
  * 为云主机分配了 IP 地址，可以通过 SSH 的方式连接到云主机中。
