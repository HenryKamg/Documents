# 可被多台云主机挂载的卷

## 将可被多台云主机挂载的卷附加给云主机

* 前提；

  * 租户中有 2 台云主机 "instance_01" 和 "instance_02"；
  * 租户中创建了一个可被多台云主机挂载的卷：

    ```
    (controller)# cinder create --display-name coffee-multi-01 --allow-multiattach 1                                                                                               
+---------------------------------------+--------------------------------------+
|                Property               |                Value                 |
+---------------------------------------+--------------------------------------+
|              attachments              |                  []                  |
|           availability_zone           |                 nova                 |
|                bootable               |                false                 |
|          consistencygroup_id          |                 None                 |
|               created_at              |      2016-03-01T10:49:31.000000      |
|              description              |                 None                 |
|               encrypted               |                False                 |
|                   id                  | 7ee0adea-adb2-4836-ab3f-fd67c67b3768 |
|                metadata               |                  {}                  |
|              multiattach              |                 True                 |
|                  name                 |           coffee-multi-01            |
|         os-vol-host-attr:host         |                 None                 |
|     os-vol-mig-status-attr:migstat    |                 None                 |
|     os-vol-mig-status-attr:name_id    |                 None                 |
|      os-vol-tenant-attr:tenant_id     |   7f67af7413074a85b751eaf997d59ae7   |
|   os-volume-replication:driver_data   |                 None                 |
| os-volume-replication:extended_status |                 None                 |
|           replication_status          |               disabled               |
|                  size                 |                  1                   |
|              snapshot_id              |                 None                 |
|              source_volid             |                 None                 |
|                 status                |               creating               |
|                user_id                |   02cf5d669cbc4fd1a50be6f2aca0c332   |
|              volume_type              |                 None                 |
+---------------------------------------+--------------------------------------+
    ```

* 操作：

  1. 登录到 Dashboard，点击左侧导航栏中的 【Project】，选择其中的 【Compute】 中的 【Volumes】 选项；
  1. 在右侧的 Volumes 列表中，选择上述新建的卷，点击 【Actions】 中的 【Edit Attachments】；
  1. 在弹出的 【Manage Volume Attachments】 窗口中，在 "Attach To Instance" 处选择 "instance_01"，将卷挂载到 "instance_01" 上；
  1. 登录 "instance_01"，将卷格式化：

    ```
    $ sudo mkfs.ext3 /dev/vdb
    mke2fs 1.42.8 (20-Jun-2013)
    Filesystem label=
    OS type: Linux
    Block size=4096 (log=2)
    Fragment size=4096 (log=2)
    Stride=0 blocks, Stripe width=0 blocks
    65536 inodes, 262144 blocks
    13107 blocks (5.00%) reserved for the super user
    First data block=0
    Maximum filesystem blocks=268435456
    8 block groups
    32768 blocks per group, 32768 fragments per group
    8192 inodes per group
    Superblock backups stored on blocks: 
    	32768, 98304, 163840, 229376

    Allocating group tables: done                            
    Writing inode tables: done                            
    Creating journal (8192 blocks): done
    Writing superblocks and filesystem accounting information: done
    ```
  1. 创建 `/tmp/test01` 目录，并将 /dev/vdb 挂载到该目录下：

    ```
    $ mkdir /tmp/test01
    $ sudo mount /dev/vdb /tmp/test01
    ```
  1. 在 `/tmp/test01` 目录下创建文件，并写入内容：

    ```
    $ sudo chmod 777 /tmp/test01
    $ sudo echo 'test multiattach on instance_01' > /tmp/test01/test01
    ```
  1. 登录 Controller 节点，执行命令，将该卷挂载到 "instance_02" 上：

    ```
    (controller)# nova volume-attach [INSTANCE_02_ID] [VOLUME_ID]
    ```
  1. 登录 "instance_02"，创建 `/tmp/test02` 目录，并将 /dev/vdb 挂载到该目录下：

    ```
    $ mkdir /tmp/test02
    $ sudo mount /dev/vdb /tmp/test02
    ```
  1. 查看 "instance_02" 的 `/tmp/test02/test01` 文件的内容：

    ```
    $ cat /tmp/test02/test01
    ```
  1. 在 "instance_02" 中写入文件内容：

    ```
    $ sudo echo 'test multiattach on instance_02' >> /tmp/test02/test01
    ```
  1. 在 "instance_01" 上查看 `/tmp/test01/test01` 文件的内容：

    ```
    $ cat /tmp/test01/test01
    ```

* 预期结果：

  * 将卷挂载到 "instance_01" 后，可以成功将卷挂载到 "instance_02" 上：

    ```
    (controller)# nova volume-attach 4b0f574f-74ed-4e6f-b6f3-185c6a5b2d7b 7ee0adea-adb2-4836-ab3f-fd67c67b3768
    +----------+--------------------------------------+
    | Property | Value                                |
    +----------+--------------------------------------+
    | device   | /dev/vdb                             |
    | id       | 7ee0adea-adb2-4836-ab3f-fd67c67b3768 |
    | serverId | 4b0f574f-74ed-4e6f-b6f3-185c6a5b2d7b |
    | volumeId | 7ee0adea-adb2-4836-ab3f-fd67c67b3768 |
    +----------+--------------------------------------+
    ```
  * 该卷是 "instance_01" 和 "instance_02" 这两台云主机共享的，TODO
