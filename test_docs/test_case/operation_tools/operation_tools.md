#运维工具
|内容编号|内容名称|
|--------|--------|
|01|运维工具|

|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01090101|测试 ```eayunstack -h``` 命令的功能|<ol>CLI:<li>登录到任意节点;</li><li>执行命令```eayunstack -h```</li></ol>|<ol>CLI:<li>查看帮助成功,显示帮助信息</li></ol>||||
|01090102|测试 ```eayunstack list``` 命令的功能|<ol>CLI:<li>登录到任意节点</li><li>执行命令```eayunstack list```</li></ol>|<ol>CLI:<li>查看eayunstack节点列表成功,显示eayunstack所有节点信息</li></ol>||||
|01090103|测试 ```eayunstack doctor all``` 命令的功能|<ol>CLI:<li>登录到fuel节点</li><li>执行命令```eayunstack doctor all```</li></ol>|<ol>CLI:<li>检查所有对象成功</li></ol>||在其他节点执行则检查当前节点的状态||
|01090104|测试```eayunstack doctor cls -n rabbitmq```命令的功能|<ol>CLI:<li>登录到fuel节点</li><li>执行命令```eayunstack doctor cls -n rabbitmq```</li><li>登录到controller节点</li><li>执行命令```eayunstack doctor cls -n rabbitmq```</li></ol>|<ol>CLI:<li>检查所有controller节点上的rabbitmq的状态成功</li><li>检查所在的controller节点上的rabbitmq的状态成功</li></ol>||-n的参数为集群名称||
|01090105|测试```eayunstack doctor stack --controller```命令的功能|<ol>CLI:<li>登录到fuel节点</li><li>执行命令```eayunstack doctor stack --controller``</li></ol>|<ol>CLI:<li>对所有controller节点进行检测</li></ol>||后面的参数可以指定为其他节点||
|01090106|测试```eayunstack doctor net vrouter```命令的功能|<ol>CLI:<li>登录到controller节点</li><li>执行命令```eayunstack doctor net vrouter```</li></ol>|<ol>CLI:<li>检查虚拟路由,返回状态</li></ol>||只能在网络节上执行||
|01090107|测试```eayunstack doctor env -n network```命令的功能|<ol>CLI:<li>登录到controller节点</li><li>执行命令```eayunstack doctor env -n network```</li></ol>|<ol>CLI:<li>检测当前节点的网卡状态</li></ol>||-n参数指定不同的基础环境||
|01090108|测试```eayunstack manage ami --kernel-file vmlinuz-3.2.0-23-generic --initrd-file initrd.img-3.2.0-23-generic --image-file eayun-ubuntu-12.04-x64-raw-v1.img --name ubuntu-12.04 ```命令的功能|<ol>CLI:<li>登录到controller节点</li><li>执行命令```eayunstack manage ami --kernel-file vmlinuz-3.2.0-23-generic --initrd-file initrd.img-3.2.0-23-generic --image-file eayun-ubuntu-12.04-x64-raw-v1.img --name ubuntu-12.04```</li></ol>|<ol>CLI:<li>上传ami镜像成功</li></ol>||只能在controller节点执行该命令||
|01090109|测试```eayunstack manage volume -d --id d77b5983-95d6-4c07-9382-544453975b98```命令的功能|<ol>CLI:<li>登录到controller节点</li><li>执行命令```eayunstack manage volume -d --id d77b5983-95d6-4c07-9382-544453975b98```</li></ol>|<ol>CLI:<li>成功删除一个volume</li></ol>||只能在controller节点上使用||
|01090110|测试```eayunstack init```命令的功能|<ol>CLI:<li>登录到fuel节点</li><li>执行命令```eayunstack init```</li></ol>|<ol>CLI:<li>对EayunStack环境进行初始化操作，在整个环境中的所有节点生成保存了节点角色和节点信息列表的配置文件</li></ol>||只能在fuel节点上使用||
|01090111|测试```eayunstack fuel backup -n```命令的功能|<ol>CLI:<li>登录到fuel节点</li><li>执行命令```eayunstack fuel backup -n```</li></ol>|<ol>CLI:<li>对fuel节点进行备份</li></ol>||只能在fuel节点上使用||
|01090112|测试```eayunstack fuel backup -l```命令的功能|<ol>CLI:<li>登录到fuel节点</li><li>执行命令```eayunstack fuel backup -l```</li></ol>|<ol>CLI:<li>列出fuel节点的备份信息</li></ol>||只能在fuel节点上使用||
|01090113|测试```eayunstack fuel restore -i 1```命令的功能|<ol>CLI:<li>登录到fuel节点</li><li>执行命令```eayunstack fuel restore -i 1```</li></ol>|<ol>CLI:<li>成功恢复备份的信息</li></ol>||只能在fuel节点上使用||
|01090114|测试```eayunstack fuel ceph_cluster_network --env 1 --cidr 172.16.200.0/24 --nic_mappings 6:eth4,7:eth4,8:eth4```命令的功能|<ol>CLI:<li>登录到fuel节点</li><li>执行命令```eayunstack fuel ceph_cluster_network --env 1 --cidr 172.16.200.0/24 --nic_mappings 6:eth4,7:eth4,8:eth4```</li></ol>|<ol>CLI:<li>成功配置ceph cluster网络</li></ol>||只能在fuel节点上使用||





