# 验证 Nova 的 keypair 部分

|内容编号|内容名称|
|--------|--------|
|02|密钥对|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01060201|创建并列出 keypair|<ul><li>UI:<ol><li>登录到 dashboard；</li><li>点击左侧导航栏的 【Project】，展开选项卡；</li><li>点击 【Compute】 子选项卡，展开；</li><li>点击 【Access & Security】 选项；</li><li>点击右侧的 【Key Pairs】 标签；</li><li>点击 【Create Key Pair】 按钮，在弹出的 【Create Key Pair】 窗口中，填写 Key Pair Name，点击 【Create Key Pair】 按钮。</li></ol></li><li>CLI:<ol><li>登录到 rally 测试服务器；</li><li>使用 rally 测试文件 create-and-list-keypairs.yaml；</li><li>执行测试命令 <code>rally task start create-and-list-keypairs.yaml</code> 。</li></ol></li></ul>|<ul><li>UI:<ul><li>Key Pair 创建成功，提示下载</li><li>可以选择"取消"，也可以下载到本地某个目录下，保存</li></ul></li><li>CLI:<ul><li>Rally 测试成功</li></ul></li></ul>||<ul><li>执行 10 次，每次并行执行 2 个测试</li><li>每次创建 3 个 tenant，每个 tenant 包含 2 个 user</li></ul>|Rally:</br>create-and-list-keypairs.yaml|
|01060202|测试 keypair 的删除|<ul><li>UI:<ol><li>登录到 dashboard；</li><li>点击左侧导航栏的 【Project】，展开选项卡；</li><li>点击 【Compute】 子选项卡，展开；</li><li>点击 【Access & Security】 选项；</li><li>点击右侧的 【Key Pairs】 标签；</li><li>在右侧显示的 Key Pair 列表中，选择一个 Key Pair，点击 【Actions】 中的 【Delete Key Pair】 按钮</li><li>在弹出的 【Confirm Delete Key Pair】 窗口中，点击 【Delete Key Pair】 按钮。</li></ol></li><li>CLI:<ol><li>登录到 rally 测试服务器；</li><li>使用 rally 测试文件 create-and-delete-keypair.yaml；</li><li>执行测试命令 <code>rally task start create-and-delete-keypair.yaml</code> 。</li></ol></li></ul>|<ul><li>UI:<ul><li>Key Pair 创建后，成功删除；</li></ul></li><li>CLI:<ul><li>Rally 测试成功</li></ul></li></ul>||<ul><li>执行 10 次，每次并行执行 2 个测试</li><li>每次创建 3 个 tenant，每个 tenant 包含 2 个 user</li></ul>|Rally:</br>create-and-delete-keypair.yaml|
