# 防火墙服务

## 创建不允许 PING 操作的防火墙

* 前提：

  * 环境中还未创建防火墙；
  * 环境中的安全组策略允许 PING 的操作；
  * 环境中已经创建了一台云主机，这台云主机分配了外网地址，能够从外网 PING 通；
  * 用户已经登录到 EayunStack 管理界面。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项，点击 【Network】 子选项，点击其中的 【Firewalls】；
  1. 在右侧列表中，点击 【Firewall Rules】 标签；
  1. 点击列表上方的 【Add Rule】 按钮，在弹出的 【Add Rule】 窗口中：

    * 填写 Name 为 "enable-ping"；
    * 选择 Protocol 为 "ICMP"；
    * 选择 Action 为 "DENY"；
    * 勾选窗口下方的 "Enable"；

  1. 其他保持默认配置，点击窗口下方的 【Add】 按钮，创建防火墙规则；
  1. 点击 【Firewall Policies】 标签，点击列表上方的 【Add Policy】 按钮，在弹出的 【Add Policy】 窗口中：

    * 在窗口的 【AddPolicy】 标签下，填写 Name 为 "policy1"；
    * 在窗口的 【Rules】 标签下，点击 Available Rules 中的规则 "enable-ping" 后的 【+】 图标，将防火墙规则添加到 policy1 策略中；

  1. 其他保持默认配置，点击窗口下方的 【Add】 按钮，创建防火墙策略；
  1. 点击 【Firewalls】 标签，点击列表上方的 【Create Firewall】 按钮，在弹出的 【Add Firewall】 窗口中：

    * 填写 Name 为 "my-firewall"；
    * 选择 Policy 为 "policy1"；
    * Admin State 保持默认配置，即 "UP"；

  1. 点击窗口下方的 【Add】 按钮。

* 预期结果：

  * 防火墙创建成功，防火墙状态为 "ACTIVE"；
  * 创建防火墙之前，可以 PING 通云主机；
  * 防火墙创建后，不能 PING 通云主机。

> ###### 说明：
> * EayunStack 环境中默认不允许 PING 云主机；
> * 环境中没有防火墙的情况下，使用安全组的规则；如果创建了防火墙，防火墙没有允许的规则一律不会被通过：
>   * 安全组允许 PING，没有防火墙 -> 可以 PING；
>   * 安全组允许 PING，创建了防火墙，防火墙允许 PING -> 可以 PING；
>   * 安全组允许 PING，创建了防火墙，但防火墙没有允许 PING -> 不能 PING；
>   * 安全组不允许 PING，没有防火墙 -> 不能 PING；
>   * 安全组不允许 PING，创建了防火墙，防火墙允许 PING -> 不能 PING。

## 创建允许 SSH 操作的规则并添加到防火墙策略中

* 前提：

  * 环境中已经创建防火墙；
  * 环境中的安全组策略允许 SSH 的操作；
  * 环境中已经创建了一台云主机，这台云主机分配了外网地址 (在上述防火墙规则下能够 PING 通)；
  * 用户已经登录到 EayunStack 管理界面中。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项，点击 【Network】 子选项，点击其中的 【Firewalls】；
  1. 在右侧列表中，点击 【Firewall Rules】 标签；
  1. 点击列表上方的 【Add Rule】 按钮，在弹出的 【Add Rule】 窗口中：

    * 填写 Name 为 "enable-ssh"；
    * 选择 Protocol 为 "TCP"；
    * 选择 Action 为 "ALLOW"；
    * Destination Port/Port Range 中填写 "22"；
    * 勾选窗口下方的 "Enable"；

  1. 其他保持默认配置，点击窗口下方的 【Add】 按钮，创建防火墙规则；
  1. 点击 【Firewall Policies】 标签，点击列表上方的 【Add Policy】 按钮，在弹出的 【Add Policy】 窗口中：

    * 在窗口的 【AddPolicy】 标签下，填写 Name 为 "policy2"；
    * 在窗口的 【Rules】 标签下，点击 Available Rules 中的规则 "enable-ssh" 后的 【+】 图标，将防火墙规则添加到 policy2 策略中；

  1. 其他保持默认配置，点击窗口下方的 【Add】 按钮，创建防火墙策略；
  1. 点击 【Firewalls】 标签，选择防火墙 "my-firewall"，点击 【Actions】 中的 【Edit Firewall】；
  1. 在弹出的 【Edit Firewall】 窗口中，选择 Policy 为 "policy2"，点击窗口下方的 【Save Changes】，保存更改。

