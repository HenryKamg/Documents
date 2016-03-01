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
  1. 执行命令，创建端口映射，将云主机的 9090 端口映射到路由的 22 端口上：

    ```
    (controller)# neutron portmapping-create 169e460d-16ff-4c25-bd2a-47250772541c 22 172.16.200.2 9090 --name test_portmapping
    ```

* 预期结果：

  * 端口映射创建成功：

    ```
    (controller)# neutron portmapping-create 169e460d-16ff-4c25-bd2a-47250772541c 22 172.16.200.2 9090 --name test_portmapping
    Created a new portmapping:
    +------------------+--------------------------------------+
    | Field            | Value                                |
    +------------------+--------------------------------------+
    | admin_state_up   | True                                 |
    | destination_ip   | 172.16.200.2                         |
    | destination_port | 9090                                 |
    | id               | ef15a002-4d2e-4ec8-916c-e11e3ac5cbed |
    | name             | test_portmapping                     |
    | protocol         | tcp                                  |
    | router_id        | 169e460d-16ff-4c25-bd2a-47250772541c |
    | router_port      | 22                                   |
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
    | destination_port | 9090                                 |
    | id               | ef15a002-4d2e-4ec8-916c-e11e3ac5cbed |
    | name             | test_portmapping                     |
    | protocol         | tcp                                  |
    | router_id        | 169e460d-16ff-4c25-bd2a-47250772541c |
    | router_port      | 22                                   |
    | status           | ACTIVE                               |
    | tenant_id        | 7f67af7413074a85b751eaf997d59ae7     |
    +------------------+--------------------------------------+
    ```

## 验证端口映射

## 停用/启用端口映射

## 修改端口映射

## 删除端口映射
