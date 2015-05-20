# 在线迁移云主机

## 在线迁移但不迁移磁盘

* 前提：

  * 环境中至少有 2 个 Compute 节点；
  * Compute 节点上的资源足够；
  * 以 admin 身份登录到 OpenStack 管理界面。

* 操作：

  1. 点击左侧导航栏的 【Admin】 选项卡，点击 【System】 子选项卡，点击其中的 【Instances】 选项；
  1. 在右侧将列出所有云主机的列表，选择一台云主机，点击 【Actions】 中的 【Live Migrate Instance】；
  1. 弹出 【Live Migrate】 窗口，在 New Host 选择目的主机，不勾选 "Disk Over Commit" 和 "Block Migrate"；
  1. 点击窗口下方的 【Live Migrate Instance】 按钮。

* 预期结果：

  * 云主机在线迁移成功；
  * 云主机在业务没有停止的情况下，迁移到目的主机上；
  * 由于没有勾选 "Disk Over Commit"，云主机的磁盘没有迁移到目的主机上。


## 在线迁移并迁移磁盘

* 前提：

  * 环境中至少有 2 个 Compute 节点；
  * Compute 节点上的资源足够；
  * 以 admin 身份登录到 OpenStack 管理界面。

* 操作：

  1. 点击左侧导航栏的 【Admin】 选项卡，点击 【System】 子选项卡，点击其中的 【Instances】 选项；
  1. 在右侧将列出所有云主机的列表，选择一台云主机，点击 【Actions】 中的 【Live Migrate Instance】；
  1. 弹出 【Live Migrate】 窗口，在 New Host 选择目的主机，勾选 "Disk Over Commit"，不勾选 "Block Migrate"；
  1. 点击窗口下方的 【Live Migrate Instance】 按钮。

* 预期结果：

  * 云主机在线迁移成功；
  * 云主机在业务没有停止的情况下，迁移到目的主机上；
  * 由于勾选了 "Disk Over Commit"，云主机的磁盘也一并迁移到目的主机上。

