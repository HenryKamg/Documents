# 验证 Ceilometer 组件的 resource 部分

|内容编号|内容名称|
|--------|--------|
||资源|

|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
||测试列出资源的功能|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>ceilometer resource-list</code>，列出所有资源的信息。</li></ol></li><li>Rally:<ol><li>登录到 Rally 测试服务器；</li><li>切换到测试目录下，执行测试命令 <code>rally task start list-resources.yaml</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>成功列出所有的资源。</li></ul></li><li>Rally:<ul><li>Rally 执行测试成功。</li></ul></li></ul>||执行 10 次，并行任务数为 1|Rally:</br>list-resources.yaml|
||测试列出匹配的资源|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>ceilometer resource-list</code>，（添加筛选参数）列出所有匹配资源的信息。</li></ol></li><li>Rally:<ol><li>登录到 Rally 测试服务器；</li><li>切换到测试目录下，执行测试命令 <code>rally task start list-resources.yaml</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>成功列出所有的资源。</li></ul></li><li>Rally:<ul><li>Rally 执行测试成功。</li></ul></li></ul>||执行 10 次，并行任务数为 1|Rally:</br>list-matched-resources.yaml|
