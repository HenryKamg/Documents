* [ horzion上vnc加载失败 ](#horzion上vnc加载失败)
* [ 重启libvirt ](#重启libvirt)
* [ 备份volume ](#备份volume)
* [ 恢复volume ](#恢复volume)
* [ 恢复rabbitmq集群 ](#恢复rabbitmq集群)

#### horzion上vnc加载失败
* 用 eayunstack 运维工具检查 EayunStack 集群是否正常
* 尝试刷新重新加载 url
* 登录控制节点, 使用 ```nova get-vnc-console [ID]```, 得到 novnc 的url, 检查改url是否和浏览器上的 novnc 地址一致.
* 检查云主机是否正常运行. 使用 nova show [ID] 得到云主机运行的计算节点, 登录计算节点, 使用 ```ps aux | grep [ID]``` 查看云主机对应的 qemu-kvm 进程是否在运行.
* 在各个 controller 节点重启 nova-consoleauth 和 nova-novncproxy 服务

#### 重启libvirt
如果由于某些原因(比如重新配置log级别定位问题, 或者libvirt发生错误)需要重启 libvirt, 由于计算服务依赖于libvirt服务, 并且不会自动重连libvirt, 所以相应的 nova-compute 也需要重启, 步骤如下(假设重启的节点为 node-1):
* 在 node-1 使用以下指令重启libvirt
```
# systemctl libvirtd.service restart
```
* 在 node-2 使用以下指令重启 nova-compute
```
# systemctl openstack-nova-compute.service restart
```

> ###### 注意
> * libvirt 和 nova-compute 服务只运行在计算节点
> * 在哪一台计算节点上重启了 libvirt 服务, 那么必须在这台计算节点重启 nova-compute 服务

#### 备份volume
* 确保 cinder-backup 服务处在运行状态, 如果该服务没有运行, 启动它
```
# systemctl start openstack-cinder-backup
```
* 然后使用以下指令备份 volume
```
# cinder backup-create --display-name [name] [volumeID]
```
其中 **name** 是你自己取的备份的名字, **volumeID** 是你要备份的卷的ID
* 等待 ```cinder backup-list [name]``` 的 Status 由 creating 变为 available, 表示备份完成.
* 关闭 backup 服务
```
# systemctl stop openstack-cinder-backup
```

> ###### 注意
> * cinder 备份操作只能通过命令行或者 API 实现, horizon 暂不支持
> * 由于 eqlx 存储最大管理连接数的限制, 每个 backup服务要占用一个连接session, 影响 cinder-volume 的使用, cinder backup 按需开启, 即需要备份和恢复的时候打开该服务, 完成备份关闭该服务.

#### 恢复volume
* 确保 cinder-backup 服务处在运行状态, 如果该服务没有运行, 启动它
```
# systemctl start openstack-cinder-backup
```
* 然后使用以下指令恢复 volume
```
# cinder backup-restore [backupID]
```
其中 **backupID** 是你要恢复的卷的ID, 通过 ```cinder backup-list``` 获取
* 等待 ```cinder list``` 中恢复的卷的 Status 由 restoring-backup 变为 available, 表示恢复完成.
* 关闭 backup 服务
```
# systemctl stop openstack-cinder-backup
```

> ###### 注意
> * cinder 恢复操作只能通过命令行或者 API 实现, horizon 暂不支持
> * 恢复时只能指定要恢复之前备份的卷的ID, 通过 ```cinder backup-list``` 获取, 不能指定名字

#### 恢复rabbitmq集群
