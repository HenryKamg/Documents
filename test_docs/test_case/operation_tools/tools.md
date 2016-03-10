# 运维工具

|内容编号|内容名称|
|--------|--------|
|01|运维工具|

|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01040101|测试运维工具的帮助命令|<ul><li>CLI:<ol><li>登录到任意节点；</li><li>执行命令 <code>eayunstack -h</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>查看帮助成功，显示帮助信息</li></ul></li></ul>|||None|
|01040102|测试运维工具列出节点信息的功能|<ul><li>CLI:<ol><li>登录到任意节点；</li><li>执行命令 <code>eayunstack list</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>查看 eayunstack 节点列表成功,显示 eayunstack 所有节点信息</li></ul></li></ul>||||
|01040103|测试运维工具检查所有节点健康状态的功能|<ul><li>CLI:<ol><li>登录到 fuel 节点；</li><li>执行命令 <code>eayunstack doctor all</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>能够成功检查所有节点的健康状态</li></ul></li></ul>||在其他节点执行则检查当前节点的健康状态||
|01040104|测试运维工具检查集群状态的功能|<ul<li>CLI:<ol><li>登录到 fuel 节点</li><li>执行命令 <code>eayunstack doctor cls -n rabbitmq</code>；</li><li>登录到 Controller 节点；</li><li>执行命令 <code>eayunstack doctor cls -n rabbitmq</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>在 Fuel 节点上执行时，可以检查所有 Controller 节点上的 rabbitmq 的状态</li><li>在 Controller 节点上执行时，可以检查所在的 Controller 节点上的 rabbitmq 的状态</li></ul></li></ul>||-n 的参数为集群名称||
|01040105|测试运维工具检查某个节点角色的组件和配置文件状态的功能|<ul><li>CLI:<ol><li>登录到 fuel 节点</li><li>执行命令 <code>eayunstack doctor stack --controller</code></li></ol></li></ul>|<ul><li>CLI:<ul><li>检查所有 Controller 节点的健康状态</li></ul></li></ul>||后面的参数可以指定为其他节点||
|01040106|测试运维工具检查虚拟路由的功能|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>eayunstack doctor net vrouter</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>成功检查当前节点上的虚拟路由，并返回路由的状态</li></ul></li></ul>||只能在网络节上执行，在本环境中即 Controller 节点||
|01040107|测试运维工具检查基础环境状态的功能|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>eayunstack doctor env -n network</code></li></ol></li></ul>|<ul><li>CLI:<ul><li>成功检测当前节点的网卡状态</li><li>如果网卡状态正常，命令无任何输出</li><li>加上 --debug 参数后，可以看到 DEBUG 输出信息</li></ul></li></ul>||-n 参数指定不同的基础环境||
|01040108|测试使用运维工具上传 AMI 镜像的功能|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>eayunstack manage ami --kernel-file vmlinuz-3.2.0-23-generic --initrd-file initrd.img-3.2.0-23-generic --image-file eayun-ubuntu-12.04-x64-raw-v1.img --name ubuntu-12.04</code>，其中要指定 kernel 文件、initrd 文件和 image 文件。</li></ol></li></ul>|<ul><li>CLI:<ul><li>上传 AMI 镜像成功</li></ol></li></ul>||只能在 Controller 节点执行该命令||
|01040109|测试运维工具删除错误卷的功能|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>eayunstack manage volume -d --id VOLUME_ID</code>，其中，该卷处于非 Available 状态。</li></ol></li></ul>|<ul><li>CLI:<ul><li>成功删除一个卷</li></ul></li></ul>||只能在 Controller 节点上使用||
|01040110|测试使用运维工具删除一个包含快照的卷|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>eayunstack manage volume -d --id VOLUME_ID</code>，其中，该卷处于 Available 状态，但创建了该卷的快照。</li></ol></li></ul>|<ul><li>CLI:<ul><li>成功删除卷的快照，并将卷删除</li></ul></li></ul>||只能在 Controller 节点上使用||
|01040111|测试运维工具初始化环境命令的功能|<ul><li>CLI:<ol><li>登录到 fuel 节点；</li><li>执行命令 <code>eayunstack init</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>对 EayunStack 环境进行初始化操作，在整个环境中的所有节点生成保存了节点角色和节点信息列表的配置文件</li></ul></li></ul>||只能在 fuel 节点上使用||
|01040112|测试运维工具更新初始化配置的功能|<ul><li>CLI:<ol><li>登录到 fuel 节点；</li><li>执行命令 <code>eayunstack init -u</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>对 EayunStack 环境的初始化配置文件更新，在整个环境中的所有节点重新生成保存了节点角色和节点信息列表的配置文件</li></ul></li></ul>||只能在 fuel 节点上使用||
|01040113|测试运维工具备份 Fuel 的功能|<ul><li>CLI:<ol><li>登录到 Fuel 节点；</li><li>执行命令 <code>eayunstack fuel backup -n</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>对 fuel 节点进行备份</li></ul></li></ul>||只能在 Fuel 节点上使用||
|01040114|测试运维工具列出 Fuel 的所有备份的功能|<ul><li>CLI:<ol><li>登录到 Fuel 节点；</li><li>执行命令 <code>eayunstack fuel backup -l</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>列出 fuel 节点的备份信息</li></ul></li></ul>||只能在 fuel 节点上使用||
|01040115|测试运维工具恢复 Fuel 节点的功能|<ul><li>CLI:<ol><li>登录到 fuel 节点；</li><li>执行命令 <code>eayunstack fuel backup -l</code>，列出所有的备份信息，记录所要恢复的备份的 ID（在本例中 ID 为 1）</li><li>执行命令 <code>eayunstack fuel restore -i 1</code>，进行恢复。</li></ol></li></ul>|<ul><li>CLI:<ul><li>成功恢复 Fuel 节点到指定的备份</li></ul></li></ul>||<ul><li>只能在 fuel 节点上使用</li><li>使用 -f 参数，可以指定备份文件，如从 U 盘的备份中恢复 Fuel</li></ul>||
