# 查看云主机详情信息

### 通过Web horizon界面查看云主机详情信息

云主详情包括概况、日志、控制台、操作日志

概括包括（云主机概况、规格、IP地址、安全组、元数据、镜像名称、云硬盘）
* 云主机概况信息（通过点击云主机名称）

![Instance_Detail](/basic_admin/Picture/instance_detail1.jpg)

![Instance_Detail](/basic_admin/Picture/instance_detail2.jpg)

![Instance_Detail](/basic_admin/Picture/instance_detail3.jpg)

* 云主机日志信息，显示云主机启动日志信息

![Instance_Detail](/basic_admin/Picture/instance_detail4.jpg)

* 云主机控制台，通过点击控制台，打开vnc控制台界面，进行虚拟机操作

![Instance_Detail](/basic_admin/Picture/instance_detail5.jpg)

> 全屏控制台

![Instance_Detail](/basic_admin/Picture/instance_detail6.jpg)

* 云主机操作日志

![Instance_Detail](/basic_admin/Picture/instance_detail7.jpg)



### 通过命令方式查看云主机详情信息

* 查看云主机详情信息，执行如下命令

> ``` nova show INSTANCE```

(INSTANCE 为nova list 中ID 或者 Name）

### 示例如下

```
# nova list
+--------------------------------------+--------------+--------+------------+-------------+-----------------------------------------+
| ID                                   | Name         | Status | Task State | Power State | Networks                                |
+--------------------------------------+--------------+--------+------------+-------------+-----------------------------------------+
| 812b34ed-ad74-4efb-96b8-17a660dc8462 | EayunStack-3 | ACTIVE | -          | Running     | EayunNetWork-Net=11.11.11.8, 25.0.0.174 |
| 3d341752-47f6-4baa-9e08-628155318c52 | EayunStack-4 | ACTIVE | -          | Running     | EayunNetWork-Net=11.11.11.12            |
| ad00aebd-6c73-48c8-ab1c-bee73da3477e | EayunStack2  | ACTIVE | -          | Running     | EayunNetWork-Net=11.11.11.11            |
+--------------------------------------+--------------+--------+------------+-------------+-----------------------------------------+
```
```
#nova show 812b34ed-ad74-4efb-96b8-17a660dc8462
+--------------------------------------+----------------------------------------------------------+
| Property                             | Value                                                    |
+--------------------------------------+----------------------------------------------------------+
| EayunNetWork-Net network             | 11.11.11.8, 25.0.0.174                                   |
| OS-DCF:diskConfig                    | AUTO                                                     |
| OS-EXT-AZ:availability_zone          | nova                                                     |
| OS-EXT-STS:power_state               | 1                                                        |
| OS-EXT-STS:task_state                | -                                                        |
| OS-EXT-STS:vm_state                  | active                                                   |
| OS-SRV-USG:launched_at               | 2015-04-22T10:00:15.000000                               |
| OS-SRV-USG:terminated_at             | -                                                        |
| accessIPv4                           |                                                          |
| accessIPv6                           |                                                          |
| config_drive                         |                                                          |
| created                              | 2015-04-22T09:59:59Z                                     |
| flavor                               | m1.tiny (1)                                              |
| hostId                               | dae778430093b440aa4f3454bd4334bd817c9719ce9b7bf0e372c42b |
| id                                   | 812b34ed-ad74-4efb-96b8-17a660dc8462                     |
| image                                | Attempt to boot from volume - no image supplied          |
| key_name                             | -                                                        |
| metadata                             | {}                                                       |
| name                                 | EayunStack-3                                             |
| os-extended-volumes:volumes_attached | [{"id": "738cbae5-801a-49a5-96a0-cabd47936758"}]         |
| progress                             | 0                                                        |
| security_groups                      | default                                                  |
| status                               | ACTIVE                                                   |
| tenant_id                            | a41d5cfdc44a4a99886e9d36cc87618b                         |
| updated                              | 2015-04-23T07:42:31Z                                     |
| user_id                              | 1f500364cecb48b49d299ed1051ded85                         |
+--------------------------------------+----------------------------------------------------------+
```



