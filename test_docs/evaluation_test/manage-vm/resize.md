# 重新定义云主机大小

## 将从镜像启动的云主机 Resize

* 前提：

  * 环境中有至少 2 种 Flavor；
  * 环境配额足够；
  * 用户已经登录到 OpenStack 环境中。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Instances】 选项；
  1. 在右侧将列出该租户的云主机列表，选择一台使用 "m1.small" 类型创建的云主机，点击 【Actions】 中的 【Resize Instance】；
  1. 弹出 【Resize Instance】 窗口，在 Flavor Choice 标签下的 New Flavor 中选择一个大于 "m1.small" 的类型，如 "m1.medium"；
  1. 其他保持默认配置，点击窗口下方的 【Save】 按钮。

* 预期结果：

  * 云主机重新定义大小成功；
  * 重新定义大小后，需要确认：
    * 若点击 【Actions】 中的 【Confirm Resize/Migrate】 按钮，确认后，云主机以新的大小运行；
    * 若点击 【Actions】 中的 【Revert Resize/Migrate】 可以还原配置，撤销重新定义的操作，云主机还原。
  * 访问云主机，。。。

## 将从卷启动的云主机 Resize
