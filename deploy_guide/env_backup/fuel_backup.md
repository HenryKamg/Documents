# Fuel节点备份

> ###### 注意
> 所有备份文件存放在“/var/backup/fuel/”目录下，建议将该目录备份到其它存储介质中，防止由于Fuel节点磁盘损坏导致备份文件丢失。

> ## 警告
> 备份时要满足以下两个条件：</br>
> * 没有正在进行的部署任务
> * "/var/backup/fuel/“目录下至少有 11 GB 的可用空间

```
[fuel]$ eayunstack fuel backup -n
[ INFO  ] Starting backup ...
[ INFO  ] It will take about 30 minutes, Please wait ...
[ INFO  ] Backup successfully completed!

You can use "eayunstack fuel backup [ -l | --list ]" to list your backups
```
