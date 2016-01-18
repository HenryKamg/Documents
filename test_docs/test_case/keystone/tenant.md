# 验证 Keystone 的 tenant 部分

|内容编号|内容名称|
|--------|--------|
|04|租户|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01050401|创建 tenant|<ul><li>UI:<ol><li>登录到 dashboard；</li><li>点击左侧导航栏的 【Identity】，展开选项卡；</li><li>点击 【Projects】 选项，点击右侧的 【Create Project】 按钮；</li><li>在弹出的 【Create Project】 窗口中，在 【Project Infomation】 标签下填写 Name，其他保持默认配置，点击窗口下方的 【Create Project】。</li></ol></li><li>CLI:<ol><li>登录到 Rally 测试服务器；</li><li>使用测试文件 create-tenant.yaml；</li><li>执行测试命令 <code>rally task start create-tenant.yaml</code>。</li></ol></li></ul>|<ul><li>UI:<ul><li>Project 创建成功</li></ul></li><li>CLI:<ul><li>Rally 测试成功</li></ul></li></ul>||<ul><li>设置名称长度为 10</li><li>执行 100 次，每次并行执行 10 个测试</li></ul>|Rally:</br>create-tenant.yaml|
|01050402|列出 tenant|<ul><li>UI:<ol><li>登录到 dashboard；</li><li>点击左侧导航栏的 【Identity】，展开选项卡；</li><li>点击 【Projects】 选项。</li></ol></li><li>CLI:<ol><li>登录到 Rally 测试服务器；</li><li>使用测试文件 create-and-list-tenants.yaml；</li><li>执行测试命令 <code>rally task start create-and-list-tenants.yaml</code>。</li></ol></li></ul>|<ul><li>UI:<ul><li>界面上能够显示所有的 tenant</li></ul></li><li>CLI:<ul><li>Rally 测试成功</li></ul></li></ul>||<ul><li>设置名称长度为 10</li><li>执行 10 次，每次执行 1 个测试</li></ul>|Rally:</br>create-and-list-tenants.yaml|
|01050403|使用普通用户列出 tenant|<ul><li>UI:<ol><li>以普通用户登录到 dashboard；</li><li>点击左侧导航栏的 【Identity】，展开选项卡；</li><li>点击 【Projects】 选项。</li></ol></li><li>CLI:<ol><li>登录到 Controller 节点；</li><li>使用 OpenStack 普通用户执行命令 <code>keystone tenant-list</code>。</li></ol></li></ul>|<ul><li>UI:<ul><li>无法列出，跳转到错误页面</li><li>提示信息为："You do not have permission to access the resource:/dashboard/identity/"</li></ul></li><li>CLI:<ul><li>命令执行失败</li><li>提示错误信息："You are not authorized to perform the requested action: admin_required (HTTP 403)"</li></ul></li></ul>|||None|
|01050404|创建 tenant 并分配一些用户|<ul><li>UI:<ol><li>登录到 dashboard；</li><li>点击左侧导航栏的 【Identity】，展开选项卡；</li><li>点击 【Projects】 选项，点击右侧的 【Create Project】 按钮；</li><li>在弹出的 【Create Project】 窗口中，在 【Project Infomation】 标签下填写 Name；</li><li>切换到 【Project Members】 标签，选择分配给该项目的用户，点击用户后的 【+】 图标；</li><li>点击窗口下方的 【Create Project】 按钮。</li></ol></li><li>CLI:<ol><li>登录到 Rally 测试服务器；</li><li>使用测试文件 create-tenant-with-users.yaml；</li><li>执行测试命令 <code>rally task start create-tenant-with-users.yaml</code>。</li></ol></li></ul>|<ul><li>UI:<ul><li>Project 创建成功，该 project 中包含所选择的用户</li></ul></li><li>CLI:<ul><li>Rally 测试成功</li></ul></li></ul>||<ul><li>设置 tenant 和 user 的名称长度为 10</li><li>执行 10 次，每次并行执行 10 个测试</li></ul>|Rally:</br>create-tenant-with-users.yaml|

