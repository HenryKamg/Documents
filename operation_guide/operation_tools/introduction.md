# 简介

EayunStack运维工具提供了对EayunStack环境的检测、管理功能。主要功能通过子命令来实现以下功能：

* init
   * 初始化EayunStack环境
* fuel
   * Fuel节点备份
   * Fuel节点恢复
* manage
   * 列出所有OpenStack节点信息
   * 删除错误的Cinder卷
   * 上传AMI镜像
* doctor
   * 检测所有OpenStack节点基础环境状态
   * 检测所有OpenStack节点OpenStack组件配置及服务运行状态
   * 检测MySQL/RabbitMQ/Ceph集群状态

## 命令格式

```
$ eayunstack --help
usage: eayunstack [-h] COMMAND ...

EayunStack Management Tools.

optional arguments:
  -h, --help  show this help message and exit

Commands:
  COMMAND     DESCRIPTION
    fuel      EayunStack Fuel Management
    init      EayunStack Environment Initialization
    manage    EayunStack Management
    doctor    EayunStack Doctor
```
