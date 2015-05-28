# LBaaS
|内容编号|内容名称|
|--------|--------|
|06|LWaaS|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01010601|创建资源池|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击 【Networks】 选项，点击【负载均衡】子选项，进入负载均衡配置界面；</li><li>点击资源池按钮创建一个新的资源池，点击资源池，弹出新增资源池对话框；</li><li>名称填写“lb-pool”，提供者使用默认着“haproxy”，子网选择一个你需要去负载均衡的子网网段，协议“TCP”，负载均衡方式“ROUND——ROBIN”，点击添加按钮资源池创建成功。</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令：<code>neutron lb-pool-create --lb-method ROUND_ROBIN --name pool2 --protocol TCP --subnet-id SUBNET-ID</code>|||协议类型可以根据需求选择|||
|01010602|创建VIP|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击 【Networks】 选项，点击【负载均衡】子选项，进入负载均衡配置界面；</li><li>点击资源池按钮，选择需要添加VIP的资源池，点击下拉菜单点击添加VIP；</li><li>名称填写“lb-vip”，选择负载均衡中子网中一个可用IP填写到“从选定的子网中指定一个可用的IP地址”，协议端口“22”，点击添加按钮，VIP创建成功。</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令：<code> neutron lb-vip-create --name vip2 --protocol-port 22 --protocol TCP --subnet-id SUBNET-ID POOL-ID</code>|||端口号根据协议类型以及需求选择|||
|01010603|创建资源池成员|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击 【Networks】 选项，点击【负载均衡】子选项，进入负载均衡配置界面；</li><li>点击成员按钮，创建成员，点击新增成员按钮；</li><li>选择一个可用资源池，成员来源选择需要去担任负载工作的实例，协议端口填“22”，点击添加按钮成功添加一个组成员到资源池中。</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令：<code>neutron lb-member-create --address 192.168.202.6 --protocol-port 22 POOL-ID</code>|||端口号根据协议类型以及需求选择，获取主机IP可以执行命令<code>nova list</code>获取到|||
|01010604|创建监控|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击 【Networks】 选项，点击【负载均衡】子选项，进入负载均衡配置界面；</li><li>点击监控按钮，创建监控，点击新增监控弹出新增监控对话框；</li><li>类型选择“PING”，延迟“1”，超时“1”，最大重试次数“2”，点击添加按钮，监控创建成功；</li><li>将监控与资源池绑定，点击资源池按钮，选定需要绑定监控的资源池，点击下拉菜单；</li><li>选择关联监控，弹出关联监控对话框，选择需要绑定的监控，点击关联。</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令创建监控：<code>neutron lb-healthmonitor-create --delay 3 --type PING --max-retries 3 --timeout 3</code></li><li>执行命令将监控与资源池绑定：<code>neutron lb-healthmonitor-associate LB-HEALTHMONITOR-ID POOL-ID</code>|||延迟、时延、最大重试次数根据实际可行情况填写|||
|01010605|删除资源池|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击 【Networks】 选项，点击【负载均衡】子选项，进入负载均衡配置界面；</li><li>点击资源池，选择要删除的资源池，点击删除资源池按钮删除资源池；。</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令删除资源池：<code>neutron lb-pool-delete LB-POOL-ID</code>||||||
|01010606|删除资源池成员|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击 【Networks】 选项，点击【负载均衡】子选项，进入负载均衡配置界面；</li><li>点击成员按钮，选中要删除的成员，点击删除成员，删除成员成功。</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令删除资源池成员：<code>neutron lb-member-delete LB-MEMBER-DELETE</code>||||||
|01010606|删除监控|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击 【Networks】 选项，点击【负载均衡】子选项，进入负载均衡配置界面；</li><li>点击监控按钮，进入监控界面，选定需要删除的监控，点击按钮删除监控，删除监控成功。</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令删除监控：<code>neutron lb-healthmonitor-delete LB-HEALTHMONITOR-ID</code>|||若监控已经与资源池绑定则只有在资源池被删除或与资源池解除绑后才能成功删除|||
















