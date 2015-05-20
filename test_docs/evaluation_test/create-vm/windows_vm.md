# 创建 Windows 云主机

## 通过镜像创建云主机

* 前提：

  * 环境中已经有一个 Windows 镜像；
  * 环境中已经创建提供给给云主机用的内网租户网络；
  * 用户登录到 OpenStack 的管理界面。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Instances】 选项；
  1. 在右侧将列出该租户的云主机列表，点击列表右上角的 【Launch Instance】 按钮；
  1. 在弹出的【Launch Instance】 窗口中，在 Details 标签下，选择 Availability Zone 为 "nova"；
  1. 填写 Instance Name 为 "windows_vm"，选择 Flavor 为 "m1.small"，输入 Instance Count 为 "1"；
  1. 在 Instance Boot Source 处选择 "Boot from image"，从镜像启动云主机，在下方出现的 Image 中选择 "..." 镜像；
  1. 在 Access & Security 标签下，在 Key Pair 处点击下拉按钮，选择密钥对，勾选 Security Groups "default"；
  1. 在 Networking 标签下，点击网络 "net04" 后的 【+】 图标，为云主机选择该网络；
  1. 其他配置保持默认，点击窗口下方的 【Launch Instance】 按钮。

* 预期结果：

  * 云主机成功创建；
  * 云主机状态变为 "Active" 后，可以打开控制台查看云主机；
  * 为云主机分配了 IP 地址，可以通过 SSH 的方式连接到云主机中。

## 通过快照创建云主机

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

## 通过卷创建云主机

* 前提：

  * 环境中有一个基于镜像创建的卷；
  * 环境中已经创建提供给给云主机用的内网租户网络；
  * 用户登录到 OpenStack 管理界面。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Instances】 选项；
  1. 在右侧将列出该租户的云主机列表，点击列表右上角的 【Launch Instance】 按钮；
  1. 在弹出的【Launch Instance】 窗口中，在 Details 标签下，选择 Availability Zone 为 "nova"；
  1. 填写 Instance Name 为 "windows_vm"，选择 Flavor 为 "m1.small"，输入 Instance Count 为 "1"；
  1. 在 Instance Boot Source 处选择 "Boot from volume"，从镜像启动云主机，在下方出现的 Volume 中选择 "..." 卷；
  1. 在 Details 标签下，点击网络 "net04" 后的 【+】 图标，为云主机选择该网络；
  1. 其他配置保持默认，点击窗口下方的 【Launch Instance】 按钮。

* 预期结果：

  * 云主机成功创建；
  * 云主机状态变为 "Active" 后，可以打开控制台查看云主机；
  * 为云主机分配了 IP 地址，可以通过 SSH 的方式连接到云主机中。

## 删除云主机

* 前提：

  * 用户是 admin 角色，或登录的用户从属于要删除的云主机所在的项目，本实验属于后者；
  * 用户登录到 OpenStack 管理界面。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Instances】 选项；
  1. 在右侧将列出该租户的云主机列表，选择要删除的云主机，点击云主机后的 【Actions】 中的 【Terminate Instance】；
  1. 弹出 【Confirm Terminate Instance】 窗口，点击窗口下方的 【Terminate Instance】 按钮，确认删除。

* 预期结果：

  * 点击窗口下方的 【Terminate Instance】 按钮后，云主机被删除，有 Success 的信息提示；
  * 若点击了窗口下方的 【Cancel】 按钮，则取消删除，云主机不会被删除，保持原样。

