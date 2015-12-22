# 验证 Ceilometer 组件的 meter 部分

|内容编号|内容名称|
|--------|--------|
||计量|

|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
||测试查看计量列表的功能|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>ceilometer meter-list</code>，查看命令执行结果。</li></ol></li><li>Rally:<ol><li>登录到 Rally 测试服务器；</li><li>切换到测试目录，执行测试命令 <code>rally task start list-meters.yaml</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>成功列出所有的计量。</li></ul></li>Rally:<ul><li>Rally 测试执行成功。</li></ul></li></ul>||执行 10 次，并行任务数为 1|Rally:</br>list-meters.yaml|
||测试查看某种计量统计数据的功能|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>ceilometer statistics --meter \<METER\_NAME\></code>，查看命令执行结果。</li></ol></li><li>Rally:<ol><li>登录到 Rally 测试服务器；</li><li>切换到测试目录，执行测试命令 <code>rally task start create-meter-and-get-stats.yaml</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>成功列出计量的统计数据。</li></ul></li><li>Rally:<ul><li>Rally 测试执行成功。</li></ul></li></ul>||执行 100 次，并行任务数为 5|Rally:</br>create-meter-and-get-stats.yaml|
||测试列出匹配的计量|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>ceilometer meter-list</code>，查看命令执行结果（需要添加参数进行查询）。</li></ol></li><li>Rally:<ol><li>登录到 Rally 测试服务器；</li><li>切换到测试目录，执行测试命令 <code>rally task start list-matched-meters.yaml</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>成功列出所有匹配的计量。</li></ul></li>Rally:<ul><li>Rally 测试执行成功。</li></ul></li></ul>||执行 5 次，并行任务数为 1|Rally:</br>list-matched-meters.yaml|
