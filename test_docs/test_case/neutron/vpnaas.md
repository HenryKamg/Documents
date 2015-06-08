# VPNaaS
|内容编号|内容名称|
|--------|--------|
|08|VPNaaS|

|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01010801|创建ike-policy|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击 【Networks】 选项，点击【VPN】子选项，进入VPN配置界面；</li><li>点击IKE策略选项，点击添加IKE策略，弹出添加IKE策略对话框；</li><li>填写名称“my-ikepolicy”，点击添加；</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令添加ike-policy：<code>neutron vpn-ikepolicy-create my-ikepolicy</code>|<ul><li>UI:<ol><li>ike-policy创建成功。</li></ol></li><li>CLI:<ol><li>ike-policy创建成功。||算法在没有特殊要下选择默认即可|||
|01010802|创建ipsec-policy|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击 【Networks】 选项，点击【VPN】子选项，进入VPN配置界面；</li><li>点击IPSec策略选项，点击添加IPSec策略，弹出添加IPSec策略对话框；</li><li>名称填写“my-ipsecpolicy”，点击添加按钮；</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令添加ipsec-policy：<code>neutron vpn-ipsecpolicy-create my-ipsecpolicy</code>|<ul><li>UI:<ol><li>ipsec-policy创建成功。</li></ol></li><li>CLI:<ol><li>ipsec-policy创建成功。||算法在没有特殊要下选择默认即可|||
|01010803|创建VPN服务|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击 【Networks】 选项，点击【VPN】子选项，进入VPN配置界面；</li><li>点击VPN服务选项，点击添加VPN服务，弹出添加VPN服务对话框；</li><li>名称填写“my-vpnserviceA”，路由选择需要建立VPN服务的实例连接外网的路由器，子网选择实例所在的子网网段，点击添加。</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令，创建一端的VPN服务：<code>neutron vpn-service-create --name my-vpnserviceA router2 sub_net2Created a new vpnservice</code>|<ul><li>UI:<ol><li>vpn服务创建成功。</li></ol></li><li>CLI:<ol><li>vpn服务创建成功。||VPN服务要创建在两个需要使用VPN连接的实例上，此处只列举了一个实例上的服务配置，另一个命令相同|||
|01010804|创建ipsec站点连接|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击 【Networks】 选项，点击【VPN】子选项，进入VPN配置界面；</li><li>点击IPSec站点连接选项，点击添加IPSec站点连接弹出添加IPSec站点连接对话框；</li><li>名称填写“my-connectionA”，VPN服务选择好的用于此连接的服务，选择可用的IKE策略，选择可用的IPSec策略；</li><li>伙伴网关公共IPV4填写“对端建立VPN路由的外网”，伙伴ID填写“对端路由器ID”，PSK填写“abc123”,点击添加。</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令，创建一端的IPSec站点连：<code>neutron ipsec-site-connection-create --name my-connectionA --vpnservice-id VPNSERVICE-ID --ikepolicy-id IKEPOLICY-ID --ipsecpolicy-id IPSECPOLICY-ID --peer-address 25.0.0.130 --peer-id 25.0.0.130 --peer-cidr 192.168.201.0/24 --psk abc123</code>|<ul><li>UI:<ol><li>ipsec站点创建成功。</li></ol></li><li>CLI:<ol><li>ipsec站点创建成功。||站点的创建是双向，此处只列出了一端的连接|||
|01010805|修改ike-policy|<ul><li>UI:<ol><li>登录dashboard，点击【Project】选项，点击【network】子选项；</li><li>点击【VPN】选项，点击IKE策略按钮选中需要修改的IKE策略，点击编辑IKE策略，弹出编辑IKE策略对话框；</li><li>可以修改名称，加密算法，IKE版本等，点击保存。</li></ol></li><li>CLI:<ol><li>登录到controller节点上；</li><li>执行下列命修改名字：<code>neutron vpn-ikepolicy-update IKEPOLICY-NAME --name UPDATE-NAME</code>|<ul><li>UI:<ol><li>ike-policy修改成功。</li></ol></li><li>CLI:<ol><li>ike-policy修改成功。||已经将IKE策略绑定到了IPSEC站点的ike-policy将无法修改|||
|01010806|修改ipsec-policy|<ul><li>UI:<ol><li>登录dashboard，点击【Project】选项，点击【network】子选项；</li><li>点击【VPN】选项，点击IPSEC策略按钮，选择需要修改的ipsec策略，点击编辑IPSec策略，弹出编辑IPSec策略对话框；</li><li>可修改名称，封装模式，加密算法等，点击保存按钮。</li></ol></li><li>CLI:<ol><li>登录到controller节点上；</li><li>执行命令修改名字：<code>neutron vpn-ipsecpolicy-update IPSECPOLICY-NAME --name UPDATE-NAME</code>。|<ul><li>UI:<ol><li>ipsec-policy修改成功。</li></ol></li><li>CLI:<ol><li>ipsec-policy修改成功。||</li><li>若ipsecpolicy已绑定到了ipsec连接上将不能修改；</li><li>其他修改的属性命令行方式一样|||
|01010807|修改VPN服务|ul><li>UI:<ol><li>登录dashboard，点击【Project】选项，点击【network】子选项；</li><li>点击【VPN】选项，点击VPN服务，选中需要修改的VPN服务，点击编辑VPN服务按钮弹出编辑VPN服务对话框；</li><li>可修改VPN服务名称。</li></ol></li><li>CLI:<ol><li>登录到controller节点上；</li><li>执行命令修改VPN服务名字：<code>neutron vpn-service-update VPN-SERVICE-ID --name UPDATE-NAME</code>。|<ul><li>UI:<ol><li>vpn服务修改成功。</li></ol></li><li>CLI:<ol><li>vpn服务修改成功。||</li><li>其他属性命令行修改方式一样；</li><li>VPN服务在被绑定到ipsec站点上时，只能修改名称着一个属性|||
|01010808|修改ipsec站点|<ul><li>UI:<ol><li>登录dashboard，点击【Project】选项，点击【network】子选项；</li><li>点击【VPN】选项，点击IPSec站点连接，选择需要修改的IPSec站点连接；</li><li>点击编辑连接，弹出编辑IPSec站点连接对话框；</li><li>可修改名称，对端网关IP，路由器IP，对端子网等，点击保存。</li></ol></li><li>CLI:<ol><li>登录到controller节点上；</li><li>执行命令修改IPSec站点名称：<code>neutron ipsec-site-connection-update IPSEC-CONNECTION-NAME --name UPDATE-NAME。</code>|<ul><li>UI:<ol><li>ipsec站点修改成功。</li></ol></li><li>CLI:<ol><li>ipsec站点修改成功。||修改其他参数的命令行方式一样|||
|01010809|删除ike-policy|<ul><li>UI:<ol><li>登录dashboard，点击【Project】选项，点击【network】子选项；</li><li>点击【VPN】选项，点击IKE策略选中需要删除的IKE策略，点击删除IKE策略按钮。</li></ol></li><li>CLI:<ol><li>登录到controller节点上；</li><li>执行命令：<code>neutron vpn-ikepolicy-delete IKEPOLICY-ID</code>|<ul><li>UI:<ol><li>ike-policy删除成功。</li></ol></li><li>CLI:<ol><li>ike-policy删除成功。||若ike-policy绑定到了ipsec站点需要解除绑定才能删除成功|||
|01010810|删除IPSec策略|<ul><li>UI:<ol><li>登录dashboard，点击【Project】选项，点击【network】子选项；</li><li>点击【VPN】选项，点击IPSec策略按钮选中需要删除的IPSec策略，点击删除IPSec策略按钮。</li></ol></li><li>CLI:<ol><li>登录到controller节点上；</li><li>执行命令：<code>neutron vpn-ipsecpolicy-delete IPSEC-POLICY-ID</code>|<ul><li>UI:<ol><li>ipsec-policy删除成功。</li></ol></li><li>CLI:<ol><li>ipsec-policy删除成功。||若ipsec-policy绑定到了ipsec站点需要解除绑定才能删除成功|||
|01010811|删除VPN服务|<ul><li>UI:<ol><li>登录dashboard，点击【Project】选项，点击【network】子选项；</li><li>点击【VPN】选项，点击VPN服务选中需要删除的VPN服务点击删除VPN服务按钮。</li></ol></li><li>CLI:<ol><li>登录到controller节点上；</li><li>执行命令：<code>neutron vpn-service-delete VPN-SERVICE-ID</code>|<ul><li>UI:<ol><li>vpn服务删除成功。</li></ol></li><li>CLI:<ol><li>vpn服务删除成功。||若VPN服务绑定到了ipsec站点需要解除绑定才能删除成功|||
|01010812|删除IPSec站点连接|<ul><li>UI:<ol><li>登录dashboard，点击【Project】选项，点击【network】子选项；</li><li>点击【VPN】选项，点击IPSec站点连接选中选中需要删除的IPSec站点，点击删除IPSec站点连接。</li></ol></li><li>CLI:<ol><li>登录到controller节点上；</li><li>执行命令：<code>neutron ipsec-site-connection-delete IPSEC_SITE_CONNECTION_ID</code>。|<ul><li>UI:<ol><li>ipsec站点删除成功。</li></ol></li><li>CLI:<ol><li>ipsec站点删除成功。|||||
|01010813|验证VPN|<ul><li>UI:<ol><li>登录dashboard，点击【Project】选项，点击【Compute】子选项；</li><li>点击【实例】选项，选择做了VPN服务的两台实例，点击进入详情界面，启动云主机控制台；</li><li>这两台不在一个网段的两台实例能够成功ping通即验证成功</li></ol></li><li>CLI:<ol><li>|在两个不同子网网段的实例能够成功ping通|||||















