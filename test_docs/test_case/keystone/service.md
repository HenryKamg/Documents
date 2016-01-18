# 验证 Keystone 对 service 的处理

|内容编号|内容名称|
|--------|--------|
|01|服务|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01050101|创建并列出服务|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>keystone service-create --name \<name\> --type \<type\></code></li><li>创建后执行命令 <code>keystone service-list</code></li></ol></li><li>Rally:<ol><li>登录到 Rally 测试服务器；</li><li>使用测试文件 create-and-list-services.yaml；</li><li>执行测试命令 <code>rally task start create-and-list-services.yaml</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>服务创建成功</li><li>列出的服务中可以看到新建的服务的信息</li></ul></li><li>Rally:<ul><li>Rally 测试成功</li></ul></li></ul>||执行 100 次，每次并行执行 10 个测试|Rally:</br>create-and-list-services.yaml|
|01050102|使用普通用户创建服务|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>使用 OpenStack 的普通用户执行命令 <code>keystone service-create --name \<name\> --type \<type\></code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>命令执行不成功</li><li>提示信息为："You are not authorized to perform the requested action: admin_required (HTTP 403)"|||None|
|01050103|删除服务|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>keystone service-delete \<service_id or service_name\></code></li></ol></li><li>Rally:<ol><li>登录到 Rally 测试服务器；</li><li>使用测试文件 create-and-delete-service.yaml；</li><li>执行测试命令 <code>rally task start create-and-delete-service.yaml</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>服务删除成功</li><li>执行命令 <code>keystone service-list</code> 的结果中不再显示被删除的服务的信息</li></ul></li><li>Rally:<ul><li>Rally 测试成功</li></ul></li></ul>||执行 100 次，每次并行执行 10 个测试|Rally:</br>create-and-delete-service.yaml|
