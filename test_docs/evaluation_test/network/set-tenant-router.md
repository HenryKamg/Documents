# 创建租户路由

* 前提：

  - 以 **eayun_member** 身份登录到 OpenStack 管理界面。
  - 租户网络 **eayun-pri** 和 **eayun-pri-sub** 存在
  - 租户路由 **eayun-router** 存在

* 操作：

  1. 点击左侧导航栏的 【Projrct】 选项卡，点击 【Network】 子选项卡, 点击 【Routers】 子选项卡；
  1. 右侧将显示 Routers 列表，点击 【Set Gateway】 按钮；
  1. 弹出 【Set Gateway】 窗口，在 External Network 下拉框, 选择可用的外部网络.
  1. 点击【Set Gateway】;
  1. 在 【 Routers 】 设置界面, 点击 eayun-router, 进入 【Router Details】界面;
  1. 点击界面中的 【 + Add Interface 】, 弹出 【Add Interface】窗口;
  1. 在 【Add Interface】 中, 点击 Select Subnet 下拉框, 选择 **eayun-pri: 172.16.18.0.0/24(eayun-pri-sub)**, 其它默认;
  1. 点击 【Add Interface】;

* 预期结果：

  在 【Router Details】界面显示增加的 Interface
