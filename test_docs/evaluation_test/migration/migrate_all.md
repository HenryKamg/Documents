# 迁移所有云主机

* 前提：

  * 环境里至少有 2 台 Compute 节点；
  * Compute 节点上的资源足够；
  * 以 admin 身份登录到 OpenStack 管理界面。

* 操作：

  1. 登录到 Controller 节点；
  1. 以 admin 身份执行命令：`nova host-servers-migrate HOST_ID`，其中 HOST_ID 为目的主机的 ID。

* 预期结果：

  * 所选主机上的所有云主机全部迁移到其他主机上；
  * 需要对每台云主机进行 Confirm Resize/Migrate 操作来确认迁移；
  * 或可以点击 Revert Resize/Migrate 取消迁移。
