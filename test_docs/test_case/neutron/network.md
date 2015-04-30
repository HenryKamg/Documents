# 验证 Neutron 的 network 部分

|内容编号|内容名称|
|--------|--------|
|01|网络|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01070101|测试 neutron net-list 命令的功能|<ul><li>UI:<ol><li>登录到 dashboard；</li><li>点击左侧导航栏的 【Project】，展开选项卡；</li><li>点击 【Network】 子选项卡，展开；</li><li>点击 【Networks】。</li></ol></li><li>CLI:<ol><li>登录到rally测试服务器；</li><li>使用rally测试文件create_and_list_networks.yaml；</li><li>执行测试命名```rally task start create_and_list_networks.yaml```。</li></ol></li></ul>|<ul><li>UI:<ul><li>显示该Project中所有已经创建的网络</li></ul></li><li>CLI:<ul><li>Rally 测试成功</li></ul></li></ul>||创建并列出网络，需要指定参数|Rally:</br>create_and_list_networks.yaml|
|01070102|创建不包含子网的网络。测试 neutron net-create 命令的功能|<ul><li>UI:<ol><li>登录到dashboard；</li><li>点击左侧导航栏 【Project】，展开选项卡；</li><li>点击 【Network】 子选项卡点，展开，点击 【Networks】。</li><li>在右侧点击 【Create Network】 按钮，在弹出的 【Create Network】 窗口中的 Network 标签下，填写 Network Name，点击 【Next】 按钮；</li><li>窗口切换到 Subnet 标签，取消勾选 Create Subnet，不创建子网，点击 【Next】 按钮；</li><li>窗口切换到 Subnet Detail 标签，取消勾选 Enable DHCP，点击 【Create】 按钮。</li></ol></li><li>CLI:<ol><li>登录到rally测试服务器；</li><li>使用rally测试文件create_and_list_networks.yaml；</li><li>执行测试命令```rally task start create_and_list_networks.yaml```。</li></ol></li></ul>|<ul><li>UI:<ul><li>能够成功创建网络，也能够成功删除网络</li></ul></li><li>CLI:<ul><li>Rally 测试成功</li></ul></li></ul>||创建网络后，将其删除|Rally:</br>create_and_list_networks.yaml|
||测试 neutron net-delete 命令的功能|<ul><li>UI:<ol><li>登录到 dashboard；</li><li>点击左侧导航栏 【Project】，展开选项卡；</li><li>点击 【Network】 子选项卡点，展开，点击 【Networks】。</li><li>在右侧选择要删除的网络，点击 【Actions】 中的 【Delete Network】；</li><li>在弹出的 【Confirm Delete Network】 窗口中，点击窗口下方的 【Delete Network】 按钮。</li></ol></li><li>CLI:<ol><li>登录到 Rally 测试服务器；</li><li>使用测试文件 create_and_delete_networks.yaml；</li><li>执行测试命令 <code>rally task start create_and_delete_networks.yaml</code>。</li></ol></li></ul>|<ul><li>UI:<ul><li>网络删除成功，界面上不再显示该网络的信息</li></ul></li><li>CLI:<ul><li>Rally 测试成功</li></ul></li></ul>|||Rally:</br>create_and_delete_networks.yaml|
|01070103|测试 neutron net-update 命令的功能|<ul><li>UI:<ol><li>登录到dashboard，点击左侧导航栏的 【Project】 展开选项卡，点击 【Network】 子选项卡，展开；</li><li>点击 【Networks】 进入网络界面；</li><li>选择一个网络，点击 【Actions】 中的 【Edit Network】；</li><li>在弹出的 【Edit Network】 窗口中，可以修改 Name，选择 Admin State 为 Down，点击窗口下方的 【Save Changes】。</li></ol></li><li>CLI:<ol><li>登录到rally测试服务；</li><li>使用rally测试文件 create_and_update_networks.yaml；</li><li>执行测试命令```rally task start create_and_update_networks.yaml```。</li></ol></li></ul>|<ul><li>UI:<ul><li>网络修改成功，Admin State 显示的状态为 DOWN</li></ul></li><li>CLI:<ul><li>Rally 测试成功</li></ul></li></ul>||创建网络后，修改网络|Rally:</br>create_and_update_networks.yaml|

