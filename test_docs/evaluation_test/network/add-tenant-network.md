# 创建租户网络

* 前提：

  以 **eayun_member** 身份登录到 OpenStack 管理界面。

* 操作：

  1. 点击左侧导航栏的 【Projrct】 选项卡，点击 【Network】 子选项卡, 点击 【Networks】 子选项卡；
  1. 右侧将显示 Networks 列表，点击 【+Create Network】 按钮；
  1. 弹出 【Create Network】 窗口，填写 Network Name 为 eayun-pri, Admin State 保留默认为 **UP**, 点击【Next】;
  1. 在新的编辑窗口中, 勾选 **Create Subnet**, 填写 Subnet Name 为 eayun-pri-sub, Network Address 填写为一段没有使用的私网地址比如 172.18.0.0/24, 其它保持默认, 点击【Next】;
  1. 在新的编辑窗口中, 勾选 **Enable DHCP**, 在 Allocation Pools 框中填写 172.18.0.100,172.18.0.254, 其它保持默认, 点击【Create】;

* 预期结果：

  * 租户网络创建成功；
  * 所创建的租户网络显示在 Networks 列表中。
