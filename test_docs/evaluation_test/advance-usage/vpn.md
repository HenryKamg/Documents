# VPN 服务

## 创建 VPN 服务

* 前提：

  * 环境中创建了两台处于不同网络的云主机 server-A 和 server-B (相互无法 PING 通)；
  * 环境中的安全组策略允许 PING 的操作；
  * 环境中的防火墙规则允许 PING 的操作；
  * 用户已经登录到 EayunStack 管理界面。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项，点击 【Network】 子选项，点击其中的 【VPN】；
  1. 在右侧列表中，点击 【IKE Policies】 标签，点击列表上方的 【Add IKE Policy】 按钮，在弹出的 【Add IKE Policy】 窗口中，填写 Name 为 "ike-policy1"；
  1. 其他保持默认配置，点击窗口下方的 【Add】 按钮，创建 IKE 策略；
  1. 点击 【IPSec Policies】 标签，点击列表上方的 【Add IPSec Policy】 按钮，在弹出的 【Add IPSec Policy】 窗口中，填写 Name 为 "ipsec-policy1"；
  1. 其他保持默认配置，点击窗口下方的 【Add】 按钮，创建 IPSec 策略；
  1. 点击 【VPN Services】 标签，点击列表上方的 【Add VPN Service】 按钮，在弹出的 【Add VPN Service】 窗口中：

    * 填写 Name 为 "vpn-service-A"；
    * 选择 Router 为 server-A 的路由 "router-A"；
    * 选择 Subnet 为 server-A 的子网 "172.16.102.0/24"；

  1. 其他保持默认配置，点击窗口下方的 【Add】 按钮，添加 server-A 所在子网的 VPN 服务；
  1. 再次点击列表上方的 【Add VPN Service】 按钮，在弹出的 【Add VPN Service】 窗口中：

    * 填写 Name 为 "vpn-service-B"；
    * 选择 Router 为 server-B 的路由 "router-B"；
    * 选择 Subnet 为 server-B 的子网 "172.16.103.0/24"；

  1. 其他保持默认配置，点击窗口下方的 【Add】 按钮，添加 server-B 所在子网的 VPN 服务；
  1. 点击 【IPSec Site Connections】 标签，点击列表上方的 【Add IPSec Site Connection】 按钮，在弹出的 【Add IPSec Site Connection】 窗口中：

    * 填写 Name 为 "connection-A_B"；
    * 选择 VPN Service associated with this connection 为 "vpn-service-A"；
    * 选择 IKE Policy associated with this connection 为 "ike-policy1"；
    * 选择 IPSec Policy associated with this connection 为 "ipsec-policy1"；
    * Peer gateway public IPv4/IPv6 Address or FQDN 中填写 **router-B** 的外网地址 "25.0.0.201"；
    * Peer router identity for authentication (Peer ID) 中填写 **router-B** 的外网地址 "25.0.0.201"；
    * Remote peer subnet(s) 中填写 **server-B** 的子网地址段 "172.16.103.0/24"；
    * Pre-Shared Key (PSK) string 中填写密码 "abc123"；

  1. 其他保持默认配置，点击窗口下方的 【Add】 按钮，创建 server-A 所在子网到 server-B 所在子网的 VPN 连接；
  1. 再次点击 【IPSec Site Connections】 标签，点击列表上方的 【Add IPSec Site Connection】 按钮，在弹出的 【Add IPSec Site Connection】 窗口中：

    * 填写 Name 为 "connection-B_A"；
    * 选择 VPN Service associated with this connection 为 "vpn-service-B"；
    * 选择 IKE Policy associated with this connection 为 "ike-policy1"；
    * 选择 IPSec Policy associated with this connection 为 "ipsec-policy1"；
    * Peer gateway public IPv4/IPv6 Address or FQDN 中填写 **router-A** 的外网地址 "25.0.0.200"；
    * Peer router identity for authentication (Peer ID) 中填写 **router-A** 的外网地址 "25.0.0.200"；
    * Remote peer subnet(s) 中填写 **server-A** 的子网地址段 "172.16.102.0/24"；
    * Pre-Shared Key (PSK) string 中填写密码 "abc123"；

  1. 其他保持默认配置，点击窗口下方的 【Add】 按钮，创建 server-B 所在子网到 server-A 所在子网的 VPN 连接。

