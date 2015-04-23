# 验证 Neutron 的 router 部分

|内容编号|内容名称|
|--------|--------|
|03|路由|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01070301|创建并列出路由|<ul><li>UI:</li></ul><ol><li>登录dashboard，点击右上方的Project，展开选项，点击Network子选项，再选择路由子选项，进入路由界面；</li><li>点击创建路由选项取名字为“router1”，点击创建路由即创建路由成功。在路由表项中可以看到全部的路由条目</li></ol><ul><li>CLI:</li></ul><ol><li>登录rally测试服务；</li><li>使用rally测试文档create_and_list_routers.json；</li><li>执行测命令```rally task start create_and_list_routers.json```。|</li><li>UI:能够成功创建路由，在路由表项中查看到全部路由。</li><li>CLI:rally测试成功。|||Rally:</br>create_and_list_routers.json|
|01070302|创建路由后，将其删除|<ul><li>UI:</li></ul><ol><li>登录dashboard，点击右上方的Project，展开选项，点击Network子选项，再选择路由子选项，进入路由界面；</li><li>点击要删除的路由打钩选中，再选右上角删除路由选项。</li></ol><ul><li>CLI:</li></ul><ol><li>登录rally测试服务器；</li><li>使用rally测试文档create_and_delete_routers.json；</li><li>执行测试命令```rally task start create_and_list_routers.json```。|</li><li>UI:能够成功删除路由；</li><li>CLI:rally测试成功。|||Rally:</br>create_and_delete_routers.json|
|01070303|创建路由后，修改路由|<ul><li>UI:</li></ul><ol><li>登录dashboard，点击右上方的Project，展开选项，点击Network子选项，再选择路由子选项，进入路由界面；</li><li>选择要修改的路由点击进入，即可对路内的接口进行修改。</li></ol><ul><li>CLI:</li></ul><ol><li>登录rally测试服务器；</li><li>使用rally测试文档create_and_update_routers.json；</li><li>执行测试命令```rally task start create_and_update_routers.json```|</li></ol>UI:能够对路由的接口修改成功。</li></ol>CLI:rally测试成功。|||Rally:</br>create_and_update_routers.json|
