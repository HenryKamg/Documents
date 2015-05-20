# 暂停/恢复云主机

## 保存到内存

* 前提：

  * 云主机的状态为 "Active"；
  * 能够访问云主机。

* 操作：

  1. 访问云主机，在 /tmp 目录下创建一个文件：`touch test.txt`；
  1. 登录到 OpenStack 管理界面；
  1. 点击 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Instances】 选项；
  1. 选择所访问的云主机，点击 【Actions】 中的 【Pause Instance】，暂停云主机；
  1. 将云主机暂停后，点击 【Actions】 中的 【Resume Instance】，恢复云主机。
* 预期结果：

  * 点击 【Pause Instance】 后，云主机成功暂停，不能访问；
  * 云主机的状态变为 "Paused"；
  * 点击 【Resume Instance】 后，云主机成功恢复，能够访问；
  * 云主机的状态恢复为 "Active"；
  * 访问云主机，执行命令 `ls /tmp`，看到所列出的列表中没有 test.txt，文件没有保存。


## 保存到磁盘

* 前提：

  * 云主机的状态为 "Active"；
  * 能够访问云主机。

* 操作：

  1. 访问云主机，在 /tmp 目录下创建一个文件：`touch test.txt`；
  1. 登录到 OpenStack 管理界面；
  1. 点击 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Instances】 选项；
  1. 选择所访问的云主机，点击 【Actions】 中的 【Suspend Instance】，停止云主机；
  1. 将云主机停止后，点击 【Actions】 中的 【Resume Instance】，恢复云主机。

* 预期结果：

  * 点击 【Suspend Instance】 后，云主机成功停止，不能访问；
  * 云主机的状态变为 "Suspended"；
  * 点击 【Resume Instance】 后，云主机成功恢复，能够访问；
  * 云主机状态变为 "Active"；
  * 访问云主机，执行命令 `ls /tmp`，看到所列出的列表中包含 test.txt，文件被保存。