* 预期结果：

  * 2 个 VPN 连接都创建好后，状态为 "Active"；
  * 点击进入 server-A 的控制台，登录后 PING server-B 的 IP 地址，能够 PING 通；
  * 点击进入 server-B 的控制台，登录后 PING server-A 的 IP 地址，能够 PING 通。


## 验证 VPN 之间是否能互通

* 前提：

  * 已经创建好 2 个网络之间的 VPN 连接 (本实验中使用上述 VPN 连接)；
  * 环境中创建了一台与上述示例不在同一个网络中的云主机 server-C；
  * 环境中的安全组策略允许 PING 的操作；
  * 环境中的防火墙规则允许 PING 的操作；
  * 用户已经登录到 EayunStack 管理界面。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项，点击 【Network】 子选项，点击其中的 【VPN】；
  1. 在右侧列表中点击列表上方的 【Add VPN Service】 按钮，在弹出的 【Add VPN Service】 窗口中：

    * 填写 Name 为 "vpn-service-C"；
    * 选择 Router 为 server-C 的路由 "router-C"；
    * 选择 Subnet 为 server-C 的子网 "172.16.104.0/24"；

  1. 其他保持默认配置，点击窗口下方的 【Add】 按钮，添加 server-C 所在子网的 VPN 服务；
  1. 点击 【IPSec Site Connections】 标签，点击列表上方的 【Add IPSec Site Connection】 按钮，在弹出的 【Add IPSec Site Connection】 窗口中：

    * 填写 Name 为 "connection-A_C"；
    * 选择 VPN Service associated with this connection 为 "vpn-service-A"；
    * 选择 IKE Policy associated with this connection 为 "ike-policy1"；
    * 选择 IPSec Policy associated with this connection 为 "ipsec-policy1"；
    * Peer gateway public IPv4/IPv6 Address or FQDN 中填写 **router-C** 的外网地址 "25.0.0.202"；
    * Peer router identity for authentication (Peer ID) 中填写 **router-C** 的外网地址 "25.0.0.202"；
    * Remote peer subnet(s) 中填写 **server-C** 的子网地址段 "172.16.104.0/24"；
    * Pre-Shared Key (PSK) string 中填写密码 "abc123"；

  1. 其他保持默认配置，点击窗口下方的 【Add】 按钮，创建 server-A 所在子网到 server-C 所在子网的 VPN 连接；
  1. 再次点击 【IPSec Site Connections】 标签，点击列表上方的 【Add IPSec Site Connection】 按钮，在弹出的 【Add IPSec Site Connection】 窗口中：

    * 填写 Name 为 "connection-C_A"；
    * 选择 VPN Service associated with this connection 为 "vpn-service-C"；
    * 选择 IKE Policy associated with this connection 为 "ike-policy1"；
    * 选择 IPSec Policy associated with this connection 为 "ipsec-policy1"；
    * Peer gateway public IPv4/IPv6 Address or FQDN 中填写 **router-A** 的外网地址 "25.0.0.200"；
    * Peer router identity for authentication (Peer ID) 中填写 **router-A** 的外网地址 "25.0.0.200"；
    * Remote peer subnet(s) 中填写 **server-A** 的子网地址段 "172.16.102.0/24"；
    * Pre-Shared Key (PSK) string 中填写密码 "abc123"；

  1. 其他保持默认配置，点击窗口下方的 【Add】 按钮，创建 server-C 所在子网到 server-A 所在子网的 VPN 连接。


