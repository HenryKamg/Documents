# 验证 Quotas 模块的 cinder 部分

|内容编号|内容名称|
|--------|--------|
|01|cinder|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01090101|修改 cinder 的配额|<ul><li>Ter:</li></ul><ol><li>登录进入控制节点，执行命令Update a particular quota value 可修改特定配置值，例如：cinder quota-update --volumes 15 $tenant修改了cinder的配额。</li></ol><ul><li>CLI:</li></ul><ol><li>登录rally服务器；</li><li>使用rally测试文档cinder-update.json；</li><li>执行测试命令rally task start cinder-update.json；|</li><li>Ter:使用命名验证:cinder quota-show tenant01；</li><li>CLI:rally测试成功。|||Rally:</br>cinder-update.json|
|01090102|Update and Delete quotas for Cinder|<ul><li>Ter:</li></ul><ol><li>登录进入控制节点，执行命令cinder quota-update --quotaName NewValue tenantID 可以修改特定配置值；</li><li>删除quotas for cinder使用命令:cinder quota-delete tenantID。</li></ol><ul><li>CLI:</li></ul><ol><li>登录到rally测试服务器；</li><li>使用rally测试文档cinder-update-and-delete；</li><li>执行测命令rally task start cinder-update-and-delete.json。|</li><li>Ter:能够成功删除</li><li>CLI:rally测试成功。||没有在图形界面找到对应操作，只能够敲命令。|Rally:</br>cinder-update-and-delete.json|
