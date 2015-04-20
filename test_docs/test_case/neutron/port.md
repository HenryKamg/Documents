# 验证 Neutron 的 port 部分

|内容编号|内容名称|
|--------|--------|
|02|端口|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01070201|测试 neutron port-create 和 neutron port-list 命令的性能||||创建并列出端口|Rally:</br>create_and_list_ports.json|
|01070202|测试 neutron port-create 和 neutron port-delete 命令的性能||||创建端口后，将其删除|Rally:</br>create_and_delete_ports.json|
|01070203|测试 neutron port-create 和 neutron port-update 命令的性能||||创建端口后，修改端口|Rally:</br>create_and_update_ports.json|