* 预期结果：

  * 防火墙更新成功，防火墙状态为 "ACTIVE"；
  * 创建防火墙之前，不能对云主机执行 SSH 操作；
  * 防火墙创建后，能够以证书 SSH 到云主机中；
  * 不能 PING 通云主机。

> ###### 说明：
> EayunStack 环境中默认不允许 SSH 到云主机中。

## 在已有的防火墙策略中插入防火墙规则

* 前提：

  * 已经创建了一个防火墙规则 "enable-ssh"；
  * 环境中的安全组策略允许 PING 和 SSH 的操作；
  * 环境中已经创建一台云主机，这台云主机分配了外网地址，能够被 PING 通；
  * 环境中的防火墙设置为能够 PING 通云主机 (即上述防火墙策略 "policy1")；
  * 用户已经登录到 EayunStack 管理界面中。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项，点击 【Network】 子选项，点击其中的 【Firewalls】；
  1. 点击右侧列表中的 【Firewall Policies】 标签，选择策略 "policy1"，点击 【Actions】 中的 【Insert Rule】；
  1. 在弹出的 【Insert Rule to Policy】 窗口中，选择 Insert Rule 为 "enable-ssh"，选择 Before 为 "enable-ping"；
  1. 点击窗口下方的 【Save Changes】 按钮。

* 预期结果：

  * 防火墙规则插入成功，防火墙状态为 "ACTIVE"；
  * 在规则插入之前，云主机可以被 PING 通，但不允许 SSH；
  * 防火墙规则插入之后，可以通过证书 SSH 到云主机上。

## 创建指定目标路由的防火墙

* 前提：

  * 租户中有 2 个路由 "router_01" 和 "router_02"；
  * 租户的 2 个网络 "net_01" 和 "net_02" 的子网 "subnet_01" 和 "subnet_02" 分别连接到 2 个路由上；
  * 租户的安全组允许 PING 的操作；
  * 创建了 2 台云主机 "instance_01" 和 "instance_02"，分别为云主机分配了浮动 IP，分别为 "ip_01" 和 "ip_02"。

* 操作：

  1. PING "instance_01" 和 "instance_02" 的浮动 IP，都能 PING 通；
  1. 登录到 Dashboard，点击 【Project】 下的 【Network】 选项，选择 【Firewalls】 选项；
  1. 在右侧的 Firewalls 列表中，点击 【Firewall Rules】 标签，点击右上角的 【+Add Rule】 按钮；
  1. 在弹出的 【Add Rule】 对话框中，输入名称为 "deny_icmp"，选择 Protocol 为 "ICMP"，Action 为 "DENY"；勾选 "Enabled"，启用规则；
  1. 点击对话框右下角的 【Add】 按钮，创建防火墙规则；
  1. 点击列表中的 【Firewall Policies】 标签，点击右上角的 【Add Policy】 按钮；
  1. 在弹出的 【Add Policy】 对话框的 【AddPolicy】 标签下，输入策略名称为 "policy_01"；点击 【Rules】 标签，从 "Available Rules" 中选择 "deny_icmp" 规则；
  1. 点击对话框右下角的 【Add】 按钮，创建防火墙策略；
  1. 登录 Controller 节点；
  1. 执行命令，创建指定目标路由为 router_01 的防火墙：

    ```
    (controller)# neutron firewall-create --name firewall-with-router01 policy --fw_target_routers list=true [ROUTER_01_ID]
    ```
  1. 再次 PING "instance_01" 和 "instance_02" 的浮动 IP。

* 预期结果：

  * 创建防火墙之前，可以 PING 通 "instance_01" 和 "instance_02"；
  * 指定目标路由为 router_01 的防火墙创建成功：

    ```
    (controller)# neutron firewall-create --name firewall-with-router01 policy --fw_target_routers list=true 169e460d-16ff-4c25-bd2a-47250772541c
    Created a new firewall:
    +--------------------+--------------------------------------+
    | Field              | Value                                |
    +--------------------+--------------------------------------+
    | admin_state_up     | True                                 |
    | description        |                                      |
    | firewall_policy_id | aa1fd2ff-4e94-46f6-92f1-5a9d7e393604 |
    | fw_target_routers  | 169e460d-16ff-4c25-bd2a-47250772541c |
    | id                 | 2635f3e0-fe81-428f-ac69-0b6c2e1bb564 |
    | name               | firewall-with-router01               |
    | status             | PENDING_CREATE                       |
    | tenant_id          | 7f67af7413074a85b751eaf997d59ae7     |
    +--------------------+--------------------------------------+
    ```
  * 防火墙创建完成后，PING "instance_01"，无法 PING 通；PING "instance_02"，可以 PING 通。

## 更新防火墙的目标路由表

