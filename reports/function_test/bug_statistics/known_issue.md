# 遗留缺陷与未解决问题

* **OpenStack 节点数量限制**：

  * 由于 Dell Eqlx 的限制，最多支持 5 台 Controller 节点，50 台 Compute 节点 (后续版本考虑使用统一的 Ceph 存储)。

* **RabbitMQ集群故障恢复**：

  * 所有 Controller 节点同时重启时，RabbitMQ 集群会启动失败；
  * RabbitMQ 集群出现故障时，EayunStack 内部没有实现 RabbitMQ 的心跳检测，需要一段时间自动恢复时间(下个版本解决)。

* **虚拟机镜像格式**：

  * 为了实现虚拟机秒级创建和磁盘卷秒级快照功能，使用的时候虚拟机的磁盘格式请使用 RAW。
