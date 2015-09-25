# 简介

EayunStack运维工具提供了对EayunStack环境的检测、管理功能。主要功能通过子命令来实现以下功能：

* fuel
   * Fuel节点备份
   * Fuel节点恢复
   * Ceph Cluster网络配置
* init
   * 初始化EayunStack环境
* manage
   * 删除错误的Cinder卷
   * 上传AMI镜像
* list
   * 列出环境中所有OpenStack节点的信息
* doctor
   * 检测所有OpenStack节点基础环境状态
   * 检测所有OpenStack节点OpenStack组件配置及服务运行状态
   * 检测MySQL/RabbitMQ/Ceph集群状态
   * 检测OpenStack网络（如virtual router检测）

## 命令格式

```
# eayunstack --help
usage: eayunstack [-h] [-o FILENAME] [-d] [-e EMAIL] COMMAND ...

EayunStack Management Tools.

optional arguments:
  -h, --help            show this help message and exit
  -o FILENAME, --output FILENAME
                        Local File To Save Output Info
  -d, --debug           Log debug message or not
  -e EMAIL, --email EMAIL
                        email address which send error log to

Commands:
  COMMAND               DESCRIPTION
    fuel                EayunStack Fuel Management
    init                EayunStack Environment Initialization
    manage              EayunStack Management
    list                List OpenStack Node
    doctor              EayunStack Doctor
```
