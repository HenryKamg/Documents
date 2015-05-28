# floating-ip
|内容编号|内容名称|
|--------|--------|
|08|VPNaaS|

|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01010801|在公网环境下添加子网|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击【网络】子选项，进入网络界面，点击外网，进入外网配置界面；</li><li>点击创建子网按钮，弹出创建子网对话框；</li><li>名称填写“my-public”，网络地址填写“需要添加进去的子网地址”，点击下一步；</li><li>将激活DHCP对话框里的勾去掉，不使用DHCP，点击已创建即创建成功。</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令，在外网下创建子网：<code>neutron subnet-create --allocation-pool start=10.1.101.80,end=10.1.101.100 --gateway 10.1.101.254 net04_ext 10.1.101.0/24 --enable_dhcp=False</code>||||||
|01010802|使用固定地址创建路由|<ul><li>UI:<ol><li>登录dashboard，点击【Project】选项，选择【Network】子选项；</li><li>点击【路由】子选项，进入路由配置界面；</li><li>选定需要添加固定IP地址的路由，点击进入……(未完待续)</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令：<code>eutron router-gateway-set ROUTER-ID EXTERNAL-NETWORK-ID --external-fixed-ip 10.1.101.85</code>||||||
|01010803|将浮动IP绑定到对应实例|<ul><li>UI:<ol><li>登录dashboard，点击【Project】选项，选择【Compute】子选项；</li><li>点击【实例】选项，进入配置实例界面，选中需要绑定浮动IP的实例，在下拉菜单中点击绑定浮动IP；</li><li>弹出管理浮动IP的关联对话框，在IP地址对话框中点击“+”，弹出可供选择的浮动IP的networkname；</li><li>在待连接的端口对话框中填写实例的内网IP，点击关联。</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令：<code>neutron floatingip-create --port-id PORT-ID --fixed-ip-address 192.168.201.108 --floating-ip-address 10.1.101.83 NETWORK-ID</code>|||图形化界面给实例绑定浮动IP时，不能绑定添加的子网|||


















