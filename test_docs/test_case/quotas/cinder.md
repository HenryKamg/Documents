# 验证 Quotas 模块的 cinder 部分

|内容编号|内容名称|
|--------|--------|
|01|cinder|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01090101|修改 cinder volume 的配额|<ul><li>Ter:<ol><li>登录进入控制节点，执行命令 <code>cinder quota-update --volumes 15 \<tenant_id\></code> 。</li></ol></li><li>CLI:<ol><li>登录rally服务器；</li><li>使用rally测试文档cinder-update.json；</li><li>执行测试命令 <code>rally task start cinder-update.json</code>。</li></ol></li></ul>|<ul><li>Ter:<ul><li>命令执行成功，输出信息中，看到 volume 的配额由 10 -> 15</li></ul></li><li>CLI:<ul><li>rally测试成功</li></ul></li></ul>|||Rally:</br>cinder-update.json|
|01090102|更新 cinder volume 的配额后，将该租户的配额删除|<ul><li>Ter:<ol><li>登录进入控制节点，执行命令 <code>cinder quota-update --volume 20 \<tenant_id\></code>，更新配额；</li><li>执行命令 <code>cinder quota-delete \<tenant_id\></code>，删除该租户的配额</li></ol></li><li>CLI:<ol><li>登录到rally测试服务器；</li><li>使用rally测试文档cinder-update-and-delete；</li><li>执行测命令 <code>rally task start cinder-update-and-delete.json</code>。</li></ol></li></ul>|<ul><li>Ter:<ul><li>更新 cinder volume 的配额成功，输出的新的配额信息中，volume 的配额被更新 15 -> 20</li><li>删除该租户的配额后，执行命令 <code>cinder quota-show \<tenant_id\></code>，可以看到该用户的所有配额恢复到默认配额(如 cinder volume 的配额恢复到 10 的默认配额)</li></ul></li><li>CLI:<ul><li>rally测试成功。</li></ul></li></ul>|||Rally:</br>cinder-update-and-delete.json|