* 预期结果：

  * 2 个 VPN 连接都创建好后，状态为 "Active"；
  * 点击进入 server-A 的控制台，登录后 PING server-C 的 IP 地址，能够 PING 通；
  * 点击进入 server-C 的控制台，登录后 PING server-A 的 IP 地址，能够 PING 通。
  * 点击进入 server-B 的控制台，登录后 PING server-C 的 IP 地址，不能够 PING 通；
  * 点击进入 server-C 的控制台，登录后 PING server-B 的 IP 地址，不能够 PING 通。

> ###### 说明：
> VPN 服务仅支持端到端的连接，因此 server-B 与 server-C 之间不能 PING 通。

## PPTP 服务

### 创建 PPTP 服务和证书

* 前提：

  * 确认 Neutron 支持 PPTP：

    ```
    (controller)# neutron service-provider-list
    +--------------+----------+---------+
    | service_type | name     | default |
    +--------------+----------+---------+
    | VPN          | pptp     | False   |
    | VPN          | openswan | True    |
    | LOADBALANCER | haproxy  | True    |
    +--------------+----------+---------+
    ```

* 操作：

  1. 登录 Controller 节点；
  1. 执行命令，创建 vpnservice：

    ```
    (controller)# neutron vpn-service-create --name [VPN_SERVICE_NAME] [ROUTER_ID] [SUBNET_ID] --provider pptp
    ```
  1. 创建 PPTP 证书：

    ```
    (controller)# neutron eayun-pptp-credential-create [USERNAME] [PASSWORD] --vpnservices list=true [VPNSERVICE_ID]
    ```

* 预期结果：

  * PPTP VPN 服务创建成功：

    ```
    (controller)# neutron vpn-service-create --name test-pptp-vpn 169e460d-16ff-4c25-bd2a-47250772541c 9a77f095-0697-4664-896a-36e2eba60be2 --provider pptp
    Created a new vpnservice:
    +----------------+--------------------------------------+
    | Field          | Value                                |
    +----------------+--------------------------------------+
    | admin_state_up | True                                 |
    | description    |                                      |
    | id             | ace6f0cf-f774-45aa-82a9-10366e7f7633 |
    | name           | test-pptp-vpn                        |
    | provider       | pptp                                 |
    | router_id      | 169e460d-16ff-4c25-bd2a-47250772541c |
    | status         | PENDING_CREATE                       |
    | subnet_id      | 9a77f095-0697-4664-896a-36e2eba60be2 |
    | tenant_id      | 7f67af7413074a85b751eaf997d59ae7     |
    +----------------+--------------------------------------+
    ```
  * PPTP 证书创建成功：

    ```
    (controller)# neutron eayun-pptp-credential-create test abc123 --vpnservices list=true ace6f0cf-f774-45aa-82a9-10366e7f7633
    Created a new pptp_credential:
    +-------------+--------------------------------------+
    | Field       | Value                                |
    +-------------+--------------------------------------+
    | id          | 5f403265-4ab7-4534-bb1f-882be4e100c8 |
    | password    | abc123                               |
    | tenant_id   | 7f67af7413074a85b751eaf997d59ae7     |
    | username    | test                                 |
    | vpnservices | ace6f0cf-f774-45aa-82a9-10366e7f7633 |
    +-------------+--------------------------------------+
    ```

### 更新 PPTP 证书密码

* 前提：

  * 确认 Neutron 支持 PPTP VPN 服务；
  * 已经创建了 PPTP VPN 证书。

* 操作：

  1. 列出当前证书：

    ```
    (controller)# neutron eayun-pptp-credential-list
    ```
  1. 执行命令，更新证书密码：

    ```
    (controller)# neutron eayun-pptp-credential-update [CREDENTIAL_ID] --password [NEW_PASSWORD]
    ```

