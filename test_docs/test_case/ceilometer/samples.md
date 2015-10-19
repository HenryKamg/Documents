# 验证 Ceilometer 组件的 sample 部分

|内容编号|内容名称|
|--------|--------|
||样品|

|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
||测试列出样品的功能|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>ceilometer sample-list</code>，列出样品列表。</li></ol></li><li>Rally:<ol><li>登录到 Rally 测试服务器；</li><li>切换到测试目录下，执行测试命令 <code>rally task start list-samples.yaml</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>成功列出样品列表。</li></ul></li><li>Rally:<ul><li>Rally 测试执行成功。</li></ul></li></ul>||执行 10 次，并行任务数为 2|Rally:</br>list-samples.yaml|
||测试创建样品，并根据条件查询样品|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>ceilometer sample-create -r \<RESOURCE\_ID\> -m \<METER\_NAME\> --meter-type \<METER\_TYPE\> --meter-unit \<METER\_UNIT\> --sample-volume \<SAMPLE\_VOLUME\></code>，创建样品；</li><li>根据条件查询样品，执行命令 <code>ceilometer query-samples -f \<FILTER\> -o \<ORDERBY\> -l \<LIMIT\></code>，查看查询结果。</li></ol></li><li>Rally:<ol><li>登录到 Rally 测试服务器；</li><li>切换到测试目录下，执行测试命令 <code>rally task start create-and-query-samples.yaml</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>创建样品成功；</li><li>成功根据所设置的条件查询样品。</li></ul></li><li>Rally:<ul><li>Rally 测试执行成功。</li></ul></li></ul>||执行 100 次，并行任务数为 10|Rally:</br>create-and-query-samples.yaml|
