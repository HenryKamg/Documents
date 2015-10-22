# SSH 访问云主机

* 前提：

  * 创建云主机之前，创建了 keypair，用于作为 SSH 登录的密钥证书：

    1. 登录到 OpenStack 管理界面；
    1. 点击左侧导航栏的 【Project】 选项卡，点击 【Compute】 子选项卡，点击其中的 【Access & Security】；
    1. 在右侧列表中的右上方点击 【Create Key Pair】 按扭，在弹出的 【Create Key Pair】 窗口中输入密钥对的名称，点击窗口下方的 【Create Key Pair】 按扭，创建密钥对；
    1. 创建成功后，将弹出下载密钥证书的窗口，将其下载到本地。
  * 创建的云主机指定了上述创建的 keypair；
  * 该用户设置的防火墙允许 SSH 操作。

* 操作：

  1. 在本地打开终端，执行下列命令：

    ```
    # ssh -i <PATH_TO_PEM> username@ip
    ```
  1. 其中 'PATH_TO_PEM' 为之前下载的 pem 证书的路径，'username' 为云主机的登录用户名，'ip' 为云主机的 IP 地址。

* 预期结果：

  * 成功以指定用户名登录到云主机。

> #### 注意：
> * 目前没有提供向已有云主机添加 keypair 的操作，因此，在创建云主机时需要指定 keypair 才能使用 SSH 访问功能。
