# 验证 Nova 的 Security Group 部分

|内容编号|内容名称|
|--------|--------|
|01|Security Group|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01080101|创建并列出 Security Group|<ul><li>UI:<ol><li>登录到 dashboard；</li><li>点击左侧导航栏的 【Project】，展开选项卡；</li><li>点击 【Compute】 子选项卡，展开；</li><li>点击 【Access & Security】 选项卡；</li><li>点击 【Create Security Group】 按钮，在弹出的 【Create Security Group】 对话框中填写 Name，并填写 Description；</li><li>点击对话框下方的 【Create Security Group】 按钮。</li></ol></li><li>CLI:<ol><li>登录到 rally 测试服务器；</li><li>使用 rally 测试文件 create-and-list-Security Groups.json；</li><li>执行测试命令 <code>rally task start create-and-list-Security Groups.json</code> 。</li></ol></li></ul>|<ul><li>UI:<ul><li>Security Group 创建成功，有 Success 的提示</li><li>列表中显示新建的 Security Group 的信息</li></ul></li><li>CLI:<ul><li>Rally 测试成功</li></ul></li></ul>||rules_per_security_group 参数只能指定 rules 的数量|Rally:</br>create-and-list-Security Groups.json|
|01080102|测试 Security Group 的删除|<ul><li>UI:<ol><li>登录到 dashboard；</li><li>点击左侧导航栏的 【Project】，展开选项卡；</li><li>点击 【Compute】 子选项卡，展开；</li><li>点击 【Access & Security】 选项卡；</li><li>在右侧列表中，选择一个 Security Group，点击 【Actions】 中的 【Delete Security Group】；</li><li>在弹出的 【Confirm Delete Security Group】 对话框中，点击下方的 【Delete Security Group】。</li></ol></li><li>CLI:<ol><li>登录到 rally 测试服务器；</li><li>使用 rally 测试文件 create-and-delete-Security Groups.json；</li><li>执行测试命令 <code>rally task start create-and-delete-Security Groups.json</code> 。</li></ol></li></ul>|<ul><li>UI:<ul><li>Security Group 创建成功，有 Success 的提示</li><li>列表中显示新建的 Security Group 的信息</li><li>删除 Security Group 成功，删除后列表中不再显示所删除的 Security Group 的信息</li></ul></li><li>CLI:<ul><li>Rally 测试成功</li></ul></li></ul>|||Rally:</br>create-and-delete-Security Groups.json|
