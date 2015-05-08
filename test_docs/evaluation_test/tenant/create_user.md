# 创建用户

## 创建管理员用户并添加到项目

* 前提：

  以 **Admin** 身份登录到 OpenStack 管理界面。

* 操作：

  1. 点击左侧导航栏的 【Identity】 选项卡，点击 【Users】 子选项卡；
  1. 右侧将显示 Users 列表，点击列表右上方的 【Create User】 按钮；
  1. 在弹出的 【Create User】 窗口中，填写 User Name 为 "eayun_admin"，Email 为 "eayun_admin@localhost"，Password 设置为需要设置的 eayun_admin 用户的密码，并在 Confirm Password 处再次填写密码；
  1. 在 Primary Project 中选择该用户的主项目为 "eayunstack"，Role 设置为 "admin"；
  1. 设置完成后，点击窗口下方的 【Create User】 按钮。

* 预期结果：

  * 用户成功创建；
  * "eayun_admin" 拥有管理员权限；
  * "eayunstack" 为 "eayun_admin" 的主项目。

## 创建成员用户

* 前提：

  以 **Admin** 身份登录到 OpenStack 管理界面。

* 操作：

  1. 点击左侧导航栏的 【Identity】 选项卡，点击 【Users】 子选项卡；
  1. 右侧将显示 Users 列表，点击列表右上方的 【Create User】 按钮；
  1. 在弹出的 【Create User】 窗口中，填写 User Name 为 "eayun_member"，Email 为 "eayun_member@localhost"，Password 设置为需要设置的 eayun_admin 用户的密码，并在 Confirm Password 处再次填写密码；
  1. 在 Primary Project 中选择该用户的主项目为 "eayunstack"，Role 设置为 "_member_"；
  1. 设置完成后，点击窗口下方的 【Create User】 按钮。

* 预期结果：

  * 用户成功创建；
  * "eayun_member" 拥有成员权限；
  * "eayunstack" 是 "eayun_member" 的主项目。

