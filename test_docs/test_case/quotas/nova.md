# 验证 Quotas 模块的 nova 部分

|内容编号|内容名称|
|--------|--------|
|03|nova|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01090301|修改 nova 的配额|<ul><li>Ter:<ol><li>登录控制节点，执行修改nova配额的命令；</li><li>修改存在的默认的配额，执行命令```nova quota-class-update --key value default``` ；例如修改实例号执行命令:```nova quota-class-update --instances 15 default```。</li><li>为存在的租户修改配额使用命令:```nova quota-update --quotaName quotaValue tenantID```；例如浮动IP大小:```nova quota-update --floating-ips 20 tenantID```。</li></ol></li><li>CLI:<ol><li>登录rally测试服务器；</li><li>使用rally测试文档nova-update.yaml；</li><li>执行命令:```rally task start nova-update.yaml```。|<ul><li>Ter:<ul><li>修改默认配额成功，使用命令```nova quota-defaults``` 可以查看到修改成功的配额</li><li>使用命令```nova quota-show --tenant tenantID``` 可以查看到存在的租户修改的配额</li></ul></li><li>CLI:<ul><li>Rally 测试成功</li></ul></li></ul>||修改配额分为修改默认配额和为租户修改配额|Rally:</br>nova-update.yaml|
|01090302|删除 nova 的配额|<ul><li>Ter:<ol><li>登录控制节点，执行update quotas操作，执行命令```nova quota-update <tenant_id>```；</li><li>执行 delete quotas操作，执行命令```nova quota-delete <tenant_id>```</li></ol></li><li>CLI:<ol><li>登录rally测试服务器；</li><li>使用测试文档nova-update-and-delete.yaml；</li><li>执行命令:```rally task start nova-update-and-delete.yaml```。</li></ol></li></ul>|<ul><li>Ter:<ul><li>成功执行命令</li><li>nova 的配额恢复到默认值</ul></li><li>CLI:<ul><li>Rally测试成功。</li></ul></li></ul>||quota delete 功能会使设置的配额变为默认|Rally:</br>nova-update-and-delete.yaml|
