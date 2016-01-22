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
      enabled_backends=cinder_ceph,rbd1,rbd2

      ... ...
      [rbd1]
      volume_backend_name=rbd1
      volume_driver=cinder.volume.drivers.rbd.RBDDriver
      rbd_pool=rbd1
      rbd_max_clone_depth=5
      rbd_user=admin
      rbd_flatten_volume_from_snapshot=False
      rbd_ceph_conf=/etc/ceph/ceph.conf
      rbd_secret_uuid=7d65f135-d7ba-4d87-a083-910ff8cf4eb2

      [rbd2]
      volume_backend_name=rbd2
      volume_driver=cinder.volume.drivers.rbd.RBDDriver
      rbd_pool=rbd2
      rbd_max_clone_depth=5
      rbd_user=admin
      rbd_flatten_volume_from_snapshot=False
      rbd_ceph_conf=/etc/ceph/ceph.conf
      rbd_secret_uuid=7d65f135-d7ba-4d87-a083-910ff8cf4eb2
      ```
    1. 重启 Cinder 服务：

      ```
      (controller)# systemctl restart openstack-cinder-scheduler
      (controller)# systemctl restart openstack-cinder-volume
      (controller)# systemctl restart openstack-cinder-api
      ```
    1. 确认使用 V2 版本的 cinderclient，设置命令行的版本号：

      ```
      (controller)# export OS_VOLUME_API_VERSION=2
      ```
    1. 创建两个租户，用于测试：

      ```
      (controller)# keystone tenant-create --name tenant1
      +-------------+----------------------------------+
      |   Property  |              Value               |
      +-------------+----------------------------------+
      | description |                                  |
      |   enabled   |               True               |
      |      id     | 6d1e3157d64644429a35f60e1f828b7c |
      |     name    |             tenant1              |
      +-------------+----------------------------------+
      (controller)# keystone tenant-create --name tenant2
      +-------------+----------------------------------+
      |   Property  |              Value               |
      +-------------+----------------------------------+
      | description |                                  |
      |   enabled   |               True               |
      |      id     | 4e747bfdb1aa4831a24c9c3a2c1d72c5 |
      |     name    |             tenant2              |
      +-------------+----------------------------------+
      ```
    1. 分别在这两个租户中创建用户，用与测试：

      ```
      (controller)# keystone user-create --name demo1 --tenant tenant1 --pass demo1
      +----------+----------------------------------+
      | Property |              Value               |
      +----------+----------------------------------+
      |  email   |                                  |
      | enabled  |               True               |
      |    id    | b66d8110dd454d62993c6675a1e0820b |
      |   name   |              demo1               |
      | tenantId | 6d1e3157d64644429a35f60e1f828b7c |
      | username |              demo1               |
      +----------+----------------------------------+
      (controller)# keystone user-create --name demo2 --tenant tenant2 --pass demo2
      +----------+----------------------------------+
      | Property |              Value               |
      +----------+----------------------------------+
      |  email   |                                  |
      | enabled  |               True               |
      |    id    | bbf1d2a3e50340e4831debeda506db43 |
      |   name   |              demo2               |
      | tenantId | 4e747bfdb1aa4831a24c9c3a2c1d72c5 |
      | username |              demo2               |
      +----------+----------------------------------+
      ```

* 操作：

  1. 创建两种私有卷类型：

    ```
    (controller)# cinder --debug type-create volume_type_001 --is-public false
    (controller)# cinder --debug type-create volume_type_002 --is-public false
    ```
  1. 将 volume_type_001 和 volume_type_002 的后端存储分别配置为 rbd1 和 rbd2：

    ```
    (controller)# cinder type-key [volume_type_001_ID] set volume_backend_name=rbd1
    (controller)# cinder type-key [volume_type_002_ID] set volume_backend_name=rbd2
    ```
  1. 分别将卷类型 volume_type_001 和 volume_type_002 指定给租户 tenant1 和 tenant2：

    ```
    (controller)# cinder type-access-add --volume-type [volume_type_001_ID] --project 6d1e3157d64644429a35f60e1f828b7c
    (controller)# cinder type-access-add --volume-type [volume_type_002_ID] --project 4e747bfdb1aa4831a24c9c3a2c1d72c5
    ```
  1. 使用 demo1 用户登录 OpenStack 管理界面，点击左侧导航栏中的 【Project】 中的 【Compute】，展开后点击其中的 【Volumes】 选项卡；
  1. 右侧显示卷列表，点击列表右上角的 【+ Create Volume】 按钮；
  1. 在弹出的 【Create Volume】 对话框中，填写名称为 "volume1"，选择 Type 为 "volume_type_001"，Size 为 "1"(GB)；
  1. 填写完成后，点击对话框右下角的 【Create Volume】 按钮；
  1. 以同样的方式用 demo2 登录后，创建卷；
  1. 登录 Controller 节点；
  1. 使用 demo1 用户创建 volume_type_002 类型的卷：

    ```
    (controller)# . test_demo1; cinder create 1 --volume-type volume_type_002
    ```
  1. 使用 demo2 用户创建 volume_type_001 类型的卷：

    ```
    (controller)# . test_demo2; cinder create 1 --volume-type volume_type_001
    ```

* 预期结果：

  * 成功分别为 tenant1 和 tenant2 租户创建了私有类型；
  * demo1 和 demo2 可以使用本租户的卷类型创建卷；
  * demo1 创建 volume_type_002 类型的卷失败：

    ```
    (controller)# . test_demo1; cinder create 1 --volume-type volume_type_002
    ERROR: Not Found (HTTP 404) (Request-ID: req-e53feda2-0939-459a-8e69-e56801eb487e)
    ```
  * demo2 创建 volume_type_001 类型的卷失败：

    ```
    (controller)# . test_demo2; cinder create 1 --volume-type volume_type_001
    ERROR: Not Found (HTTP 404) (Request-ID: req-e40e14db-751e-4b9c-b916-66e60b7b32ba)
    ```

## 删除卷类型

* 前提：

  以卷类型所属租户的用户执行。

* 操作：

  1. 登录 Controller 节点；
  1. 执行命令，将卷类型删除：

    ```
    (controller)# cinder type-delete TYPE_ID
    ```

* 预期结果：

  * 卷类型删除成功；
  * 不能使用该卷创建卷。
