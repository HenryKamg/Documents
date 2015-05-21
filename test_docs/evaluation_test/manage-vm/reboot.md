# 重启云主机

## 硬重启云主机

* 前提：

  * 云主机的状态为 "Active"；
  * 能够访问云主机；
  * 登录到 OpenStack 管理界面中。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项卡，点击 【Compute】 子选项卡，选择 【Instances】；
  1. 选择一台状态为 "Active" 的云主机，点击 【Actions】 中的 【Hard Reboot Instance】；
  1. 弹出 【Confirm Hard Reboot Instance】 确认窗口，点击窗口下方的 【Hard Reboot Instance】 按钮，确认硬重启。

* 预期结果：

  * 云主机被硬重启；
  * 云主机的状态变化为：Hard Reboot -> Active。

## 软重启云主机

* 前提：

  * 云主机的状态为 "Active"；
  * 能够访问云主机；
  * 登录到 OpenStack 管理界面中。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项卡，点击 【Compute】 子选项卡，选择 【Instances】；
  1. 选择一台状态为 "Active" 的云主机，点击 【Actions】 中的 【Soft Reboot Instance】；
  1. 弹出 【Confirm Soft Reboot Instance】 确认窗口，点击窗口下方的 【Soft Reboot Instance】 按钮，确认硬重启。

* 预期结果：

  * 云主机被软重启；
  * 云主机的状态变化为：Reboot -> Active。
