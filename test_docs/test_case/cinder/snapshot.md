# 验证 Cinder 组件的 snapshot 部分

|内容编号|内容名称|
|--------|--------|
|02|快照|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01030201|创建并列出快照|<ul><li>UI:<ol><li>登录到 dashboard；</li><li>点击左侧导航栏的 【Project】，展开选项卡；</li><li>点击 【Compute】 子选项卡，展开；</li><li>点击 【Volumes】 选项，选择一个现有的卷；</li><li>点击该卷的 【Actions】 下拉图标，点击 【Creat Snapshot】；</li><li>在弹出的 【Create Volume Snapshot】 窗口中，输入 Snapshot Name，选择性地输入 Description，点击 【Create Volume Snapshot】 按钮。</li></ol></li></ul><ul><li>CLI:<ol><li>登录到 rally 测试服务器；</li><li>使用 rally 测试文件 create-and-list-snapshots.json；</li><li>执行测试命令 <code>rally task start create-and-list-snapshots.json</code>。</li></ol></li></ul>|<ul><li>UI:<ul><li>快照创建成功，快照的状态变化为 Creating -> Available</li></ul></li></ul><ul><li>CLI:<ul><li>Rally 测试成功</li></ul></li></ul>||基于附加给实例的卷创建快照(有可能导致损坏的快照)，rally 中参数为 force|Rally:</br>create-and-list-snapshots.json|
||基于未附加卷的实例创建快照|<ul><li>UI:<ol><li>登录到 dashboard；</li><li>点击左侧导航栏的 【Project】，展开选项卡；</li><li>点击 【Compute】 子选项卡，展开；</li><li>点击 【Instances】 选项，在右侧的实例列表中选择一台实例；</li><li>点击该实例的 【Actions】 中的 【Create Snapshot】；</li><li>在弹出的 【Create Snapshot】 窗口中，输入 Snapshot Name，点击 【Create Snapshot】 按钮，创建实例快照。</li></ol></li></ul><ul><li>CLI:<ol><li></li></ol></li></ul>|<ul><li>UI:<ul><li>快照创建成功，在 【Images】 选项卡下可以看到新创建的快照，Type 显示为 Snapshot</li><li>快照的状态变化为 Queued -> Spaning -> Active</li></ul></li></ul>|||可以用 Rally 实现(待验证)</br>boot-snapshot-boot-delete.json|
||基于已附加卷的实例创建快照|<ul><li>UI:<ol><li>登录到 dashboard；</li><li>点击左侧导航栏的 【Project】，展开选项卡；</li><li>点击 【Compute】 子选项卡，展开；</li><li>点击 【Instances】 选项，在右侧的实例列表中选择一台已附加卷的实例；</li><li>点击该实例的 【Actions】 中的 【Create Snapshot】；</li><li>在弹出的 【Create Snapshot】 窗口中，输入 Snapshot Name，点击 【Create Snapshot】 按钮，创建实例快照。</li></ol></li></ul><ul><li>CLI:<ol><li></li></ol></li></ul>|<ul><li>UI:<ul><li>快照创建成功，在 【Images】 选项卡下可以看到新创建的快照，Type 显示为 Snapshot</li><li>快照的状态变化为 Queued -> Spaning -> Active</li><li>在 【Volume】 选项卡的 【Volume Snapshot】 标签下，看到新建了一个卷的快照，这个快照是实例所附加的卷的快照</li></ul></li></ul>||||
|01030202|测试快照的删除|<ul><li>UI:<ol><li>登录到 dashboard；</li><li>点击左侧导航栏的 【Project】，展开选项卡；</li><li>点击 【Compute】 子选项卡，展开；</li><li>点击 【Volume】 选项卡，在右侧点击 【Volume Snapshot】 标签；</li><li>选择一个快照，点击 【Actions】 的下拉图标，点击 【Delete Volume Snapshot】；</li><li>在弹出的 【Confirm Delete Volume Snapshot】 确认窗口中，点击 【Delete Volume Snapshot】 按钮。</li></ol></li></ul><ul><li>CLI:<ol><li>登录到 rally 测试服务器；</li><li>使用 rally 测试文件 create-and-delete-snapshot.json；</li><li>执行测试命令 <code>rally task start create-and-delete-snapshot.json</code>。</li></ol></li></ul>|<ul><li>UI:<ul><li>卷的状态变为 Deleting</li><li>卷删除成功，列表中不再显示卷的信息</li></ul></li></ul><ul><li>CLI:<ul><li>Rally 测试成功</li></ul></li></ul>|||Rally:</br>create-and-delete-snapshot.json|
|01030203|更新快照状态，验证是否能够执行非法操作|||||None|
