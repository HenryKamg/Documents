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
$ eayunstack -d doctor env -n ntp
[ DEBUG ] =====> start running check_ntp 
          Service ntpd is running ...
          Service ntpd is enabled ...
          ntpserver is 172.16.100.2
```

## SELinux检测

该命令用于检测当前节点SELinux模式及配置文件中所配置的模式，当执行该命令输出类似如下信息时当前节点SELinux模式配置正常。

```
$ eayunstack -d doctor env -n selinux
[ DEBUG ] =====> start running check_selinux 
          SELinux current state is: Disabled
          SELinux current conf in profile is: disabled
```

## Disk检测

该命令用于检测当前节点“/”文件系统的空间使用率。当“/”文件系统空间使用率大于85%时，执行该命令会发出警告。

```
$ eayunstack -d doctor env -n disk
[ DEBUG ] =====> start running check_disk 
          The "/" filesystem used 33% space !
```

## Network检测

该命令用于检测当前节点的网卡状态。执行该命令后可查看该节点对应网卡的连接状态。

```
$ eayunstack -d doctor env -n network
[ DEBUG ] =====> start running check_network 
[ DEBUG ] Network card eno1(br-mgmt) connected
[ DEBUG ] Network card eno2(br-ex) connected
[ DEBUG ] Network card enp5s0f0(br-storage) connected
[ DEBUG ] Network card enp5s0f1(br-prv) connected
[ DEBUG ] =====> start ping internal_address of node-1.eayun.com(controller):
[ DEBUG ] 172.16.101.3 reached
[ DEBUG ] =====> start ping storage_address of node-1.eayun.com(controller):
[ DEBUG ] 172.16.102.2 reached
[ DEBUG ] =====> start ping public_address of node-1.eayun.com(controller):
[ DEBUG ] 25.0.0.3 reached
[ DEBUG ] =====> start ping internal_address of node-2.eayun.com(controller):
[ DEBUG ] 172.16.101.4 reached
[ DEBUG ] =====> start ping storage_address of node-2.eayun.com(controller):
[ DEBUG ] 172.16.102.3 reached
[ DEBUG ] =====> start ping public_address of node-2.eayun.com(controller):
[ DEBUG ] 25.0.0.4 reached
[ DEBUG ] =====> start ping internal_address of node-3.eayun.com(controller):
[ DEBUG ] 172.16.101.5 reached
[ DEBUG ] =====> start ping storage_address of node-3.eayun.com(controller):
[ DEBUG ] 172.16.102.4 reached
[ DEBUG ] =====> start ping public_address of node-3.eayun.com(controller):
[ DEBUG ] 25.0.0.5 reached
[ DEBUG ] =====> start ping internal_address of node-4.eayun.com(ceph-osd):
[ DEBUG ] 172.16.101.6 reached
[ DEBUG ] =====> start ping storage_address of node-4.eayun.com(ceph-osd):
[ DEBUG ] 172.16.102.5 reached
[ DEBUG ] =====> start ping internal_address of node-5.eayun.com(ceph-osd):
[ DEBUG ] 172.16.101.7 reached
[ DEBUG ] =====> start ping storage_address of node-5.eayun.com(ceph-osd):
[ DEBUG ] 172.16.102.6 reached
[ DEBUG ] =====> start ping internal_address of node-6.eayun.com(ceph-osd):
[ DEBUG ] 172.16.101.8 reached
[ DEBUG ] =====> start ping storage_address of node-6.eayun.com(ceph-osd):
[ DEBUG ] 172.16.102.7 reached
[ DEBUG ] =====> start ping internal_address of node-7.eayun.com(primary-mongo):
[ DEBUG ] 172.16.101.9 reached
[ DEBUG ] =====> start ping internal_address of node-8.eayun.com(compute):
[ DEBUG ] 172.16.101.10 reached
[ DEBUG ] =====> start ping storage_address of node-8.eayun.com(compute):
[ DEBUG ] 172.16.102.9 reached
[ DEBUG ] =====> start ping internal_address of node-10.eayun.com(compute):
[ DEBUG ] 172.16.101.11 reached
[ DEBUG ] =====> start ping storage_address of node-10.eayun.com(compute):
[ DEBUG ] 172.16.102.10 reached
[ DEBUG ] =====> start ping internal_address of node-12.eayun.com(ceph-osd):
[ DEBUG ] 172.16.101.12 reached
[ DEBUG ] =====> start ping storage_address of node-12.eayun.com(ceph-osd):
[ DEBUG ] 172.16.102.11 reached
```

## 检测所有检测对象

该命令用于同时检测env子命令的所有检测对象。

```
$ eayunstack -d doctor env -a
[ DEBUG ] =====> start running check_ntp 
          Service ntpd is running ...
          Service ntpd is enabled ...
          ntpserver is 172.16.100.2
