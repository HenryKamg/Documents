# 验证 Neutron 的 subnet 部分

|内容编号|内容名称|
|--------|--------|
|04|子网|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01070401|创建并列出子网|<ul><li>UI:<ol><li>登录dashboard，点击项目选项选择网路再点开网络子选项；</li><li>选择要创建子网的网络点击进入，在子网选项框中选择创建子网；</li><li>子网名称“subnet1”，网络地址选择内网地址“172.168.200.0/22”IP版本“IPv4”，网关IP“172.168.200.1”；</li><li>子网详情中，选择激活DHCP，分配地址池：172.168.200.2,172.168.200.100，然后点击已创建。</li><li>点击进入对应网络当中就可以看到子网列表。</li></ol></li><li>CLI:<ol><li>登录rally测试服务器;</li><li>使用rally测试文档create_and_list_subnets.yaml；</li><li>执行测试命令```rally task start create_and_list_subnets.yaml```。</li></ol></li></ul>|<ul><li>UI:<ul><li>能够成功创建子网并能够在网络下看到子网列表。</li></ul></li><li>CLI:<ul><li>rally测试成功</li></ul></li></ul>|||Rally:</br>create_and_list_subnets.yaml|
|01070402|创建子网后，将其删除|<ul><li>UI:<ol><li>登录dashboard，点击项目选项选择网路再点开网络子选项；</li><li>选择要创建子网的网络点击进入，在子网选项框中选中要删除的子网打上勾，点击右上方删除子网。</li></ol></li><li>CLI:<ol><li>登录rally测试服务器</li><li>使用rally测试文档create_and_delete_subnets.yaml；</li><li>执行测试命名```rally task start create_and_delete_subnets.yaml```。</li></ol></li></ul>|</li><li>UI:<ul><li>能够成功删除子网</li></ul></li><li>CLI:<ul><li>rally 测试成功</li></ul></li></ul>|||Rally:</br>create_and_delete_subnets.yaml|
|01070403|测试 neutron subnet-update 命令的性能|<ul><li>UI:<ol><li>登录dashboard，点击项目选项选择网路再点开网络子选项；</li><li>选择要修改的子网点击对话框里的编辑子网，对子网进行修改。</li></ol></li><li>CLI:<ol><li>登录rally测试服务器；</li><li>使用rally测试文档create_and_update_subnets.yaml；</li><li>执行测试命令```rally task start create_and_update_subnets.yaml```。</li></ol></li></ul>|<ul><li>UI:<ul><li>能够成功的编辑修改子网。</li></ul></li><li>CLI:<ul><li>rally测试成功</li></ul></li></ul>||创建子网后，修改子网|Rally:</br>create_and_update_subnets.yaml|
