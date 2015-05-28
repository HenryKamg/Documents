# 删除租户网络

* 前提：

  * 没有实例或其他服务在使用该租户网络；
  * 以 **eayun_member** 身份登录到 OpenStack 管理界面。

* 操作：

  1. 点击左侧导航栏的 【Projrct】 选项卡，点击 【Network】 子选项卡, 点击 【Networks】 子选项卡；
  1. 右侧将显示 Networks 列表，选择讲要删除的网络 "eayun_network"，点击 【Actions】 中的 【Delete Network】；
  1. 弹出 【Confirm Delete Network】 窗口，点击窗口下方的 【Delete Network】 按钮，确认删除。

* 预期结果：

  * "eayun_network" 网络被删除；
  * "eayun_network" 的子网也被删除。