[ DEBUG ] =====> start running check_selinux 
          SELinux current state is: Disabled
          SELinux current conf in profile is: disabled
[ DEBUG ] =====> start running check_disk 
          The "/" filesystem used 33% space !
[ DEBUG ] =====> start running check_network 
[ DEBUG ] Network card eno1(br-mgmt) connected
[ DEBUG ] Network card eno2(br-ex) connected
[ DEBUG ] Network card enp5s0f0(br-storage) connected
[ DEBUG ] Network card enp5s0f1(br-prv) connected
[ DEBUG ] =====> start ping internal_address of node-1.eayun.com(controller):
[ DEBUG ] 172.16.101.3 reached
[ DEBUG ] =====> start ping storage_address of node-1.eayun.com(controller):
[ DEBUG ] 172.16.102.2 reached
[ DEBUG ] =====> start ping public_address of node-1.eayun.com(controller):
[ DEBUG ] 25.0.0.3 reached
[ DEBUG ] =====> start ping internal_address of node-2.eayun.com(controller):
[ DEBUG ] 172.16.101.4 reached
[ DEBUG ] =====> start ping storage_address of node-2.eayun.com(controller):
[ DEBUG ] 172.16.102.3 reached
[ DEBUG ] =====> start ping public_address of node-2.eayun.com(controller):
[ DEBUG ] 25.0.0.4 reached
[ DEBUG ] =====> start ping internal_address of node-3.eayun.com(controller):
[ DEBUG ] 172.16.101.5 reached
[ DEBUG ] =====> start ping storage_address of node-3.eayun.com(controller):
[ DEBUG ] 172.16.102.4 reached
[ DEBUG ] =====> start ping public_address of node-3.eayun.com(controller):
[ DEBUG ] 25.0.0.5 reached
[ DEBUG ] =====> start ping internal_address of node-4.eayun.com(ceph-osd):
[ DEBUG ] 172.16.101.6 reached
[ DEBUG ] =====> start ping storage_address of node-4.eayun.com(ceph-osd):
[ DEBUG ] 172.16.102.5 reached
[ DEBUG ] =====> start ping internal_address of node-5.eayun.com(ceph-osd):
[ DEBUG ] 172.16.101.7 reached
[ DEBUG ] =====> start ping storage_address of node-5.eayun.com(ceph-osd):
[ DEBUG ] 172.16.102.6 reached
[ DEBUG ] =====> start ping internal_address of node-6.eayun.com(ceph-osd):
[ DEBUG ] 172.16.101.8 reached
[ DEBUG ] =====> start ping storage_address of node-6.eayun.com(ceph-osd):
[ DEBUG ] 172.16.102.7 reached
[ DEBUG ] =====> start ping internal_address of node-7.eayun.com(primary-mongo):
[ DEBUG ] 172.16.101.9 reached
[ DEBUG ] =====> start ping internal_address of node-8.eayun.com(compute):
[ DEBUG ] 172.16.101.10 reached
[ DEBUG ] =====> start ping storage_address of node-8.eayun.com(compute):
[ DEBUG ] 172.16.102.9 reached
[ DEBUG ] =====> start ping internal_address of node-10.eayun.com(compute):
[ DEBUG ] 172.16.101.11 reached
[ DEBUG ] =====> start ping storage_address of node-10.eayun.com(compute):
[ DEBUG ] 172.16.102.10 reached
[ DEBUG ] =====> start ping internal_address of node-12.eayun.com(ceph-osd):
[ DEBUG ] 172.16.101.12 reached
[ DEBUG ] =====> start ping storage_address of node-12.eayun.com(ceph-osd):
[ DEBUG ] 172.16.102.11 reached
```




















