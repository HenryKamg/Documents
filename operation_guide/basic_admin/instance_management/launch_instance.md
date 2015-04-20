# 启动新的云主机

### 命令

```
# nova boot [--flavor <flavor>] [--image <image>] [--key-name <key-name>] [--security-groups <security-groups>] [--nic <net-id=net-uuid>] <name>
```

### 示例

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
