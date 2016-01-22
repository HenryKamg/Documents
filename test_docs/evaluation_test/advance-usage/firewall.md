# 防火墙服务

## 创建允许 PING 操作的防火墙

* 前提：

  * 环境中还未创建防火墙；
  * 环境中的安全组策略允许 PING 和 SSH 的操作；
  * 环境中已经创建了一台云主机，这台云主机分配了外网地址，本应能够被 PING 通；
  * 用户已经登录到 EayunStack 管理界面。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项，点击 【Network】 子选项，点击其中的 【Firewalls】；
  1. 在右侧列表中，点击 【Firewall Rules】 标签；
  1. 点击列表上方的 【Add Rule】 按钮，在弹出的 【Add Rule】 窗口中：

    * 填写 Name 为 "enable-ping"；
    * 选择 Protocol 为 "ICMP"；
    * 选择 Action 为 "ALLOW"；
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
  * 创建防火墙之前，无法 PING 通云主机；
  * 防火墙创建后，可以 PING 通云主机。

> ###### 说明：
> EayunStack 环境中默认不允许 PING 云主机。

## 创建允许 SSH 操作的规则并添加到防火墙策略中

* 前提：

  * 环境中已经创建防火墙；
  * 环境中的安全组策略允许 PING 和 SSH 的操作；
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

TODO

## 更新防火墙的目标路由表

TODO

## 清空防火墙的目标路由表

TODO
