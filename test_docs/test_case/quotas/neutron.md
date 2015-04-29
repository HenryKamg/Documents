# 测试 Quotas 的 neutron 部分

|内容编号|内容名称|
|--------|--------|
|02|neutron|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01090201|修改 neutron 的配额|<ul><li>Ter:<ol><li>登录控制节点，使用命令修改neutron，执行命令```neutron quota-update --tenant_id <tenant_id> --network 5```</li></ol></li><li>CLI:<ol><li>登录rally测试服务器；</li><li>使用rally测试文档neutron-upddate.yaml；</li><li>执行命令rally task start neutron-update.yaml。</li></ol></li></ul>|</li><li>Ter:<ul><li>修改配额成功，使用命令neutron quota-show 可查看到修改成功的配额。</li></ul></li><li>CLI:<ul><li>Rally测试成功</li></ul></li></ul>|||Rally:</br>neutron-update.yaml|
