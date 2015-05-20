# 直接迁移云主机

* 前提：

  * 环境中至少有 2 个 Compute 节点；
  * Compute 节点上的资源足够；
  * 以 admin 身份登录到 OpenStack 管理界面。

* 操作：

  1. 点击左侧导航栏的 【Admin】 选项卡，点击 【System】 子选项卡，点击其中的 【Instances】 选项；
  1. 在右侧将列出所有云主机的列表，选择一台云主机，点击 【Actions】 中的 【Migrate Instance】；
  1. 弹出 【Confirm Migrate Instance】 窗口，点击窗口下方的 【Migrate Instance】 按钮，确认迁移。

* 预期结果：

  * 云主机成功迁移；
  * 云主机的状态为 "Confirm or Revert Resize/Migrate"，需要确认迁移：
    * 若点击 【Actions】 中的 【Confirm Resize/Migrate】，确认迁移，则云主机迁移到另一台 Compute 节点上；
    * 若点击 【Actions】 中的 【Revert Resize/Migrate】，可以撤销迁移操作，云主机恢复到原来的主机上运行。

> #### 注意：
> 在默认规则下，迁移操作是只有管理员身份才能执行的，因此要以 admin 的角色登录。
