# 创建规格

### 通过Web horizon界创建规格

 登录Web horizon界面，点击云主机类型----创建云主类型，弹出云主机类型创建界面，配置类型参数，点击创建云主机类型

* 创建规格（创建云主机类）

![Flavors_Create](/operation_guide/basic_admin/Picture/flavors_create.jpg)

* 查看已创建规格

![Flavors_Create](/operation_guide/basic_admin/Picture/flavors_create1.jpg)


### 通过命令创建规格

* 创建规格，执行如下命令

> ```nova flavor-create <FLAVOR-NAME> <FLAVOR-ID> <RAM-IN-MB> <ROOT-DISK-IN-GB> <VCPU>```


###示例
```
 nova flavor-create m1.custom 6 512 5 1
+----+-----------+-----------+------+-----------+------+-------+-------------+-----------+
| ID | Name      | Memory_MB | Disk | Ephemeral | Swap | VCPUs | RXTX_Factor | Is_Public |
+----+-----------+-----------+------+-----------+------+-------+-------------+-----------+
| 6  | m1.custom | 512       | 5    | 0         |      | 1     | 1.0         | True      |
+----+-----------+-----------+------+-----------+------+-------+-------------+-----------+

```
