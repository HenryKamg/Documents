# 删除云主机

* 前提：

  * 用户是 admin 角色，或登录的用户从属于要删除的云主机所在的项目，本实验属于后者；
  * 用户登录到 OpenStack 管理界面。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Instances】 选项；
  1. 在右侧将列出该租户的云主机列表，选择要删除的云主机，点击云主机后的 【Actions】 中的 【Terminate Instance】；
  1. 弹出 【Confirm Terminate Instance】 窗口，点击窗口下方的 【Terminate Instance】 按钮，确认删除。

* 预期结果：

  * 点击窗口下方的 【Terminate Instance】 按钮后，云主机被删除，有 Success 的信息提示；
  * 若点击了窗口下方的 【Cancel】 按钮，则取消删除，云主机不会被删除，保持原样。


