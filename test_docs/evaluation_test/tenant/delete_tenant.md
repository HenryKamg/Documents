# 删除租户

* 前提：

  以 **Admin** 身份登录到 OpenStack 的管理界面。

* 操作：

  1. 点击左侧导航栏的 【Identity】 选项卡，点击 【Projects】 子选项卡；
  1. 在右侧的 Projects 列表中，选择项目 "eayunstack"，点击 【Actions】 下拉列表中的 【Delete Project】，或勾选 "eayunstack" 项目，点击列表右上角的 【Delete Projects】 按钮；
  1. 在弹出 【Confirm Delete Project】 确认框时，点击窗口下方的 【Delete Project】 按钮。

* 预期结果：

  * 项目被删除；
  * 属于该项目的用户不会被删除；
  * 如果该项目下的用户仅仅属于此项目，那么用户将无法登录到 OpenStack 界面。
