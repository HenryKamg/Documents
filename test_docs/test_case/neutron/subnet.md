# 验证 Neutron 的 subnet 部分

|内容编号|内容名称|
|--------|--------|
|03|子网|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01010301|创建并列出子网|<ul><li>UI:<ol><li>登录dashboard，点击 【Project】 选项，选择 【Network】 子选项；</li><li>点击 【Networks】 选项，在右侧选择要创建子网的网络，点击该网络的 Name 进入页面；</li><li>在 Subnet 处点击 【Create Subnet】 按钮；</li><li>在弹出的 【Create Subnet】 窗口的 Subnet 标签中，填写子网名称 "subnet1"，网络地址选择内网地址 "172.168.200.0/22"，IP版本 "IPv4"，网关IP "172.168.200.1"，点击 【Next】 按钮；</li><li>切换到 Subnet Detail 中，勾选 "Enable DHCP"，Allocation Pools 中填写 "172.168.200.2,172.168.200.100"，点击 【Create】 按钮。</li></ol></li><li>CLI:<ol><li>登录rally测试服务器；</li><li>使用rally测试文档create_and_list_subnets.yaml；</li><li>执行测试命令```rally task start create_and_list_subnets.yaml```。</li></ol></li></ul>|<ul><li>UI:<ul><li>能够成功创建子网并能够在网络下看到子网列表。</li></ul></li><li>CLI:<ul><li>rally测试成功</li></ul></li></ul>|||Rally:</br>create_and_list_subnets.yaml|
|01010302|创建 IPv6 子网||||||
|01010303|创建包含错误网关的子网||||||
|01010304|创建没有网关的子网||||||
|01010305|为同一个网络创建多个子网||||||
|01010306|为同一个网络创建同一段地址的子网||||||
|01010307|测试子网的删除|<ul><li>UI:<ol><li>登录dashboard，点击 【Project】 选项，点击 【Network】 子选项；</li><li>点击 【Networks】 子选项，在右侧列表中选择要删除子网的网络，点击网络的 Name 进入页面；</li><li>选择要删除的子网，在选项框中勾选，点击右上方 【Delete Subnet】 按钮；</li><li>在弹出的 【Confirm Delete Subnets】 窗口中，点击 【Delete Subnet】 按钮，确认删除。</li></ol></li><li>CLI:<ol><li>登录rally测试服务器</li><li>使用rally测试文档create_and_delete_subnets.yaml；</li><li>执行测试命名```rally task start create_and_delete_subnets.yaml```。</li></ol></li></ul>|</li><li>UI:<ul><li>能够成功删除子网，列表中不再显示该子网的信息</li></ul></li><li>CLI:<ul><li>rally 测试成功</li></ul></li></ul>|||Rally:</br>create_and_delete_subnets.yaml|
|01010308|测试 neutron subnet-update 命令的功能|<ul><li>UI:<ol><li>登录dashboard，点击 【Project】 选项，点击 【Network】 子选项；</li><li>点击 【Networks】 子选项，在右侧列表中选择要修改子网的网络，点击网络的 Name 进入页面；</li><li>选择要修改的子网 "subnet1"，点击 【Actions】 中的 【Edit Subnet】；</li><li>在弹出的 【Edit Subnet】 窗口的 Subnet 标签中，修改子网的名称 Subnet Name 为 "subnet2"，修改网关为 "..."，点击 【Next】 按钮；</li><li>在 Subnet Detail 标签中，点击下方的 【Save】 按钮。</li></ol></li><li>CLI:<ol><li>登录rally测试服务器；</li><li>使用rally测试文档create_and_update_subnets.yaml；</li><li>执行测试命令```rally task start create_and_update_subnets.yaml```。</li></ol></li></ul>|<ul><li>UI:<ul><li>能够成功的编辑修改子网。</li></ul></li><li>CLI:<ul><li>rally测试成功</li></ul></li></ul>||创建子网后，修改子网|Rally:</br>create_and_update_subnets.yaml|
