# 创建租户

* 前提：

  以 **Admin** 身份登录到 OpenStack 的管理界面。

* 操作：

  1. 点击左侧导航栏的 【Identity】 选项卡，点击 【Projects】 子选项卡；
  1. 右侧将显示 Projects 列表，点击列表右上角的 【Create Project】 按钮；
  1. 在弹出的 【Create Project】 窗口中，在 【Project Information】 标签下，填写 Name 为 "eayunstack"，Description 中填写 "EayunStack org"，Enable 默认勾选；
  1. 点击 【Quota】 标签，设置项目的配额，如下：

    * *Metadata Items*: -1
    * *VCPUs*: 20
    * *Instance*: 100
    * *Injected Files*: -1
    * *Injected Files Content (Bytes)*: -1
    * *Volumes*: 10
    * *Volume Snapshots*: 10
    * *Total Size of Volumes and Snapshots (GB)*: 1000
    * *RAM (MB)*: 20480
    * *Security Groups*: 100
    * *Security Group Rules*: 1000
    * *Floating IPs*: 500
    * *Networks*: 100
    * *Ports*: 500
    * *Routers*: 100
    * *Subnets*: 100

  1. 设置完成后，点击窗口下方的 【Create Project】 按钮。

* 预期结果：

  * 租户成功创建；
  * 租户的配额以上述数值设置成功；
  * 由于没有为租户分配用户，该租户是没有用户的，无法登录。

> ##### 注意：
> 租户管理的操作只有管理员可以进行，因此必须以 **Admin** 身份登录。
