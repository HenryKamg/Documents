# 验证 Cinder 的 volume 部分

|内容编号|内容名称|
|--------|--------|
|01|卷|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01030102|测试 cinder list 命令的功能|<ul><li>UI:</li></ul><ol><li>登录到 dashboard；</li><li>点击左侧导航栏的 Project，展开选项卡；</li><li>点击 Compute 子选项卡，展开；</li><li>点击 Volumes 选项。</li></ol><ul><li>CLI:</li></ul><ol><li>登录到 rally 测试服务器；</li><li>使用 rally 测试文件 list-volume.json；</li><li>执行测试命令 <code>rally task start list-volume.json</code> ；</li></ol>|<ul><li>UI:</br>显示该 project 中的所有 volume 的列表</li><li>CLI:</br>Rally 测试成功</li></ul>||列出卷|Rally:</br>list-volume.json|
|01030101|测试活跃卷的数量对创建卷的功能的影响|<ul><li>UI:</li></ul><ol><li>登录到 dashboard；</li><li>点击左侧导航栏的 Project，展开选项卡；</li><li>点击 Compute 子选项卡，展开；</li><li>点击 Volumes 选项；</li><li>点击 Create Volume 图标；</li><li>在弹出的对话框中，输入 Volume Name，选择 Volume Source 为 "No source, empty volume"，选择 Volume Type 为 "No volume type"；</li><li>设置卷的大小为 1G；</li><li>其他保持默认配置，点击 Create Volume 图标，创建 volume。</li></ol><ul><li>CLI:</li></ul><ol><li>登录到 rally 测试服务器；</li><li>使用 rally 测试文件 create-volumes.json (文件已经提前修改参数)；</li><li>执行测试命令 <code>rally task start create-volumes.json</li></ol>|<ul><li>UI:<ul><li>卷创建成功</li><li>卷的状态变化为 Creating -> Available</li></ul></li></ul><ul><li>CLI:<ul><li>Rally 测试成功</li></ul></li></ul>||创建卷|Rally:</br>create-volumes.json|
|01030103|随着卷的增加，测试 cinder list 命令的性能||||创建并列出卷|Rally:</br>create-and-list-volume.json|
|01030104|测试环境对卷的最大带宽||||创建卷后将其删除|Rally:</br>create-and-delete-volume.json|
|01030105|测试卷附加给实例的功能||||创建卷后将其附加给一个实例|Rally:</br>create-and-attach-volume.json|
|01030106|创建卷后将其扩展、删除|||||Rally:</br>create-and-extend-volume.json|
|01030107|创建一个卷后，将其上传到镜像中||||force or not|Rally:</br>create-and-upload-volume-to-image.json|
|01030108|从一个镜像中创建卷，然后删除||||与创建卷后将其删除其实一样|Rally:</br>create-from-image-and-delete-volume.json|
|01030109|测试卷的克隆||||从一个卷中创建卷，然后删除|Rally:</br>create-from-volume-and-delete-volume.json|
|01030110|创建一个嵌套的快照，然后附加卷||||volume->snapshot->volume->snapshot->volume...|Rally:</br>create_nested_snapshots_and_attach_volume.json|
|01030111|对 cinder 的压力测试||||创建卷、快照，然后附加/分离卷到实例上|Rally:</br>create-snapshot-and-attach-volume.json|
|01030112|更新卷状态，验证是否能执行非法操作|||||None|
