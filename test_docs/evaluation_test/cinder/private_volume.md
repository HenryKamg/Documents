# 私有卷

## 创建私有卷

* 前提：

  * 创建 2 个租户：tenantA, tenantB；
  * 创建 2 个用户：userA, userB，分别属于 tenantA 和 tenantB；
  * 对 Ceph 的设置：

    1. 创建 rbd pool：

      ```
      (controller)# ceph osd pool create rbd1 128
      pool 'rbd1' created
      (controller)# ceph osd pool create rbd2 128
      pool 'rbd2' created
      ```
    1. 查看所创建的 pool：

      ```
      (controller)# rados lspools
      data
      metadata
      rbd
      images
      volumes
      volumes-backup
      compute
      ssd-cachepool-volumes
      rbd1
      rbd2
      ```
    1. 修改配置文件，增加 Cinder 的后端：

      ```
      ```
    1. 重启 Cinder 服务：

      ```
      ```
    1. 确认使用 V2 版本的 cinderclient，设置命令行的版本号：

      ```
      ```

* 操作：

  1. 创建私有卷类型：

    ```
    ```