* 前提：

  * 租户中有 2 个路由 "router_01" 和 "router_02"；
  * 租户的 2 个网络 "net_01" 和 "net_02" 的子网 "subnet_01" 和 "subnet_02" 分别连接到 2 个路由上；
  * 租户的安全组允许 PING 的操作；
  * 创建了 2 台云主机 "instance_01" 和 "instance_02"，分别为云主机分配了浮动 IP，分别为 "ip_01" 和 "ip_02"；
  * 创建了指定目标路由为 "router_01" 的防火墙。

* 操作：

  1. PING "instance_01" 和 "instance_02"，其中，"instance_01" 无法 PING 通，"instance_02" 可以 PING 通；
  1. 执行命令，将防火墙更新为指定目标路由为 "router_02"：

    ```
    (controller)# neutron firewall-update [FW_ID] --fw_target_routers list=true [ROUTER_02_ID]
    ```
  1. 再次 PING "instance_01" 和 "instance_02"。

* 预期结果：

  * 更新防火墙路由表之前，无法 PING 通 "instance_01"，可以 PING 通 "instance_02"；
  * 防火墙更新成功，防火墙的 fw_target_routers 中显示路由表为 "router_02"：

    ```
    (controller)# neutron firewall-update 2635f3e0-fe81-428f-ac69-0b6c2e1bb564 --fw_target_routers list=true e3dfd77e-e863-4d36-bb37-a7fcadfa48f7
    Updated firewall: 2635f3e0-fe81-428f-ac69-0b6c2e1bb564

    (controller)# neutron firewall-show 2635f3e0-fe81-428f-ac69-0b6c2e1bb564
    +--------------------+--------------------------------------+
    | Field              | Value                                |
    +--------------------+--------------------------------------+
    | admin_state_up     | True                                 |
    | description        |                                      |
    | firewall_policy_id | aa1fd2ff-4e94-46f6-92f1-5a9d7e393604 |
    | fw_target_routers  | e3dfd77e-e863-4d36-bb37-a7fcadfa48f7 |
    | id                 | 2635f3e0-fe81-428f-ac69-0b6c2e1bb564 |
    | name               | firewall-with-router01               |
    | status             | ACTIVE                               |
    | tenant_id          | 7f67af7413074a85b751eaf997d59ae7     |
    +--------------------+--------------------------------------+
    ```
  * 防火墙更新完成后，PING "instance_01"，可以 PING 通；PING "instance_02"，无法 PING 通。

## 清空防火墙的目标路由表

  * 租户中有 2 个路由 "router_01" 和 "router_02"；
  * 租户的 2 个网络 "net_01" 和 "net_02" 的子网 "subnet_01" 和 "subnet_02" 分别连接到 2 个路由上；
  * 租户的安全组允许 PING 的操作；
  * 创建了 2 台云主机 "instance_01" 和 "instance_02"，分别为云主机分配了浮动 IP，分别为 "ip_01" 和 "ip_02"；
  * 创建了指定目标路由为 "router_01" 的防火墙。

* 操作：

  1. PING "instance_01" 和 "instance_02"，其中，"instance_01" 无法 PING 通，"instance_02" 可以 PING 通；
  1. 执行命令，清空防火墙的目标路由表：

    ```
    (controller)# neutron firewall-update [FW_ID] --fw_target_routers action=clear
    ```
  1. 再次 PING "instance_01" 和 "instance_02"。

* 预期结果：

  * 清空防火墙路由表成功，防火墙的 fw_target_routers 显示路由表为空：

    ```
    (controller)# neutron firewall-update 2635f3e0-fe81-428f-ac69-0b6c2e1bb564 --fw_target_routers action=clear
    Updated firewall: 2635f3e0-fe81-428f-ac69-0b6c2e1bb564

    (controller)# neutron firewall-show 2635f3e0-fe81-428f-ac69-0b6c2e1bb564
    +--------------------+--------------------------------------+
    | Field              | Value                                |
    +--------------------+--------------------------------------+
    | admin_state_up     | True                                 |
    | description        |                                      |
    | firewall_policy_id | aa1fd2ff-4e94-46f6-92f1-5a9d7e393604 |
    | fw_target_routers  |                                      |
    | id                 | 2635f3e0-fe81-428f-ac69-0b6c2e1bb564 |
    | name               | firewall-with-router01               |
    | status             | ACTIVE                               |
    | tenant_id          | 7f67af7413074a85b751eaf997d59ae7     |
    +--------------------+--------------------------------------+
    ```
  * 清空防火墙目标路由表后，防火墙作用于整个租户，"instance_01" 和 "instance_02" 均无法 PING 通。
