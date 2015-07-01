# 虚拟网络的工作性能

虚拟网络的工作性能使用 iperf 进行测试，通过 Rally 的辅助完成自动化测试。测试内容包括 TCP 和 UDP 的带宽质量测试。

## 测试准备：

  * 使用 CentOS-7.0-x86_64 镜像进行测试；
  * 由于侧重点在于网络性能，所准备的镜像需要安装 iperf (用于执行测试) 和 python-paramiko (用于向 Rally 服务器传输测试结果)；
  * 由于执行测试时需要 root 权限，镜像需要设置为默认 sudo 不需要 tty (Rally 的限制)；
  * 准备两台环境内的云主机作为 iperf 测试的服务器：

    在云主机中分别执行：

    ```
    # TCP 测试服务器：
    $ iperf -s -i 5

    # UDP 测试服务器：
    $ iperf -u -s -i 5
    ```

## 执行测试：

1. 登录到 Rally 测试服务器；
1. 使用 Rally 测试文件 [test_iperf.yaml](https://github.com/eayunstack/rally/blob/EayunStack_v1.0/use_rally/scenarions_with_args/vm/test_iperf.yaml)，测试文件中已指定对应的测试脚本；
1. 执行测试命令：`rally -d task start test_iperf.yaml`；
1. 测试执行结束后，执行以下命令获取测试结果：

  ```
  # 获取 html 格式的测试结果：
  # rally task report <task_uuid> --out /var/www/html/rally_report/vm/success/<file_name>.html

  # 获取 json 格式的测试结果：
  # rally task results <task_uuid> >> /var/www/html/rally_report/vm/success/<file_name>.json
  ```

1. 在云主机中执行脚本的直接输出将在 Rally 测试执行完成后保存在 Rally 服务器的 /tmp/ 目录下，文件名为 `/tmp/iperf_*`。

> ###### 说明：
> 本测试一次性执行 TCP 和 UDP 的测试，但并非同时执行，结果互不影响。

> ## 警告：
> 执行网络性能测试需要保证服务器端和客户端云主机运行在不同 Compute 节点上，而由于 Rally 的限制，需要临时修改 Nova 的配置，**测试时请联系研发人员**。

> ###### 注：
> 另外，可以直接在两台作为 iperf 测试服务器的云主机上直接观察到测试过程的输出信息。

> ###### 注：
> Rally 的测试结果输出到 /var/www/html/ 目录下后，可以直接通过浏览器输入 Rally 服务器 IP 地址，以打开测试结果。
