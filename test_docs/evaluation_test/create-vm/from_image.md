# 从镜像创建云主机

## 创建 Linux 云主机

* 前提：

  * 环境中已经有一个 Linux 镜像；
  * 环境中已经创建提供给给云主机用的内网租户网络；
  * 用户登录到 OpenStack 的管理界面。

* 操作：

  1. 点击左侧导航栏的 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Instances】 选项；
  1. 在右侧将列出该租户的云主机列表，点击列表右上角的 【Launch Instance】 按钮；
  1. 在弹出的【Launch Instance】 窗口中，在 Details 标签下，选择 Availability Zone 为 "nova"；
  1. 填写 Instance Name 为 "centos_vm"，选择 Flavor 为 "m1.small"，输入 Instance Count 为 "1"；
  1. 在 Instance Boot Source 处选择 "Boot from image"，从镜像启动云主机，在下方出现的 Image 中选择 "centos-7.0-x86_64" 镜像；
  1. 在 Access & Security 标签下，在 Key Pair 处点击下拉按钮，选择密钥对，勾选 Security Groups "default"；
  1. 在 Networking 标签下，点击网络 "net04" 后的 【+】 图标，为云主机选择该网络；
  1. 其他配置保持默认，点击窗口下方的 【Launch Instance】 按钮。

* 预期结果：

  * 云主机成功创建；
  * 云主机状态变为 "Active" 后，可以打开控制台查看云主机；
  * 为云主机分配了 IP 地址，可以通过 SSH 的方式连接到云主机中。

## 创建 Windows 云主机

### 将 Windows ISO 作为镜像创建

* 前提：

  * 将 Windows ISO 上传至 Glance 作为镜像；
  * 环境中已经创建提供给云主机使用的内网租户网络。

* 操作：

  1. 登录 Controller 节点；
  1. 执行命令，创建 Windows 云主机：

    ```
    (controller)# nova boot --flavor m1.small --image WINDOWS_ISO_ID --block-device source=blank,dest=volume,bus=ide,type=disk,size=10,bootindex=1 eayun-windows
    ```
  1. 登录到 OpenStack 管理界面，点击左侧导航栏的 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Instances】 选项；
  1. 在右侧列出的云主机列表中，点击所创建的 Windows 云主机的名称，进入详细信息页面，点击 【Console】 选项卡，打开控制台；
  1. 根据提示操作安装系统。

* 预期结果：

  * 云主机成功创建；
  * 云主机状态变为 "Active" 后，可以打开控制台查看云主机并安装操作系统；
  * 操作系统安装成功，登录后可以使用。

### 将 Windows ISO 和 virtio ISO 作为镜像创建

* 前提：

  * 分别上传 Windows ISO 和 virtio ISO 至 Glance 作为镜像：

    ```
    (controller)# glance image-create --name <windows iso name> --disk-format iso --container-format bare --file <windows iso file location> --progress
    (controller)# glance image-create --name <virtio iso name> --disk-format iso --container-format bare --file <virtio iso file location> --progress
    ```
  * 环境中已经创建提供给云主机使用的内网租户网络。

* 操作：

  1. 登录 Controller 节点；
  1. 执行命令，创建 Windows 云主机：

    ```
    (controller)# nova boot --flavor m1.small --image WINDOWS_ISO_ID --block-device source=image,dest=volume,id=VIRTIO_ISO_ID,bus=ide,type=cdrom,size=1,bootindex=1 --block-device source=blank,dest=volume,bus=virtio,type=disk,size=10,bootindex=2 eayun-windows-with-virtio
    ```
  1. 登录 OpenStack 管理界面，点击左侧导航栏的 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Instances】 选项；
  1. 在右侧列出的云主机列表中，点击所创建的 Windows 云主机的名称，进入详细信息页面，点击 【Console】 选项卡，打开控制台；
  1. 根据提示操作安装系统。

* 预期结果：

  * 云主机成功创建；
  * 云主机状态变为 "Active" 后，可以打开控制台查看云主机并安装操作系统；
  * 根据提示可成功安装操作系统，登录后可以使用。
