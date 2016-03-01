# 验证 Ceilometer 组件的 trait 部分

|内容编号|内容名称|
|--------|--------|
|02|Trait|

|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01020201|列出某个事件类型的属性描述列表|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>ceilometer trait-description-list -e \<EVENT\_TYPE\></code>，其中，event_type 可以通过 <code>ceilometer event-type-list</code> 获取。</li></ol></li><li>Rally:<ol><li>登录到 Rally 测试服务器；</li><li>切换到测试目录下，执行测试命令 <code>rally task start create\_user\_and\_list\_trait\_descriptions.yaml</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>成功列出某个事件类型的属性描述信息；</li><li>可以知道该事件类型中属性的数据类型。</li></ul></li><li>Rally:<ul><li>Rally 测试执行成功。</li></ul></li></ul>||执行 10 次，并行任务数为 10|Rally:</br>create\_user\_and\_list\_trait\_descriptions.yaml|
|01020202|列出某个事件类型的某个属性的信息|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>ceilometer trait-list -e \<EVENT\_TYPE\></code> -t \<TRAIT\_NAME\></code>，其中，trait_name 可以通过 <code>ceilometer trait-description-list -e \<EVENT\_TYPE\></code> 获取。</li></ol></li><li>Rally:<ol><li>登录到 Rally 测试服务器；</li><li>切换到测试目录下，执行测试命令 <code>rally task start create\_user\_and\_list\_traits.yaml</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>成功列出某个事件类型的某个属性的信息。</li></ul></li><li>Rally:<ul><li>Rally 测试执行成功。</li></ul></li></ul>||执行 10 次，并行任务数为 10|Rally:</br>create\_user\_and\_list\_traits.yaml|
