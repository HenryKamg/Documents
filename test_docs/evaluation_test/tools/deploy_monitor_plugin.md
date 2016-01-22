# 部署监控插件

## 部署 influxdb/grafana 服务

* 前提：

  * Fuel 节点已经安装完成；
  * EayunStack 环境已经部署完成。

* 操作：

  1. 登录 Fuel 节点；
  1. 获取要部署监控平台的环境 ID：

    ```
    (fuel)# fuel environment list
    id | status      | name       | mode       | release_id | changes                                                                  | pending_release_id
    ---|-------------|------------|------------|------------|--------------------------------------------------------------------------|-------------------
    1  | operational | EayunStack | ha_compact | 1          | [{u'node_id': 3, u'name': u'disks'}, {u'node_id': 4, u'name': u'disks'}] | None              

    # 即环境 ID 为 1
    ```
  1. 执行命令，部署 influxdb/grafana 服务：

    TODO

## 部署 lma_collector 服务

* 前提：

  * 已经部署好 influxdb/grafana 服务。

* 操作：

  1. 登录 Fuel 节点；
  1. 执行命令，部署 lma_collector 服务：

    TODO
