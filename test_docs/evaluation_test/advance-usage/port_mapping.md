# 路由端口映射

## 创建端口映射

* 前提：

  * 租户下创建了路由；
  * 租户下创建了云主机，云主机连接到路由且获得一个内网的 IP 地址。

* 操作：

  1. 登录到 Controller 节点；
  1. 获取租户的路由 ID：

    ```
    (controller)# neutron router-show test_router
    ```
  1. 获取云主机的 IP 地址：

    ```
    (controller)# nova show test_server
    ```
  1. 执行命令，创建端口映射，将云主机的 22 端口映射到路由的 9022 端口上：

    ```
    (controller)# neutron portmapping-create 169e460d-16ff-4c25-bd2a-47250772541c 9022 172.16.200.2 22 --name test_portmapping
    ```

* 预期结果：

  * 端口映射创建成功：

    ```
    (controller)# neutron portmapping-create 169e460d-16ff-4c25-bd2a-47250772541c 9022 172.16.200.2 22 --name test_portmapping
    Created a new portmapping:
    +------------------+--------------------------------------+
    | Field            | Value                                |
    +------------------+--------------------------------------+
    | admin_state_up   | True                                 |
    | destination_ip   | 172.16.200.2                         |
    | destination_port | 22                                   |
    | id               | ef15a002-4d2e-4ec8-916c-e11e3ac5cbed |
    | name             | test_portmapping                     |
    | protocol         | tcp                                  |
    | router_id        | 169e460d-16ff-4c25-bd2a-47250772541c |
    | router_port      | 9022                                 |
    | status           | DOWN                                 |
    | tenant_id        | 7f67af7413074a85b751eaf997d59ae7     |
    +------------------+--------------------------------------+
    ```
  * 端口映射创建完成后，状态为 "ACTIVE"：

    ```
    (controller)# neutron portmapping-show test_portmapping
    +------------------+--------------------------------------+
    | Field            | Value                                |
    +------------------+--------------------------------------+
    | admin_state_up   | True                                 |
    | destination_ip   | 172.16.200.2                         |
    | destination_port | 22                                   |
    | id               | ef15a002-4d2e-4ec8-916c-e11e3ac5cbed |
    | name             | test_portmapping                     |
    | protocol         | tcp                                  |
    | router_id        | 169e460d-16ff-4c25-bd2a-47250772541c |
    | router_port      | 9022                                 |
    | status           | ACTIVE                               |
    | tenant_id        | 7f67af7413074a85b751eaf997d59ae7     |
    +------------------+--------------------------------------+
    ```

## 验证端口映射

* 前提：

  * 租户中的安全组允许 SSH 的操作；
  * 租户中创建了一台云主机，该云主机分配了内网地址，开启了 SSH，允许通过用户名和密码 SSH；
  * 该云主机没有分配浮动 IP，无法从外网进行 SSH 连接。

* 操作：

  1. 获取云主机所连接的路由 ID 和路由网关：

    ```
    (controller)# neutron router-show [ROUTER_NAME]
    ```
  1. 将云主机的 22 端口映射到路由的 9022 端口上：

    ```
    (controller)# neutron portmapping-create [ROUTER_ID] 9022 [INSTANCE_IP] 22
    ```
  1. 从外网（如本地机器）执行 SSH 命令，尝试 SSH 到云主机：

    ```
    $ ssh username@[ROUTER_GATEWAY_IP] -p 9022
    ```

* 预期结果：

  * 端口映射创建成功：

    ```
    (controller)# neutron portmapping-create 169e460d-16ff-4c25-bd2a-47250772541c 9022 172.16.200.6 22
    Created a new portmapping:
    +------------------+--------------------------------------+
    | Field            | Value                                |
    +------------------+--------------------------------------+
    | admin_state_up   | True                                 |
    | destination_ip   | 172.16.200.6                         |
    | destination_port | 22                                   |
    | id               | 6e6b5686-e7cb-4e97-b275-fc8777358a18 |
    | name             |                                      |
    | protocol         | tcp                                  |
    | router_id        | 169e460d-16ff-4c25-bd2a-47250772541c |
    | router_port      | 9022                                 |
    | status           | DOWN                                 |
    | tenant_id        | 7f67af7413074a85b751eaf997d59ae7     |
    +------------------+--------------------------------------+
    ```
  * 端口映射创建完成后，可以成功从外网通过 9022 端口 SSH 到云主机中：

    ```
    (controller)# neutron portmapping-show 6e6b5686-e7cb-4e97-b275-fc8777358a18
    +------------------+--------------------------------------+
    | Field            | Value                                |
    +------------------+--------------------------------------+
    | admin_state_up   | True                                 |
    | destination_ip   | 172.16.200.6                         |
    | destination_port | 22                                   |
    | id               | 6e6b5686-e7cb-4e97-b275-fc8777358a18 |
    | name             |                                      |
    | protocol         | tcp                                  |
    | router_id        | 169e460d-16ff-4c25-bd2a-47250772541c |
    | router_port      | 9022                                 |
    | status           | ACTIVE                               |
    | tenant_id        | 7f67af7413074a85b751eaf997d59ae7     |
    +------------------+--------------------------------------+

    ssh test@25.0.0.134 -p 9022
    test@25.0.0.134's password: 
    Last login: Tue Mar  1 08:12:04 2016 from 25.0.0.1
    [test@coffee-test-01 ~]#
    ```

