# 验证 Ceilometer 组件的 alarm 部分

|内容编号|内容名称|
|--------|--------|
||警报|

|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
||测试警报的创建|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行创建命令 <code>ceilometer alarm-create --name \<ALARM\_NAME\> -m \<METER\_NAME\> --threshold \<THRESHOLD\></code>；</li><li>验证警报是否成功创建。</li></ol></li><li>Rally:<ol><li>登录到 Rally 测试服务器；</li><li>切换到测试目录下，执行测试命令 <code>rally task start create-alarm.yaml</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>警报创建成功；</li><li>使用命令 <code>ceilometer alarm-list</code> 可以看到新创建的警报出现在列表中。</li></ul></li><li>Rally:<ul><li>Rally 测试执行成功。</li></ul></li></ul>||执行 10 次，并行任务数为 1|Rally:</br>create-alarm.yaml|
||测试列出警报|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>ceilometer alarm-list</code>。</li></ol></li><li>Rally:<ol><li>登录到 Rally 测试服务器；</li><li>切换到测试目录下，执行测试命令 <code>rally task start list-alarm.yaml</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>成功列出警报。</li></ul></li><li>Rally:<ul><li>Rally 测试执行成功。</li></ul></li></ul>||执行 10 次，并行任务数为 1|Rally:</br>list-alarm.yaml|
||测试警报的创建和列出|<ul><li>Rally:<ol><li>登录到 Rally 测试服务器；</li><li>切换到测试目录下，执行测试命令 <code>rally task start create-and-list-alarm.yaml</code>。</li></ol></li></ul>|<ul><li>Rally:<ul><li>Rally 测试执行成功。</li></ul></li></ul>||执行 10 次，并行任务数为 1|Rally:</br>create-and-list-alarm.yaml|
||测试警报的更新功能|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行更新命令 <code>ceilometer alarm-update \<ALARM\_ID\></code>；</li><li>在命令中加上对应的参数来指定修改的内容，如 --name 等，详细使用可用 help 查看</li></ol></li><li>Rally:<ol><li>登录到 Rally 测试服务器；</li><li>切换到测试目录下，执行测试命令 <code>rally task start create-and-update-alarm.yaml</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>成功更新警报；</li><li>使用 <code>ceilometer alarm-show \<ALARM\_ID\></code> 查看该警报的信息，看到警报信息被更新。</li></ul></li><li>Rally:<ul><li>Rally 测试执行成功。</li></ul></li></ul>||执行 10 次，并行任务数为 1|Rally:</br>create-and-update-alarm.yaml|
||测试获取警报的历史更新信息|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>ceilometer alarm-history \<ALARM\_ID\></code>。</li></ol></li><li>Rally:<ol><li>登录到 Rally 测试服务器；</li><li>切换到测试目录下，执行测试命令 <code>rally task start create-alarm-and-get-history.yaml</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>查询警报更新历史成功，列出警报状态更新的历史记录。</li></ul></li><li>Rally:<ul><li>Rally 测试执行成功。</li></ul></li></ul>||执行 10 次，并行任务数为 5|Rally:</br>create-alarm-and-get-history.yaml|
||测试通过查询过滤警报的历史更新信息？？|||||Rally:</br>create-and-query-alarm-history.yaml|
||测试通过查询过滤警报的列表信息？？？？|||||Rally:</br>create-and-query-alarms.yaml|
