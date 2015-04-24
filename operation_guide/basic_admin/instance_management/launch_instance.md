# 启动新的云主机


### 通过Web horizon界面启动新的云主机

通过登录horzion界查看云主机信息，登录后选择项目----实例----启动云主机（在启动云主机界面配置云主机信息)
* 点击启动云主机，配置云主详情信息(云主机名称、云主机类型、云主机数量、云主机启动源、镜像名称）

   ![Launch_instace](/basic_admin/Picture/launch_instance1.jpg)
* 从可用网络中选择fix网络net04，点击运行开创建云主机

   ![Launch_instance](/basic_admin/Picture/launch_instance2.jpg)

* 云主机开始创建，等待一段时间后云主机创建完成

   ![Launch_instance](/basic_admin/Picture/launch_instance3.jpg)

            (备注：创建云主机根据实际情况进行配置云主机类型，云主机镜像)

### 通过命令方式启动新的云主机

* 启动新的云主机，执行如下命令

> ```
# nova boot [--flavor <flavor>] [--image <image>] [--key-name <key-name>] [--security-groups <security-groups>] [--nic <net-id=net-uuid>] <name>
```

### 示例如下

```
# nova boot --flavor m1.tiny --image cirros-0.3.3-x86_64 --key-name test_keypair --security-groups default --nic net-id=98e535c3-5245-432e-b947-e9c041f2839c test-vm
+--------------------------------------+------------------------------------------------------------+
| Property                             | Value                                                      |
+--------------------------------------+------------------------------------------------------------+
| OS-DCF:diskConfig                    | MANUAL                                                     |
| OS-EXT-AZ:availability_zone          | nova                                                       |
| OS-EXT-SRV-ATTR:host                 | -                                                          |
| OS-EXT-SRV-ATTR:hypervisor_hostname  | -                                                          |
| OS-EXT-SRV-ATTR:instance_name        | instance-0000002c                                          |
| OS-EXT-STS:power_state               | 0                                                          |
| OS-EXT-STS:task_state                | scheduling                                                 |
| OS-EXT-STS:vm_state                  | building                                                   |
| OS-SRV-USG:launched_at               | -                                                          |
| OS-SRV-USG:terminated_at             | -                                                          |
| accessIPv4                           |                                                            |
| accessIPv6                           |                                                            |
| adminPass                            | wrME66mKq2vz                                               |
| config_drive                         |                                                            |
| created                              | 2015-04-16T05:43:45Z                                       |
| flavor                               | m1.tiny (1)                                                |
| hostId                               |                                                            |
| id                                   | 1015b3ff-7395-475b-89cf-a9d76444f39b                       |
| image                                | cirros-0.3.3-x86_64 (82bff63e-62fa-4f6d-acca-97fdd58e4759) |
| key_name                             | test_keypair                                               |
| metadata                             | {}                                                         |
| name                                 | test-vm                                                    |
| os-extended-volumes:volumes_attached | []                                                         |
| progress                             | 0                                                          |
| security_groups                      | default                                                    |
| status                               | BUILD                                                      |
| tenant_id                            | f7376cdfe1804f1ab4c30c6c304bf25b                           |
| updated                              | 2015-04-16T05:43:45Z                                       |
| user_id                              | a385d73636c84a29bbfc72a0b15d882c                           |
+--------------------------------------+------------------------------------------------------------+
```

