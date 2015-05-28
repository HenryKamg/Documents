# FWaaS
|内容编号|内容名称|
|--------|--------|
|05|FWaaS|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01010501|创建防火墙规则|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击 【Networks】 选项，点击【firewall】子选项，进入防火墙配置界面，点击【防火墙规则】按钮进入；</li><li>进入防火墙规则创建界面，点击添加规则按钮弹出添加规则窗口；</li><li>填写防火墙名称“firewall-rule”，协议类型“TCP”，动作“允许”，目的端口“80”。</li></ol></li><li>CLI:<ol><li>登录到controller节点；</li><li>执行命令<code>neutron firewall-rule-create --protocol tcp --destination-port 80 --action allow</code>|||协议类型以及端口号可以根据需求选择|||
|01010502|创建防火墙策略|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击 【Networks】 选项，点击【firewall】子选项，进入防火墙配置界面，点击【防火墙策略】按钮进入；</li><li>进入防火墙策略创建界面，点击增加策略按钮弹出增加策略窗口；</li><li>名称填写“firewall-policy”，点击规则按钮，将创建好的规则在可规则栏拖入选定规则栏，点击添加按钮，策略创建成功。</li></ol></li><li>CLI:<ol><li>登录到controller节点上</li><li>执行命令：<code>neutron firewall-policy-create --firewall-rules "FIREWALL-RULE-ID" policy1</code>||||||
|01010503|创建防火墙|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击 【Networks】 选项，点击【firewall】子选项，进入防火墙配置界面，点击【防火墙】按钮进入；</li><li>进入防火墙创建界面，点击创建防火墙按钮弹出添加防火墙窗口；</li><li>名称填写“firewall”，策略在下拉菜单中选择一个可用策略，点击添加按钮，防火墙创建成功。</li></ol></li><li>CLI:<ol><li>登录到controller节点</li><li>执行命令<code>neutron firewall-create POLICY-ID</code>||||||
|01010504|删除防火墙|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击 【Networks】 选项，点击【firewall】子选项，进入防火墙配置界面，点击【防火墙】按钮进入；</li><li>选中需要删除的防火墙，点击按钮删除防火墙将防火墙删除。</li></ol></li><li>CLI:<ol><li>登录到controller节点上；</li><li>执行命令：<code>neutron firewall-delete FIREWALL-ID</code>||||||
|01010505|删除防火墙策略|<ul><li>UI:<ol><li>登录dashboard，点击【Project】 选项，选择【Network】子选项；</li><li>点击 【Networks】 选项，点击【firewall】子选项，进入防火墙配置界面，点击【防火墙策略】按钮进入；</li><li>选中需要删除的防火墙策略，点击按钮删除策略将策略删除。</li></ol></li><li>CLI:<ol><li>登录到controller节点上；</li><li>执行命令：<code>neutron firewall-policy-delete FIREWALL-POLICY-ID</code>||||||
|01010506|删除防火墙规则|</li><li>点击 【Networks】 选项，点击【firewall】子选项，进入防火墙配置界面，点击【防火墙规则】按钮进入；</li><li>选中需要删除的防火墙规则，点击按钮删除归贼将规则删除。</li></ol></li><li>CLI:<ol><li>登录到controller节点上；</li><li>执行命令：<code>neutron firewall-rule-delete FIREWALL-RULE-ID</code>||||||


