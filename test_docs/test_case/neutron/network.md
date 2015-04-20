# 验证 Neutron 的 network 部分

|内容编号|内容名称|
|--------|--------|
|01|网络|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01070101|测试 neutron net-list 命令的性能||||创建并列出网络，需要指定参数|Rally:</br>create_and_list_networks.json|
|01070102|测试 neutron net-create 和 neutron net-delete 命令的性能||||创建网络后，将其删除|Rally:</br>create_and_delete_networks.json|
|01070103|测试 neutron net-create 和 neutron net-update 命令的性能||||创建网络后，修改网络|Rally:</br>create_and_update_networks.json|

