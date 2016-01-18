# 验证 keystone 角色

|内容编号|内容名称|
|--------|--------|
|03|角色|

|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01050301|测试用户角色的创建和删除|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>keystone role-create --name NAME</code>，创建角色。</li></ol></li>Rally:<ol><li>登录到 rally 测试服务器；</li><li>使用 rally 测试文件 create_and_delete_role.yaml；</li><li>执行测试命令 <code>rally task start create_and_delete_role.yaml</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>角色创建成功，显示角色创建的 id 和名称等信息</li></ul></li><li>Rally:<ul><li>Rally 测试成功</li></ul></li></ul>||执行 100 次，并行任务数为 10|Rally:</br>create_and_delete_role.yaml|
|01050302|测试用户角色的创建、添加并列出|<ul><li>CLI:<ol><li>登录到 Controller 节点；</li><li>执行命令 <code>keystone role-create --name NAME</code>，创建角色；</li><li>执行命令 <code>keystone user-role-add --user USER_NAME --role ROLE_NAME --tenant TENANT_NAME</code>，其中的各个参数，可以替换为 ID；</li><li>执行命令 <code>keystone user-role-list --user USER_NAME</code> 列出该用户的角色列表。</li></ol></li>Rally:<ol><li>登录到 rally 测试服务器；</li><li>使用 rally 测试文件 create_add_and_list_user_roles.yaml；</li><li>执行测试命令 <code>rally task start create_add_and_list_user_roles.yaml</code>。</li></ol></li></ul>|<ul><li>CLI:<ul><li>角色创建成功</li><li>为用户添加角色后，列出该用户的角色列表，可以看到新添加的用户角色显示在列表中</li></ul></li><li>Rally:<ul><li>Rally 测试成功</li></ul></li></ul>||执行 100 次，并行任务数为 10|Rally:</br>create_add_and_list_user_roles.yaml|
|01050303|测试为用户分配角色和删除|<ul><li>UI:<ol><li>以 admin 身份登录到 Dashboard；</li><li>点击左侧导航栏的 【【Identity】，展开选项卡；</li><li>点击 【Projects】 选项；</li><li>在右侧的租户列表中，选择一个租户，点击 【Actions】 中的 【Modify Users】；</li><li>在弹出的 【Edit Project】 对话框中，点击 【Project Members】 标签，点击右侧用户中的下拉按扭，对该租户的用户进行角色分配，点击对话框右下角的 【Save】 按扭，完成分配；</li><li>如果点击下拉列表后，将列表中所勾选的角色取消勾选，则删除该用户在该租户中的角色。</li></ol></li>Rally:<ol><li>登录到 rally 测试服务器；</li><li>使用 rally 测试文件 add_and_remove_user_role.yaml；</li><li>执行测试命令 <code>rally task start add_and_remove_user_role.yaml</code>。</li></ol></li></ul>|<ul><li>UI:<ul><li>成功为用户分配角色，用户拥有所分配的新角色</li><li>取消勾选后，用户不再具有该角色</li></ul></li><li>Rally:<ul><li>Rally 测试成功</li></ul></li></ul>||执行 100 次，并行任务数为 10|Rally:</br>add_and_remove_user_role.yaml|
