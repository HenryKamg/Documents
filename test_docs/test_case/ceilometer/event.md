# 验证 Ceilometer 组件的 event 部分

|内容编号|内容名称|
|--------|--------|
||事件|

|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
||测试列出事件的功能|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>ceilometer event-list</code>，查看命令显示结果。</li></ol></li><li>Rally:<ol><li>登录到 Rally 测试服务器；</li><li>切换到测试目录，执行测试命令 <code>rally task start create\_user\_and\_list\_events.yaml</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>获取事件列表成功，将列出该用户下所有事件的列表。</li></ul></li>Rally:<ul><li>Rally 测试执行成功。</li></ul></li></ul>|执行 10 次，并行任务数为 10|Rally:</br>create\_user\_and\_list\_events.yaml|
||测试列出某个事件详细信息的功能|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>ceilometer event-show \<EVENT\_ID\></code>，查看事件的详细信息。</li></ol></li>Rally:<ol><li>登录到 Rally 测试服务器；</li><li>切换到测试目录，执行测试命令 <code>rally task start create\_user\_and\_get\_event.yaml</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>获取事件详细信息成功，将列出该事件的详细信息。</li></ul></li>Rally:<ul><li>Rally 测试执行成功。</li></ul></li></ul>|执行 10 次，并行任务数为 10|Rally:</br>create\_user\_and\_get\_event.yaml|
||测试列出事件类型的功能|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>ceilometer event-type-list</code>，查看命令显示结果。</li></ol></li><li>Rally:<ol><li>登录到 Rally 测试服务器；</li><li>切换到测试目录，执行测试命令 <code>rally task start create\_user\_and\_list\_event\_types.yaml</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>获取事件类型列表成功，将列出事件类型的列表。</li></ul></li>Rally:<ul><li>Rally 测试执行成功。</li></ul></li></ul>|执行 10 次，并行任务数为 10|Rally:</br>create\_user\_and\_list\_event\_types.yaml|
