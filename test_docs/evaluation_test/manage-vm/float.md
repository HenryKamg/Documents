# 为云主机分配浮动 IP

## 分配浮动 IP

* 前提：

  * 云主机的状态为 "Active"；
  * 租户已经创建了路由，且路由连接了外网；
  * 外网使用了 DHCP，DHCP 池中还有可用 IP。

* 操作：

  1. 登录 OpenStack 管理界面；
  1. 点击 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Instances】 选项；
  1. 选择要分配浮动 IP 的云主机，点击 【Actions】 中的 【Associate Floating IP】；
  1. 在弹出的 【Manage Floating IP Associations】 对话框中，为云主机选择一个 IP 地址；
  1. 如果 IP Address 列表中为空，则点击 【+】 按钮，在弹出的 【Allocate Floating IP】 对话框中，选择从哪一个池中分配 IP，点击对话框右下角的 【Allocate IP】 按钮；
  1. 返回 【Manage Floating IP Associations】 对话框，在 "Port to be associated" 下拉列表中找到要分配的云主机名以及对应的端口，选择后点击对话框右下角的 【Associate】 按钮。

* 预期结果：

  * 为云主机分配浮动 IP 成功；
  * 界面有成功提示；
  * 在云主机列表的 "IP Address" 一栏中，看到增加了外网的 IP 地址；
  * 可以从外网通过浮动 IP 访问云主机。

## 释放浮动 IP

* 前提：

  * 用户从外网的 DHCP 地址池中分配了 IP；
  * IP 地址已被云主机使用。

* 操作：

  1. 登录 OpenStack 管理界面；
  1. 点击 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Access & Security】 选项；
  1. 在右侧点击 【Floating IPs】 标签，在 【Floating IPs】 列表中，选择要释放的 IP 地址，点击 【Actions】 中的 【Disassociate】；
  1. 在弹出的 【Confirm Disassociate】 对话框中点击右下角的 【Disassociate】 按钮。

* 预期结果：

  * IP 地址成功被释放，界面上有成功提示；
  * 云主机列表中的 "IP Address" 没有浮动 IP 的显示；
  * 云主机不再拥有外网浮动 IP 地址，无法从外网访问云主机；
  * 被释放的 IP 地址可以重新被分配给其他云主机使用。