* 预期结果：

  * 证书密码更新成功，命令行返回成功提示：
    ```
    (controller)# neutron eayun-pptp-credential-update 5f403265-4ab7-4534-bb1f-882be4e100c8 --password eayun123
    Updated pptp_credential: 5f403265-4ab7-4534-bb1f-882be4e100c8
    ```
  * 查看证书，看到密码被更新：

    ```
    (controller)# neutron eayun-pptp-credential-show 5f403265-4ab7-4534-bb1f-882be4e100c8
    +-------------+--------------------------------------+
    | Field       | Value                                |
    +-------------+--------------------------------------+
    | id          | 5f403265-4ab7-4534-bb1f-882be4e100c8 |
    | password    | eayun123                             |
    | tenant_id   | 7f67af7413074a85b751eaf997d59ae7     |
    | username    | test                                 |
    | vpnservices | ace6f0cf-f774-45aa-82a9-10366e7f7633 |
    +-------------+--------------------------------------+
    ```

### 更新 PPTP 证书的 vpnservice 列表

* 前提：

  * 确认 Neutron 支持 PPTP VPN 服务；
  * 已经创建了 PPTP VPN 服务和证书。

* 操作：

  1. 获取要更新到 PPTP 证书的 vpnservice 的 ID；
  1. 执行命令，更新 PPTP 证书的 vpnservice 列表：

    ```
    (controller)# neutron eayun-pptp-credential-update [CREDENTIAL_ID] --vpnservices list=true [VPNSERVICE_ID1] [VPNSERVICE_ID2]
    ```

* 预期结果：

  * 更新证书 vpnservice 列表成功，命令行返回成功提示：

    ```
    (controller)# neutron eayun-pptp-credential-update 5f403265-4ab7-4534-bb1f-882be4e100c8 --vpnservices list=true ace6f0cf-f774-45aa-82a9-10366e7f7633 fa409fdf-383c-4f61-ade5-330fa123102b
    Updated pptp_credential: 5f403265-4ab7-4534-bb1f-882be4e100c8
    ```
  * 查看证书，看到 vpnservice 列表被更新为指定的 vpnservice：

    ```
    (controller)# neutron eayun-pptp-credential-show 5f403265-4ab7-4534-bb1f-882be4e100c8
    +-------------+--------------------------------------+
    | Field       | Value                                |
    +-------------+--------------------------------------+
    | id          | 5f403265-4ab7-4534-bb1f-882be4e100c8 |
    | password    | eayun123                             |
    | tenant_id   | 7f67af7413074a85b751eaf997d59ae7     |
    | username    | test                                 |
    | vpnservices | ace6f0cf-f774-45aa-82a9-10366e7f7633 |
    |             | fa409fdf-383c-4f61-ade5-330fa123102b |
    +-------------+--------------------------------------+
    ```
  * 可以使用该证书连接到列表中的 vpnservice。

### 清空 PPTP 证书的 vpnservice 列表

* 前提：

  * 确认 Neutron 支持 PPTP VPN 服务；
  * 已经创建了 PPTP VPN 服务和证书。

* 操作：

  1. 登录 Controller 节点；
  1. 执行命令，清空 vpnservice 列表：

    ```
    (controller)# neutron eayun-pptp-credential-update [CREDENTIAL_ID] --vpnservices action=clear
    ```

* 预期结果：

  * PPTP 证书的 vpnservice 列表被清空，命令行返回成功提示：

    ```
    (controller)# neutron eayun-pptp-credential-update 5f403265-4ab7-4534-bb1f-882be4e100c8 --vpnservices action=clear
    Updated pptp_credential: 5f403265-4ab7-4534-bb1f-882be4e100c8
    ```
  * 查看证书，看到 vpnservice 列表被清空：

    ```
    (controller)# neutron eayun-pptp-credential-show 5f403265-4ab7-4534-bb1f-882be4e100c8
    +-------------+--------------------------------------+
    | Field       | Value                                |
    +-------------+--------------------------------------+
    | id          | 5f403265-4ab7-4534-bb1f-882be4e100c8 |
    | password    | eayun123                             |
    | tenant_id   | 7f67af7413074a85b751eaf997d59ae7     |
    | username    | test                                 |
    | vpnservices |                                      |
    +-------------+--------------------------------------+
    ```
  * 该证书无法连接到任何 vpnservice。
