# 验证 Glance 的镜像功能

|内容编号|内容名称|
|--------|--------|
|01|镜像|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01040101|测试 glance image-list 命令的性能||||列出镜像|Rally:</br>list_images.json|
|01040102|随着镜像的增加，测试 glance image-list 命令的性能||||创建并列出镜像，需要针对不同类型的镜像写测试用例|Rally:</br>create-and-list-image.json|
|01040103|创建镜像后，将其删除|||||Rally:</br>create-and-delete-image.json|
|01040104|创建镜像，从该镜像启动实例||||可能会跟 nova/server.md 重复|Rally:</br>create-image-and-boot-instances.json|