## 停用/启用端口映射（更新端口映射）

* 前提：

  * 租户下创建了一台没有分配浮动 IP 的云主机；
  * 租户的安全组允许 SSH 的操作；
  * 将该云主机的 22 端口映射到路由的 9022 端口上，云主机可以通过路由的 9022 端口进行 SSH 连接；
  * 端口的状态为 "ACTIVE"：

    ```
    (controller)# neutron portmapping-show 6e6b5686-e7cb-4e97-b275-fc8777358a18
    +------------------+--------------------------------------+
    | Field            | Value                                |
    +------------------+--------------------------------------+
    | admin_state_up   | True                                 |
    | destination_ip   | 172.16.200.6                         |
    | destination_port | 22                                   |
    | id               | 6e6b5686-e7cb-4e97-b275-fc8777358a18 |
    | name             |                                      |
    | protocol         | tcp                                  |
    | router_id        | 169e460d-16ff-4c25-bd2a-47250772541c |
    | router_port      | 9022                                 |
    | status           | ACTIVE                               |
    | tenant_id        | 7f67af7413074a85b751eaf997d59ae7     |
    +------------------+--------------------------------------+
    ```

* 操作：

  1. 执行命令，停用端口映射：

    ```
    (controller)# neutron portmapping-update [PORTMAPPING_ID] --admin_state_up False
    ```
  1. 尝试从路由的 9022 端口 SSH 到云主机；
  1. 执行命令，启用端口映射：

    ```
    (controller)# neutron portmapping-update [PORTMAPPING_ID] --admin_state_up True
    ```
  1. 再次尝试从路由的 9022 端口 SSH 到云主机。

* 预期结果：

  * 停用端口映射成功，端口映射的状态为 "DOWN"：

    ```
    (controller)# neutron portmapping-show 6e6b5686-e7cb-4e97-b275-fc8777358a18
    +------------------+--------------------------------------+
    | Field            | Value                                |
    +------------------+--------------------------------------+
    | admin_state_up   | False                                |
    | destination_ip   | 172.16.200.6                         |
    | destination_port | 22                                   |
    | id               | 6e6b5686-e7cb-4e97-b275-fc8777358a18 |
    | name             |                                      |
    | protocol         | tcp                                  |
    | router_id        | 169e460d-16ff-4c25-bd2a-47250772541c |
    | router_port      | 9022                                 |
    | status           | DOWN                                 |
    | tenant_id        | 7f67af7413074a85b751eaf997d59ae7     |
    +------------------+--------------------------------------+
    ```
  * 端口映射停用后，SSH 连接失败：

    ```
    $ ssh test@25.0.0.134 -p 9022
    ssh: connect to host 25.0.0.134 port 9022: Connection refused
    ```
  * 启用端口映射后，端口映射的状态恢复为 "ACTIVE"：

    ```
    (controller)# neutron portmapping-show 6e6b5686-e7cb-4e97-b275-fc8777358a18
    +------------------+--------------------------------------+
    | Field            | Value                                |
    +------------------+--------------------------------------+
    | admin_state_up   | True                                 |
    | destination_ip   | 172.16.200.6                         |
    | destination_port | 22                                   |
    | id               | 6e6b5686-e7cb-4e97-b275-fc8777358a18 |
    | name             |                                      |
    | protocol         | tcp                                  |
    | router_id        | 169e460d-16ff-4c25-bd2a-47250772541c |
    | router_port      | 9022                                 |
    | status           | ACTIVE                               |
    | tenant_id        | 7f67af7413074a85b751eaf997d59ae7     |
    +------------------+--------------------------------------+
    ```
  * 重新启用端口映射，SSH 连接成功：

    ```
    $ ssh test@25.0.0.134 -p 9022
    test@25.0.0.134's password: 
    Last login: Tue Mar  1 08:12:50 2016 from 25.0.0.1
    [test@coffee-test-01 ~]# 
    ```

## 删除端口映射

* 前提：

  * 租户下创建了一台没有分配浮动 IP 的云主机；
  * 租户的安全组允许 SSH 的操作；
  * 将该云主机的 22 端口映射到路由的 9022 端口上，云主机可以通过路由的 9022 端口进行 SSH 连接；
  * 端口的状态为 "ACTIVE"：

* 操作：

  1. 执行命令，删除端口映射：

    ```
    (controller)# neutron portmapping-delete [PORTMAPPING_ID]
    ```
  1. 尝试从路由的 9022 端口 SSH 到云主机。

* 预期结果：

  * 端口映射成功删除：

    ```
    (controller)# neutron portmapping-delete 6e6b5686-e7cb-4e97-b275-fc8777358a18
    Deleted portmapping: 6e6b5686-e7cb-4e97-b275-fc8777358a18
    ```
  * 从路由的 9022 端口 SSH 到云主机失败：

    ```
    $ ssh root@25.0.0.134 -p 9022
    ssh: connect to host 25.0.0.134 port 9022: Connection refused
    ```
