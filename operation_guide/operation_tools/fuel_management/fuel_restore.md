# Fuel节点恢复

该命令主要用来恢复Fuel节的备份。

## 命令格式

```
[fuel]$ eayunstack fuel restore --help
usage: eayunstack fuel restore [-h] [-i ID] [-f FILE]

Fuel Restore

optional arguments:
  -h, --help            show this help message and exit
  -i ID, --id ID        Specify the ID you want to restore
  -f FILE, --file FILE  Specify the backup path to restore
```

## 恢复备份

```
[fuel]$ eayunstack fuel restore -i 1
[ INFO  ] Starting Restore ...
[ INFO  ] It will take about 30 minutes, Please wait ...

[ INFO  ] Restore successfully completed!
```
