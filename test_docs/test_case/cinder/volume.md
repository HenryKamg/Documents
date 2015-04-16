# 验证 Cinder 的 volume 部分

|内容编号|内容名称|
|--------|--------|
|01|卷|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01030101|测试活跃卷的数量对创建卷的性能的影响|<ol><li>在默认 project 中创建卷；</li><li>设置卷的大小为 1 GB.</li></ol>|<ul><li>卷创建成功</li></ul>||创建卷|Rally:</br>list-volumes.json|
|01030102|测试 cinder list 命令的性能|<ol><li>列出默认的 project 中的卷。</li></ol>|<ul><li>列出所有该 project 中的卷</li></ul>||列出卷|Rally:</br>create-volume.json|
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
