# 云主机快照备与恢复

云主机快照备份是对云主机数据进行快照备份，恢复的时间点取决于备份时间
### 通过Web horizon对云主机进行快照

* 选择云主机，点击创建快照，弹出快照创建界面
* 输入快照名称，点击创建快照，开始创建

![Snapshot](/operation_guide/basic_admin/Picture/snapshot1.jpg)

* 创建过程如下

![Snapshot](/operation_guide/basic_admin/Picture/snapshot4.jpg)

![Snapshot](/operation_guide/basic_admin/Picture/snapshot2.jpg)

* 创建完成后，镜像界面查看创建快照信息

![Snapshot](/operation_guide/basic_admin/Picture/snapshot3.jpg)

### 通过命令方式创建快照

* 云主机快照，执行如下命令

> ```nova image-create``` （创建）

> ```nova image-list```   （查看）

### 示例如下

```
#nova image-create EayunStack2 EayunStack2_System
# nova image-list
+--------------------------------------+----------------------+--------+--------------------------------------+
| ID                                   | Name                 | Status | Server                               |
+--------------------------------------+----------------------+--------+--------------------------------------+
| db0132cb-1641-4834-8c81-371ca3c7fdca | EayunStack-1-shelved | ACTIVE | da2774d1-7019-46c7-9805-938328f32a83 |
| 4c7ac48e-4fc2-4675-9e76-ccf11bf3122d | EayunStack2_System   | SAVING | ad00aebd-6c73-48c8-ab1c-bee73da3477e |
| c677b037-acfe-4f54-849b-b29988c2d36d | EayunStack3          | ACTIVE |                                      |
| 27e7f5b0-442e-46ab-8859-0ef100f665ed | EayunStack_System    | ACTIVE | ad00aebd-6c73-48c8-ab1c-bee73da3477e |
| b3ed9a61-dd1b-4933-9f6e-9fda0801ee32 | TestVM               | ACTIVE |                                      |
| b30f6d3b-04ee-4d62-b66f-f2ee80acfa21 | centos64             | ACTIVE |                                      |
| 82bff63e-62fa-4f6d-acca-97fdd58e4759 | cirros-0.3.3-x86_64  | ACTIVE |                                      |
| 832393e3-1676-4d28-853f-a7948d358555 | coffee_test_01       | ACTIVE |                                      |
| 3d007e17-7540-4153-a9ee-8542501eaae3 | tt                   | ACTIVE | ad00aebd-6c73-48c8-ab1c-bee73da3477e |
+--------------------------------------+----------------------+--------+--------------------------------------+

```
