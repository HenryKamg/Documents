# 重新构建云主机

## 将 Linux 云主机重新构建为其他 Linux 操作系统

* 前提：

  * 环境中至少有 2 个 Linux 镜像；
  * 云主机所使用的 Flavor 适合所选择的镜像；
  * 用户已经登录到 OpenStack 管理环境中。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Instances】 选项；
  1. 在右侧将列出该租户的实例列表，选择一台使用 "centos-7.0-x86_64" 镜像创建的云主机，点击 【Actions】 中的 【Rebuild Instance】；
  1. 弹出 【Rebuild Instance】 窗口，在 Select Image 处选择 "ubuntu-14.04-x86_64" 镜像；
  1. 其他保持默认配置，点击窗口下方的 【Rebuild Instance】 按钮。

* 预期结果：

  * 云主机重新构建成功；
  * 新的云主机以 Ubuntu14.04 系统启动；
  * 新的云主机与原云主机有相同的 ID 和网络。

> #### 注意：
> * 云主机所使用的 Flavor 必须适用于 ubuntu-14.04-x86_64 这个镜像，否则重新构建云主机失败，云主机不会被重新构建；
> * 若 Flavor 不合适，可以先 resize 后，再进行 rebuild 操作。


## 将 Windows 云主机重新构建为其他 Windows 操作系统

* 前提：

  * 环境中至少有 2 个 Windows 镜像；
  * 云主机所使用的 Flavor 适合所选择的镜像；
  * 用户已经登录到 OpenStack 管理环境中。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Instances】 选项；
  1. 在右侧将列出该租户的实例列表，选择一台使用 "..." 镜像创建的云主机，点击 【Actions】 中的 【Rebuild Instance】；
  1. 弹出 【Rebuild Instance】 窗口，在 Select Image 处选择 "..." 镜像；
  1. 其他保持默认配置，点击窗口下方的 【Rebuild Instance】 按钮。

* 预期结果：

  * 云主机重新构建成功；
  * 新的云主机以 ... 系统启动；
  * 新的云主机与原云主机有相同的 ID 和网络。

> #### 注意：
> * 云主机所使用的 Flavor 必须适用于 ... 这个镜像，否则重新构建云主机失败，云主机不会被重新构建；
> * 若 Flavor 不合适，可以先 resize 后，再进行 rebuild 操作。


## 将 Linux 云主机重新构建为 Windows 操作系统

* 前提：

  * 环境中至少有 1 个 Windows 镜像；
  * 云主机所使用的 Flavor 适合所选择的镜像；
  * 用户已经登录到 OpenStack 管理环境中。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Instances】 选项；
  1. 在右侧将列出该租户的实例列表，选择一台使用 "centos-7.0-x86_64" 镜像创建的云主机，点击 【Actions】 中的 【Rebuild Instance】；
  1. 弹出 【Rebuild Instance】 窗口，在 Select Image 处选择 "..." 镜像；
  1. 其他保持默认配置，点击窗口下方的 【Rebuild Instance】 按钮。

* 预期结果：

  * 云主机重新构建成功；
  * 新的云主机以 ... 系统启动；
  * 新的云主机与原云主机有相同的 ID 和网络。

> #### 注意：
> * 云主机所使用的 Flavor 必须适用于 ... 这个镜像，否则重新构建云主机失败，云主机不会被重新构建；
> * 若 Flavor 不合适，可以先 resize 后，再进行 rebuild 操作。


## 将 Windows 云主机重新构建为 Linux 操作系统

* 前提：

  * 环境中至少有 1 个 Windows 镜像；
  * 云主机所使用的 Flavor 适合所选择的镜像；
  * 用户已经登录到 OpenStack 管理环境中。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Instances】 选项；
  1. 在右侧将列出该租户的实例列表，选择一台使用 "..." 镜像创建的云主机，点击 【Actions】 中的 【Rebuild Instance】；
  1. 弹出 【Rebuild Instance】 窗口，在 Select Image 处选择 "centos-7.0-x86_64" 镜像；
  1. 其他保持默认配置，点击窗口下方的 【Rebuild Instance】 按钮。

* 预期结果：

  * 云主机重新构建成功；
  * 新的云主机以 Centos7.0 系统启动；
  * 新的云主机与原云主机有相同的 ID 和网络。

> #### 注意：
> * 云主机所使用的 Flavor 必须适用于 centos-7.0-x86_64 这个镜像，否则重新构建云主机失败，云主机不会被重新构建；
> * 若 Flavor 不合适，可以先 resize 后，再进行 rebuild 操作。

