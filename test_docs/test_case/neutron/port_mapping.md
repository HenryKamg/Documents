# 验证 Neutron 的 Port Mapping 部分

|内容编号|内容名称|
|--------|--------|
|05|端口映射|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01010501|测试端口映射的创建|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>neutron router-show [ROUTER_NAME]</code> 获取要进行端口映射的路由 ID (ROUTER_ID)；</li><li>执行命令 <code>nova show [INSTANCE_NAME]</code> 获取要映射的云主机的内网 IP 地址；</li>li>执行命令 <code>neutron portmapping-create [ROUTER_ID] [ROUTER_PORT] [DESTINATION_IP] [DESTINATION_PORT]</code>，创建端口映射，其中，ROUTER_ID 是该云主机所连接到的要映射的路由的 ID；ROUTER_PORT 指路由中的 TCP/UDP 端口，使用 --protocol 参数，则默认是 TCP 端口；DESTINATION_IP 为云主机的内网 IP 地址；DESTINATION_PORT 为要映射的云主机的某个端口，如 9090。</li></ol></li></ul>|<ul><li>CLI:<ul><li>成功创建端口映射</li></ul></li></ul>|||None|
|01010502|测试端口映射的列出|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>neutron portmapping-list</code> 列出端口映射。</li></ol></li></ul>|<ul><li>CLI:<ul><li>成功列出该租户下的端口映射列表</li></ul></li></ul>|||None|
|01010503|测试现实端口映射的详细信息|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>neutron portmapping-show [PORTMAPPING_ID]</code> 查看某个端口映射的详细信息。</li></ol></li></ul>|<ul><li>CLI:<ul><li>成功查看该端口映射的详细信息</li></ul></li></ul>|||None|
|01010504|测试端口映射的更新|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>neutron portmapping-update [PORTMAPPING_ID] --admin\_state\_up False</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>成功将端口映射的管理员状态更新为 False，即关闭该端口映射</li><li>执行命令 <code> neutron portmapping-show [PORTMAPPING_ID]</code> 查看该端口映射，看到 admin\_state_\up 为 False</li></ul></li></ul>|||None|
|01010504|测试端口映射的更新|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>neutron portmapping-update --name [NEW_NAME] [PORTMAPPING_ID]</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>成功将端口映射的名称修改为所指定的新的名称</li><li>执行命令 <code> neutron portmapping-show [PORTMAPPING_ID]</code> 查看该端口映射，看到名称改变</li></ul></li></ul>|||None|
|01010505|测试端口映射的删除|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>neutron portmapping-delete [PORTMAPPING_ID]</code> 删除端口映射。</li></ol></li></ul>|<ul><li>CLI:<ul><li>成功删除该端口映射</li><li>执行 <code>neutron portmapping-list</code>，列表中不再现实该端口映射的信息</li></ul></li></ul>|||None|
