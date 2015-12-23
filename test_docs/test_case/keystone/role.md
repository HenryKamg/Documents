# 验证 keystone 角色

|内容编号|内容名称|
|--------|--------|
|04|角色|

|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
||测试用户角色的创建和删除|<ul><li>UI:?<ol><li>TODO</li></ol></li>Rally:<ol><li>登录到 rally 测试服务器；</li><li>使用 rally 测试文件 create_and_delete_role.yaml；</li><li>执行测试命令 <code>rally task start create_and_delete_role.yaml</code>。</li></ol></li></ul>|<ul><li>UI:<ul><li>TODO</li></ul></li><li>Rally:<ul><li>Rally 测试成功</li></ul></li></ul>||执行 100 次，并行任务数为 10|Rally:</br>create_and_delete_role.yaml|
||测试用户角色的创建、添加并列出|<ul><li>UI:?<ol><li>TODO</li></ol></li>Rally:<ol><li>登录到 rally 测试服务器；</li><li>使用 rally 测试文件 create_add_and_list_user_roles.yaml；</li><li>执行测试命令 <code>rally task start create_add_and_list_user_roles.yaml</code>。</li></ol></li></ul>|<ul><li>UI:<ul><li>TODO</li></ul></li><li>Rally:<ul><li>Rally 测试成功</li></ul></li></ul>||执行 100 次，并行任务数为 10|Rally:</br>create_add_and_list_user_roles.yaml|
||测试为用户分配角色和删除|<ul><li>UI:?<ol><li>TODO</li></ol></li>Rally:<ol><li>登录到 rally 测试服务器；</li><li>使用 rally 测试文件 add_and_remove_user_role.yaml；</li><li>执行测试命令 <code>rally task start add_and_remove_user_role.yaml</code>。</li></ol></li></ul>|<ul><li>UI:<ul><li>TODO</li></ul></li><li>Rally:<ul><li>Rally 测试成功</li></ul></li></ul>||执行 100 次，并行任务数为 10|Rally:</br>add_and_remove_user_role.yaml|
