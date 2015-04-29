# 基础环境检测

该命令用于对EayunStack环境中的各节点进行基础环境检测，包括对NTP、SELinux、Disk、Network的检测。

## 命令格式

```
$ eayunstack doctor env --help
usage: eayunstack doctor env [-h] [-n {ntp,selinux,disk,network}] [-a]
                             [-o FILENAME]

Check Environment Object

optional arguments:
  -h, --help            show this help message and exit
  -n {ntp,selinux,disk,network}
                        Object Name
  -a, --all             Check ALL
  -o FILENAME           Local File To Save Output Info
```

## NTP检测

该命令用于检测当前节点NTP服务运行状态及与上游NTP服务器的同步状态，当执行该命令输出类似如下信息时，当前节点NTP服务运行状态及与上游NTP服务器同步状态正常。

```
$ eayunstack doctor env -n ntp
[ INFO  ] ========== start running check_ntp ==========
[ INFO  ]    Service ntpd is running ...
[ INFO  ]    Service ntpd is enabled ...
[ INFO  ] ntpserver is 172.16.100.2
```

## SELinux检测

该命令用于检测当前节点SELinux模式及配置文件中所配置的模式，当执行该命令输出类似如下信息时当前节点SELinux模式配置正常。

```
$ eayunstack doctor env -n selinux
[ INFO  ] ========== start running check_selinux ==========
[ INFO  ] SELinux current state is: Disabled
[ INFO  ] SELinux current conf in profile is: disabled
```

## Disk检测

该命令用于检测当前节点“/”文件系统的空间使用率。当“/”文件系统空间使用率大于85%时，执行该命令会发出警告。

```
$ eayunstack doctor env -n disk
[ INFO  ] ========== start running check_disk ==========
[ INFO  ] The "/" filesystem used 32% space !
```

## Network检测

该命令用于检测当前节点的网卡状态。执行该命令后可查看该节点对应网卡的连接状态。

```
$ eayunstack doctor env -n network
[ INFO  ] ========== start running check_network ==========
[ INFO  ] Network card information:
          eth3                                    : yes
          eth2                                    : yes
          eth1                                    : yes
          eth0                                    : yes
```

## 检测所有检测对象

该命令用于同时检测env子命令的所有检测对象。

```
$ eayunstack doctor env -a
[ DEBUG ] This option will do following things:
          --check_ntp
          --check_selinux
          --check_disk
          --check_network
[ INFO  ] ========== start running check_ntp ==========
[ INFO  ]    Service ntpd is running ...
[ INFO  ]    Service ntpd is enabled ...
[ INFO  ] ntpserver is 172.16.100.2
[ INFO  ] ========== start running check_selinux ==========
[ INFO  ] SELinux current state is: Disabled
[ INFO  ] SELinux current conf in profile is: disabled
[ INFO  ] ========== start running check_disk ==========
[ INFO  ] The "/" filesystem used 32% space !
[ INFO  ] ========== start running check_network ==========
[ INFO  ] Network card information:
          eth3                                    : yes
          eth2                                    : yes
          eth1                                    : yes
          eth0                                    : yes

```




















