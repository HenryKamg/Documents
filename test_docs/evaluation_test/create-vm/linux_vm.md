# 创建 Linux 虚拟机

## 通过镜像创建虚拟机

* 前提：

  * 环境中已经有一个 Linux 镜像；
  * 环境中已经创建租户网络；
  * 用户登录到 OpenStack 的管理界面。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Instances】 选项；
  1. 在右侧将列出该租户的实例列表，点击列表右上角的 【Launch Instance】 按钮；
  1. 在弹出的【Launch Instance】 窗口中，在 Details 标签下，填写 Instance Name 为 "centos_vm"，选择 Flavor 为 "..."，输入 Instance Count 为 "1"；
  1. 在 Instance Boot Source 处选择 "Boot from image"，从镜像启动实例，在下方出现的 Image 中选择 "..." 镜像；
  1. 在 Details 标签下，点击网络 "..." 后的 【+】 图标，为实例选择该网络；
  1. 其他配置保持默认，点击窗口下方的 【Launch Instance】 按钮。

* 预期结果：

  * 实例成功创建；
  * 可以打开控制台查看实例；
  * 。。。

## 通过快照创建虚拟机

* 前提：

  * 环境中已经有一个实例的快照；
  * 环境中已经创建租户网络？
  * 用户登录到 OpenStack 管理界面。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Instances】 选项；
  1. 在右侧将列出该租户的实例列表，点击列表右上角的 【Launch Instance】 按钮；
  1. 在弹出的【Launch Instance】 窗口中，在 Details 标签下，填写 Instance Name 为 "centos_vm"，选择 Flavor 为 "..."，输入 Instance Count 为 "1"；
  1. 在 Instance Boot Source 处选择 "Boot from image"，从镜像启动实例，在下方出现的 Image 中选择 "..." 镜像；
  1. 在 Details 标签下，点击网络 "..." 后的 【+】 图标，为实例选择该网络；
  1. 其他配置保持默认，点击窗口下方的 【Launch Instance】 按钮。

* 预期结果：

  * 实例成功创建；
  * 可以打开控制台查看实例；
  * 。。。

## 通过卷创建虚拟机

* 前提：

  * 卷？；
  * 环境中已经创建租户网络？
  * 用户登录到 OpenStack 管理界面。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Instances】 选项；
  1. 在右侧将列出该租户的实例列表，点击列表右上角的 【Launch Instance】 按钮；
  1. 在弹出的【Launch Instance】 窗口中，在 Details 标签下，填写 Instance Name 为 "centos_vm"，选择 Flavor 为 "..."，输入 Instance Count 为 "1"；
  1. 在 Instance Boot Source 处选择 "Boot from volume"，从镜像启动实例，在下方出现的 Image 中选择 "..." 镜像；
  1. 在 Details 标签下，点击网络 "..." 后的 【+】 图标，为实例选择该网络；
  1. 其他配置保持默认，点击窗口下方的 【Launch Instance】 按钮。

* 预期结果：

  * 实例成功创建；
  * 可以打开控制台查看实例；
  * 。。。

## 删除虚拟机

* 前提：

* 操作：

* 预期结果：

