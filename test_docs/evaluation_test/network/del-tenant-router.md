# 删除租户网络

* 前提：

  - 以 **eayun_member** 身份登录到 OpenStack 管理界面。
  - 租户网络 **eayun-pri** 和 **eayun-pri-sub** 存在
  - 租户路由 **eayun-router** 存在
  - 已为租户路由设置了网关, 并把 eayun-pri-sub 增加到路由中

* 操作：

  1. 点击左侧导航栏的 【Projrct】 选项卡，点击 【Network】 子选项卡, 点击 【Routers】 子选项卡；
  1. 在 【Routers】 设置界面，点击 eayun-router，进入 【Router Details】 界面；
  1. 在 【Interfaces】列表，点击所有勾选 Interface，点击右上角的 【Delete Interfaces】按钮，删除 Intrefaces；
  1. 在 【Router Details】 界面，点击 【Clear Gateway】，删除 Gateway；
  1. 回到左侧导航栏的 【Projrct】 选项卡，点击 【Network】 子选项卡，点击 【Routers】 子选项卡，进入 【Routers】 界面；
  1. 选中 eayun-router，点击 【Delete Routers】，删除路由。

* 预期结果：

  该租户路由被成功删除。
