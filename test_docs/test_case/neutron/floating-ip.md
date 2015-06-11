# floating-ip
|内容编号|内容名称|
|--------|--------|
|06|VPNaaS|

|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01010601|在公网环境下添加子网|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击【网络】子选项，进入网络界面，点击外网，进入外网配置界面；</li><li>点击创建子网按钮，弹出创建子网对话框；</li><li>名称填写“my-public”，网络地址填写“需要添加进去的子网地址”，点击下一步；</li><li>将激活DHCP对话框里的勾去掉，不使用DHCP，点击已创建即创建成功。</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令，在外网下创建子网：<code>neutron subnet-create --allocation-pool start=10.1.101.80,end=10.1.101.100 --gateway 10.1.101.254 net04_ext 10.1.101.0/24 --enable_dhcp=False</code>|<ul><li>UI:<ol><li>子网创建成功。</li></ol></li><li>CLI:<ol><li>子网创建成功。|||||
|01010602|使用固定地址创建路由|<ul><li>UI:<ol><li>登录dashboard，点击【Project】选项，选择【Network】子选项；</li><li>点击【路由】子选项，进入路由配置界面；</li><li>选定需要添加固定IP地址的路由，点击设置网关按钮弹出设置网关界面；</li><li>外部网络选择对应的外部网络，点击设置网关按钮。</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令：<code>eutron router-gateway-set ROUTER-ID EXTERNAL-NETWORK-ID --external-fixed-ip 10.1.101.85</code>|<ul><li>UI:<ol><li>子网IP绑定成为路由网关</li></ol></li><li>CLI:<ol><li>子网IP绑定成为路由网关。||分配给路由器的固定网关IP貌似是随机分配的|||
|01010603|将浮动IP绑定到对应实例|<ul><li>UI:<ol><li>登录dashboard，点击【Project】选项，选择【Compute】子选项；</li><li>点击【实例】选项，进入配置实例界面，选中需要绑定浮动IP的实例，在下拉菜单中点击绑定浮动IP；</li><li>弹出管理浮动IP的关联对话框，在IP地址对话框中点击“+”，弹出可供选择的浮动IP的networkname；</li><li>在待连接的端口对话框中填写实例的内网IP，点击关联。</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令：<code>neutron floatingip-create --port-id PORT-ID --fixe-ip-address 192.168.201.108 --floating-ip-address 10.1.101.83 NETWORK-ID</code>|<ul><li>UI:<ol><li>子网IP绑定成为实例外网与实例子网关联。</li></ol></li><li>CLI:<ol><li>子网IP绑定成为实例外网与实例子网关联。||图形化界面给实例绑定浮动IP时，不能绑定添加的子网|||
|01010604|修改子网|<ul><li>UI:<ol><li>登录dashboard，点击【Project】选项，选择【Network】子选项；</li><li>选择网络选项，点击子所在的外网，在子网对话框中，找到需要修改的子网；</li><li>点击编辑子网按钮，弹出编辑子网对话框；</li><li>可修改子网名称，可选网关等，点击保存。</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令，修改名字：<code>neutron subnet-update  SUBNET-ID --name UPDATE-NAME</code>。|<ul><li>UI:<ol><li>修改子网成功。</li></ol></li><li>CLI:<ol><li>修改子网成功。||其他的参数修改命令行方式一致|||
|01010605|删除子网|<ul><li>UI:<ol><li>登录dashboard，点击【Project】选项，选择【Network】子选项；</li><li>选择网络选项，点击子所在的外网，在子网对话框中，找到需要删除的子网；</li><li>选中子网点击删除子网按钮。</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令，删除子网：<code>neutron subnet-delete SUBNET-ID</code>。|||子网在未被使用的情况下才能成功删除|||
|01010606|解除路由绑定|<ul><li>UI:<ol><li>登录dashboard，点击【Project】选项，选择【Network】子选项；</li><li>选择路由选项，找到需要解除绑定的路由，点击清除网关按钮。</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令:<code>neutron router-gateway-clear ROUTER-ID</code>。|<ul><li>UI:<ol><li>删除子网成功。</li></ol></li><li>CLI:<ol><li>删除子网成功。|||||
|01010607|解除实例绑定|<ul><li>UI:<ol><li>登录dashboard，点击【Project】选项，选择【Compute】子选项；</li><li>选择【访问&安全】选项，点击浮动IP选项找到需要解除绑定的IP并选定，点击释放浮动IP。</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令：<code>neutron floatingip-delete FLOATINGIP-ID</code>。|<ul><li>UI:<ol><li>实例浮动IP释放。</li></ol></li><li>CLI:<ol><li>实例浮动IP释放。|||||


















