# 验证 Neutron 的 QoS

|内容编号|内容名称|
|--------|--------|
|06|QoS|

|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01010601|在公网环境下添加一条QoS|<ul><li>CLI:<ol><li>登录到network节点；</li><li>执行命令，创建QoS并为新建的QoS匹配上port：<code>neutron eayun-qos-create --name test-qos --target-type port --target-id TARGET-ID ingress 102400 20480</code>|<ul><li>CLI:QoS创建成功||可以为QoS匹配对应的port或者router||
|01010602|在公网环境下修改一条QoS|<ul><li>CLI:<ol><li>登录到network节点；</li><li>执行命令，修改限定速率：<code>neutron eayun-qos-update --rate 51200 QOS-ID</code>|<ul><li>CLI:QoS修改成功||可以为QoS修改的选项还有名字，匹配的目标类型等||
|01010603|QoS脱离绑定设备|<ul><li>CLI:<ol><li>登录到network节点；</li><li>执行命令：<code>neutron eayun-qos-unbind QOS-ID</code>。|<ul><li>CLI:QoS成功脱离设备||||
|01010604|在公网环境下删除一条QoS|<ul><li>CLI:<ol><li>登录到network节点；</li><li>执行命令，删除：<code>neutron eayun-qos-delete QOS-ID</code>。|<ul><li>CLI:QoS删除成功||||
|01010605|在QoS中添加队列|<ul><li>CLI:<ol><li>登录到network节点；</li><li>执行命令：<code>neutron eayun-qos-queue-create QOS-ID 20480 --prio 0</code>。|<ul><li>CLI:队列创建成功||要创建子队列只需添加参数<code>--parent PARENT-ID</code>||
|01010606|队列更新|<ul><li>CLI:<ol><li>登录到network节点；</li><li>执行命令：<code>neutron eayun-qos-queue-update --rate 51200 QOS_QUEUE-ID</code>。|<ul><li>CLI:队列更新成功||可以修改的队列参数还有优先级等且默认队列不能更新||
|01010607|队列删除|<ul><li>CLI:<ol><li>登录到network节点；</li><li>执行命令：<code>neutron eayun-qos-queue-delete QOS_QUEUE-ID</code>。|<ul><li>CLI:队列删除成功||||
|01010608|在公网环境下创建过滤器|<ul><li>CLI:<ol><li>登录到network节点；</li><li>执行命令：<code>neutron eayun-qos-filter-create --queue QOS_QUEUE-ID --protocol 6 --src-port 23 --dst-port 23 --src-addr 172.168.200.4/24 --dst-addr 172.168.200.2/24 QOS-ID 104</code>。|<ul><li>CLI:过滤器创建成功||过滤器只能创建在没有子队列的队列中||
|01010609|更新过滤器|<ul><li>CLI:<ol><li>登录到network节点；</li><li>执行命令：<code>neutron eayun-qos-filter-update --prio 200 QOS_FILTER-ID</code>。|<ul><li>CLI:过滤器更新成功||过滤器可以修改的参数还有协议，匹配端口等||
|01010610|过滤器脱离队列|<ul><li>CLI:<ol><li>登录到network节点；</li><li>执行命令：<code>neutron eayun-qos-filter-unattach QOS_FILTER-ID</code>。|<ul><li>CLI:过滤器成功脱离队列||||
|01010611|删除过滤器|<ul><li>CLI:<ol><li>登录到network节点；</li><li>执行命令：<code>neutron eayun-qos-filter-delete QOS_FILTER-ID</code>。|<ul><li>CLI:过滤器成功删除||||
|01010612|验证QoS|<ul><li>UI:<ol><li>登录dashboard，点击【Project】选项，点击【Compute】子选项；</li><li>点击【实例】选项，选择过滤器匹配的两个实例，点击虚拟控制台进入；</li><li>选用合适的网络性能测试工具，在两台实例之间测试流量。|<ul><li>CLI:网络流量按照需求匹配||||









