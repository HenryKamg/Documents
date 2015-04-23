# 验证 Neutron 的 network 部分

|内容编号|内容名称|
|--------|--------|
|01|网络|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01070101|测试 neutron net-list 命令的性能|<ul><li>UI:</li></ul><ol><li>登录到 dashboard；</li><li>点击左侧导航栏的 Project，展开选项卡；</li><li>点击 Network 子选项卡，展开；</li><li>点击Network。</li></ol><ul><li>CLI:</li></ul><ol><li>登录到rally测试服务器；</li><li>使用rally测试文件create_and_list_networks.json；</li><li>执行测试命名```rally task start create_and_list_networks.json```。|<ul><li>UI:</li></ul><ol><li>显示该Project中所有已经创建的网络||创建并列出网络，需要指定参数|Rally:</br>create_and_list_networks.json|
|01070102|测试 neutron net-create 和 neutron net-delete 命令的性能|<ul><li>UI:</li></ul><ol><li>登录到dashboard；</li><li>点击左侧导航栏Project，展开选项卡；</li><li>点击Network子选项卡点，展开，点击Network。</li><li>进入页面右上方有network-create和network-delete两个选项。</li><li>测试neutron net-create选择network-create，填写网络名称“network1”，创建子网填写信息，根据需求填写网络地址，子网详情，激活DHCP，填写地址池，最后点击已创建完成network-create；</li><li>测试neutron net-delete，选中要删除的网络打钩，点击右上方删除网络按钮</li></ol><ul><li>CLI:</li></ul><ol><li>登录到rally测试服务器；</li><li>使用rally测试文件create_and_delete_networks.json；</li><li>执行测试命```rally task start create_and_delete_networks.json```。|<ul><li>UI:</li></ul><ol><li>能够成功创建网络，也能够成功删除网络||创建网络后，将其删除|Rally:</br>create_and_delete_networks.json|
|01070103|测试 neutron net-create 和 neutron net-update 命令的性能|<ul><li>UI:</li></ul><ol><li>登录到dashboard,点击左侧导航栏的Project展开选项卡，点击Network子选项卡，展开，再点击Network进入网络界面；</li><li>测试neutron net-create选择network-create，填写网络名称“network1”，创建子网填写信息，根据需求填写网络地址，子网详情，激活DHCP，填写地址池，点击已创建完成network-create；</li><li>测试neutron net-update，选择要修改的网络点击进入即可进入对子网和端口进行修改更新。</li></ol><ul><li>CLI:</li></ul><ol><li>登录到rally测试服务；</li><li>使用rally测试文件 create_and_update_networks.json；</li><li>执行测试命令```rally task start create_and_update_networks.json```；|<ul><li>UI:</li></ul><ol><li>能够成功创建网络以及对网络的更新||创建网络后，修改网络|Rally:</br>create_and_update_networks.json|

