# 验证 Nova 的 server 部分

|内容编号|内容名称|
|--------|--------|
|03|虚拟机|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01080301|启动一台实例|<ol><li>创建实例，选择从镜像启动；</li><li>使用镜像 TestVM；</li><li>选择实例的类型为 m1.tiny；</li><li>启动实例。</li></ol>|<ul><li>实例创建成功</li><li>实例以所选择的镜像和类型启动</li></ul>||需要针对不同的实例 flavor 和 boot source 写测试用例|Rally:</br>boot.json|
|01080302|测试 nova list 命令的性能|<ol><li>创建实例，选择从镜像启动；</li><li>使用镜像 TestVM；</li><li>选择实例的类型为 m1.tiny；</li><li>启动实例。</li><li>列出实例。</li></ol>|<ul><li>实例创建成功</li><li>实例以所选择的镜像和类型启动</li><li>列出的实例中包含所创建的实例</li></ul>||启动并列出一台实例|Rally:</br>boot-and-list.json|
|01080303|启动一台实例，然后将其删除|<ol><li>创建实例，选择从镜像启动；</li><li>使用镜像 TestVM；</li><li>选择实例的类型为 m1.tiny；</li><li>启动实例；</li><li>将该实例删除。</li></ol>||||Rally:</br>boot-and-delete.json|
|01080304|测试在同一个 availability zone 中迁移实例|<ol><li>创建实例，选择从镜像启动；</li><li>使用镜像 TestVM；</li><li>选择实例的类型为 m1.tiny；</li><li>启动实例；</li><li>停止运行实例；</li><li>将该实例迁移到另一台主机上。</li></ol>|||测试在同一个 availability zone 中迁移实例|Rally:</br>boot-and-migrate.json|
|01080305|测试在同一个 availability zone 中在线迁移实例|<ol><li>创建实例，选择从镜像启动；</li><li>使用镜像 TestVM；</li><li>选择实例的类型为 m1.tiny；</li><li>启动实例；</li><li>不停止运行实例，直接将实例迁移到另一台主机上。</li></ol>|||启动一台实例，然后在线迁移实例|Rally:</br>boot-and-live-migrate.json|
|01080306|启动一台实例，并在实例中执行一些特定操作|<ol><li>创建实例，选择从镜像启动；</li><li>使用镜像 TestVM；</li><li>选择实例的类型为 m1.tiny；</li><li>启动实例；</li><li>在实例中执行特定操作。</li></ol>||||Rally:</br>boot-bounce-delete.json|
|01080306|启动一台实例，并在实例中执行脚本|<ol><li>创建实例，选择从镜像启动；</li><li>使用镜像 TestVM；</li><li>选择实例的类型为 m1.tiny；</li><li>启动实例；</li><li>在实例中执行某个脚本。</li></ol>||||Rally:</br>vm/boot-runcommand-delete.json|
|01080307|从一个卷启动一台实例|<ol><li>创建一台实例，选择从云硬盘启动；</li><li>选择卷；</li><li>启动实例。</li></ol>||||Rally:</br>boot-from-volume.json|
|01080308|从一个卷启动一台实例，然后将实例删除|<ol><li>创建一台实例，选择从云硬盘启动；</li><li>选择卷；</li><li>启动实例；</li><li>将该实例删除。</li></ol>||||Rally:</br>boot-from-volume-and-delete.json|
|01080310|从一个卷启动一台实例，然后在线迁移实例|<ol><li>创建一台实例，选择从云硬盘启动；</li><li>选择卷；</li><li>启动实例；</li><li>不停止运行实例，直接将该实例迁移到另一台主机上。</li></ol>||||Rally:</br>boot-server-from-volume-and-live-migrate.json|
|01080311|创建一台实例，附加一个卷，然后在线迁移实例|||||Rally:</br>boot-server-attach-created-volume-and-live-migrate.json|
|01080312|创建一台实例，重新定义实例大小，然后删除实例||||实例 resize: small -> big & big -> small 的情况需要考虑，参数为 to_flavor|Rally:</br>resize-server.json|
|01080313|创建一台实例，然后创建该实例的快照，而后删除实例和快照|||||Rally:</br>boot-snapshot-boot-delete.json|
|01080314|以某个 keypair 创建和删除实例|||||Rally:</br>boot-and-delete-server-with-keypairs.json|
|01080315|以某个 secgroup 创建和删除实例||||Rally:</br>boot-and-delete-server-with-secgroups.json|
||创建实例，pause 后将其恢复|||||Rally:</br>pause-and-unpause.json|
||创建实例，suspend 后将其恢复|||||Rally:</br>suspend-and-resume.json|

