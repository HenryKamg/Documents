# VPNaaS
|内容编号|内容名称|
|--------|--------|
|07|VPNaaS|

|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01010701|创建ike-policy|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击 【Networks】 选项，点击【VPN】子选项，进入VPN配置界面；</li><li>点击IKE策略选项，点击添加IKE策略，弹出添加IKE策略对话框；</li><li>填写名称“my-ikepolicy”，点击添加；</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令添加ike-policy：<code>neutron vpn-ikepolicy-create my-ikepolicy</code>|||算法在没有特殊要下选择默认即可|||
|01010702|创建ipsec-policy|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击 【Networks】 选项，点击【VPN】子选项，进入VPN配置界面；</li><li>点击IPSec策略选项，点击添加IPSec策略，弹出添加IPSec策略对话框；</li><li>名称填写“my-ipsecpolicy”，点击添加按钮；</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令添加ipsec-policy：<code>neutron vpn-ipsecpolicy-create my-ipsecpolicy</code>|||算法在没有特殊要下选择默认即可|||
|01010703|创建VPN服务|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击 【Networks】 选项，点击【VPN】子选项，进入VPN配置界面；</li><li>点击VPN服务选项，点击添加VPN服务，弹出添加VPN服务对话框；</li><li>名称填写“my-vpnserviceA”，路由选择需要建立VPN服务的实例连接外网的路由器，子网选择实例所在的子网网段，点击添加。</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令，创建一端的VPN服务：<code>neutron vpn-service-create --name my-vpnserviceA router2 sub_net2Created a new vpnservice</code>|||VPN服务要创建在两个需要使用VPN连接的实例上，此处只列举了一个实例上的服务配置，另一个命令相同|||
|01010704|创建ipsec站点连接|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击 【Networks】 选项，点击【VPN】子选项，进入VPN配置界面；</li><li>点击IPSec站点连接选项，点击添加IPSec站点连接弹出添加IPSec站点连接对话框；</li><li>名称填写“my-connectionA”，VPN服务选择好的用于此连接的服务，选择可用的IKE策略，选择可用的IPSec策略；</li><li>伙伴网关公共IPV4填写“对端建立VPN路由的外网”，伙伴ID填写“对端路由器ID”，PSK填写“abc123”,点击添加。</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令，创建一端的IPSec站点连：<code>neutron ipsec-site-connection-create --name my-connectionA --vpnservice-id VPNSERVICE-ID --ikepolicy-id IKEPOLICY-ID --ipsecpolicy-id IPSECPOLICY-ID --peer-address 25.0.0.130 --peer-id 25.0.0.130 --peer-cidr 192.168.201.0/24 --psk abc123</code>|||站点的创建是双向，此处只列出了一端的连接|||














