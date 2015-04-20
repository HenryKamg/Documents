# 验证 Nova 的 keypair 部分

|内容编号|内容名称|
|--------|--------|
|01|keypair|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01080101|(以随机名称)创建并列出 keypair|<ul><li>UI:<ol><li>登录到 dashboard；</li><li>点击左侧导航栏的 【Project】，展开选项卡；</li><li>点击 【Compute】 子选项卡，展开；</li><li>点击 【Access & Security】 选项；</li><li>点击右侧的 【Key Pairs】 标签；</li><li>点击 【Create Key Pair】 按钮，在弹出的 【Create Key Pair】 窗口中，填写 Key Pair Name，点击 【Create Key Pair】 按钮。</li></ol></li><li>CLI:<ol><li>登录到 rally 测试服务器；</li><li>使用 rally 测试文件 create-and-list-keypairs.json；</li><li>执行测试命令 <code>rally task start create-and-list-keypairs.json</code> 。</li></ol></li></ul>|<ul><li>UI:<ul><li>Key Pair 创建成功，提示下载</li><li>可以选择"取消"，也可以下载到本地某个目录下，保存</li></ul></li><li>CLI:<ul><li>Rally 测试成功</li></ul></li></ul>|||Rally:</br>create-and-list-keypairs.json|
|01080102|(以随机名称)创建 keypair 后，将其删除|<ul><li>UI:<ol><li>登录到 dashboard；</li><li>点击左侧导航栏的 【Project】，展开选项卡；</li><li>点击 【Compute】 子选项卡，展开；</li><li>点击 【Access & Security】 选项；</li><li>点击右侧的 【Key Pairs】 标签；</li><li>点击 【Create Key Pair】 按钮，在弹出的 【Create Key Pair】 窗口中，填写 Key Pair Name，点击 【Create Key Pair】 按钮；</li><li>创建成功后，不保存 Key Pair，再次点击 【Access & Security】 选项卡；</li><li>在右侧显示的 Key Pair 列表中，选择所创建的 Key Pair，点击 【Actions】 中的 【Delete Key Pair】 按钮</li><li>在弹出的 【Confirm Delete Key Pair】 窗口中，点击 【Delete Key Pair】 按钮。</li></ol></li><li>CLI:<ol><li>登录到 rally 测试服务器；</li><li>使用 rally 测试文件 create-and-delete-keypair.json；</li><li>执行测试命令 <code>rally task start create-and-delete-keypair.json</code> 。</li></ol></li></ul>|<ul><li>UI:<ul><li>Key Pair 创建后，成功删除；</li></ul></li><li>CLI:<ul><li>Rally 测试成功</li></ul></li></ul>|||Rally:</br>create-and-delete-keypair.json|
