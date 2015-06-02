# 负载均衡

## 为云主机创建负载均衡

* 前提：

  * 安全组策略允许 HTTP 连接；
  * 防火墙允许 HTTP 连接；
  * 已经创建好 2 台 CentOS 7 的云主机 server-1 和 server-2，server-1 和 server-2 在同一个子网中(如：192.168.0.0/24)；
  * 2 台云主机在其中安装了 httpd，启动并设置为随系统启动；
  * 2 台云主机的 httpd 主页分别设置为 "I am server-1" 和 "I am server-2"；
  * 登录到 EayunStack 管理界面。

* 操作：

  1. 点击左侧导航栏中的 【Project】 选项，点击 【Network】 子选项，点击其中的 【Load Balancers】；
  1. 点击 【Pools】 标签，创建 pool：

    1. 点击列表上方的 【Add Pool】 按钮，在弹出的 【Add Pool】 窗口中，填写 Name 为 "server-pool"，Provider 保持默认 "haproxy"；
    1. 选择 Subnet 为 server-1 和 server-2 所在的子网地址："192.168.0.0/24"；
    1. 选择 Protocol 为 HTTP；
    1. 选择 Load Balancing Method 为 "ROUND_ROBIN"；
    1. 其他保持默认配置，点击窗口下方的 【Add】 按钮；

  1. 点击 【Members】 标签，添加 members：

    1. 点击列表上方的 【Add Member】 按钮，在弹出的 【Add Member】 窗口中，选择 Pool 为 "server-pool"；
    1. 选择 Member Source 为 "Select from active instances"，Member(s) 中选择 "server-1" 和 "server-2"；
    1. Weight 填写为 "1"，Protocol Port 填写 "80"；
    1. 点击窗口下方的 【Add】 按钮；

  1. 点击 【Pools】 标签，添加 vip：

    1. 选择 "server-pool"，点击 【Actions】 中的 【Add VIP】；
    1. 在弹出的 【Add VIP】 窗口中，填写 Name 为 "server-vip"，选择 VIP Subnet 为 server-1 和 server-2 所使用的子网："192.168.0.0/24"；
    1. 在 Specify a free IP address from the selected subnet 处填写子网中的某一个未被使用的 IP 地址，如："192.168.0.253"；
    1. 填写 Protocol Port 为 "80"，选择 Protocol 为 "HTTP"；
    1. 其他保持默认配置，点击窗口下方的 【Add】 按钮；

  1. 分配 Floating IP：

    1. 点击左侧导航栏的 【Project】 选项下的 【Compute】 子选项，点击 【Access & Securiry】 选项；
    1. 点击右侧列表中的 【Floating IPs】 标签，选择一个可用的浮动 IP 地址，如："25.0.0.253"，点击 【Actions】 中的 【Associate】；
    1. 在弹出的 【Manage Floating IP Associations】 窗口中，选择 Port to be associated 为 "None: 192.168.0.253"，即在 VIP 中所使用的地址；
    1. 点击窗口下方的 【Associate】 按钮。

* 预期结果：

  * 为云主机成功创建负载均衡服务；
  * 使用浏览器打开地址 "25.0.0.253"，可以访问 server-1 的 httpd 主页，显示 "I am server-1"；
  * 刷新页面，访问到 server-2 的 httpd 主页，显示 "I am server-2"。

## 为云主机的负载均衡添加 Monitor

* 前提：

  * 已经为云主机配置好负载均衡服务 (本实验使用上述所配置的负载均衡服务)；
  * 安全组策略允许 HTTP 连接；
  * 防火墙规则允许 HTTP 连接；
  * 登录到 EayunStack 管理界面。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项，点击 【Network】 子选项，点击其中的 【Load Balancers】；
  1. 在右侧列表中，点击 【Monitors】 标签，点击列表上方的 【Add Monitor】 按钮；
  1. 在弹出的 【Add Monitor】 窗口中，选择 Type 为 "HTTP"，Delay 填写为 "60"，Timeout 填写为 "15"，Max Retries 填写为 "2"；
  1. 其他保持默认配置，点击窗口下方的 【Add】 按钮；
  1. 点击 【Pools】 标签，选择 "server-pool"，点击 【Actions】 中的 【Associate Monitor】；
  1. 在弹出的 【Associate Monitor】 窗口中，选择 Monitor 为上述所创建的 monitor，点击窗口下方的 【Associate】 按钮。

* 预期结果：

  * 为云主机的负载均衡添加 Monitor 成功；
  * 登录到 Controller 节点，执行命令：

      ```
      neutron lb-pool-stats 09a7c3f2-3057-4e9c-bfbf-9b1ab7f2a0b1
      +--------------------+-------+
      | Field              | Value |
      +--------------------+-------+
      | active_connections | 0     |
      | bytes_in           | 0     |
      | bytes_out          | 0     |
      | total_connections  | 0     |
      +--------------------+-------+ 
      ```

  * 使用浏览器打开地址 "25.0.0.253"，刷新几次，再次执行命令：

      ```
      neutron lb-pool-stats 09a7c3f2-3057-4e9c-bfbf-9b1ab7f2a0b1
      +--------------------+-------+
      | Field              | Value |
      +--------------------+-------+
      | active_connections | 0     |
      | bytes_in           | 4430  |
      | bytes_out          | 2540  |
      | total_connections  | 10    |
      +--------------------+-------+ 
      ```

  * 看到数据更新，对 HTTP 的数据进行监控。


## 删除云主机的负载均衡的 Monitor

* 前提：

  * 已经为云主机配置好负载均衡服务 (本实验使用上述所配置的负载均衡服务) 并添加了 Monitor；
  * 安全组策略允许 HTTP 连接；
  * 防火墙规则允许 HTTP 连接；
  * 登录到 EayunStack 管理界面。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项，点击 【Network】 子选项，点击其中的 【Load Balancers】；
  1. 在右侧列表中点击 【Pools】 标签，选择 "server-pool"，点击 【Actions】 中的 【Disassociate Monitor】；
  1. 在弹出的 【Disassociate Monitor】 窗口中，选择要取消分配的 Monitor，即上述所添加的 Monitor，点击窗口下方的 【Disassociate】 按钮。

* 预期结果：

  * 云主机负载均衡服务的 Monitor 成功被删除；
  * 使用浏览器打开地址 "25.0.0.253"，刷新几次后，执行命令：

      ```
      neutron lb-pool-stats 09a7c3f2-3057-4e9c-bfbf-9b1ab7f2a0b1
      +--------------------+-------+
      | Field              | Value |
      +--------------------+-------+
      | active_connections | 0     |
      | bytes_in           | 0     |
      | bytes_out          | 0     |
      | total_connections  | 0     |
      +--------------------+-------+ 
      ```

  * 看到数据被清除，不再监控 HTTP 的数据。
