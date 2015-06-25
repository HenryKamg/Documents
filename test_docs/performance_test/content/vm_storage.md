# 虚拟存储的使用性能

EayunStack 允许云主机使用两种类型的存储：Ceph 和 Eqlx。

其性能有所不同，将分开进行测试。

虚拟存储的性能使用 fio 工具进行测试，通过 Rally 的辅助完成自动化测试。测试不同的 IO 和队列深度，对比性能的变化。

## 测试准备：

  * 使用 CentOS-7.0-x86_64 镜像进行测试；
  * 由于测试的侧重点在于存储性能，所准备的镜像需要安装 fio (用于执行测试) 和 python-paramiko (用于向 Rally 服务器传输测试结果)；
  * 由于测试执行时需要 root 权限，镜像需要设置为默认 sudo 不需要 tty (Rally 的限制)；

## 执行测试：

### 测试 Ceph 类型存储的性能

* 不同 IO 下性能的变化：

  1. 登录到 Rally 测试服务器；
  1. 使用测试文件 [test_fio_bs_rbd.yaml](https://github.com/eayunstack/rally/blob/EayunStack_v1.0/use_rally/scenarions_with_args/vm/test_fio_bs_rbd.yaml)，测试文件中已指定对应的测试脚本；
  1. 执行测试命令：`rally -d task start test_fio_bs_rbd.yaml`；
  
      ```
      # 获取 html 格式的测试结果：
      # rally task report <task_uuid> --out /var/www/html/rally_report/vm/success/<file_name>.html

      # 获取 json 格式的测试结果：
      # rally task results <task_uuid> >> /var/www/html/rally_report/vm/success/<file_name>.json
      ```

  1. 在云主机中执行脚本的直接输出将在 Rally 测试执行完成后保存在 Rally 服务器的 /tmp/ 目录下，文件名为 `/tmp/fio_bs_*`；

  > ###### 说明：
  > 测试不同 IO 时，所设置的队列深度为 4，所测试的 IO 大小为：4k, 8k, 16k, 512k, 1M, 2M, 4M, 8M。

* 不同队列深度下性能的变化：

  1. 登录到 Rally 测试服务器；
  1. 使用测试文件 [test_fio_iodepth_rbd.yaml](https://github.com/eayunstack/rally/blob/EayunStack_v1.0/use_rally/scenarions_with_args/vm/test_fio_iodepth_rbd.yaml)，测试文件中已指定对应的测试脚本；
  1. 执行测试命令：`rally -d task start test_fio_iodepth_rbd.yaml`；
  
      ```
      # 获取 html 格式的测试结果：
      # rally task report <task_uuid> --out /var/www/html/rally_report/vm/success/<file_name>.html

      # 获取 json 格式的测试结果：
      # rally task results <task_uuid> >> /var/www/html/rally_report/vm/success/<file_name>.json
      ```

  1. 在云主机中执行脚本的直接输出将在 Rally 测试执行完成后保存在 Rally 服务器的 /tmp/ 目录下，文件名为 `/tmp/fio_iodepth_*`；

  > ###### 说明：
  > 测试不同队列深度时，设置 bs=512k，所测试的队列深度为：1, 2, 4, 8, 16, 32, 64, 128, 256。

### 测试 Eqlx 类型存储的性能

* 不同 IO 下性能的变化：

  1. 登录到 Rally 测试服务器；
  1. 使用测试文件 [test_fio_bs_eqlx.yaml](https://github.com/eayunstack/rally/blob/EayunStack_v1.0/use_rally/scenarions_with_args/vm/test_fio_bs_eqlx.yaml)，测试文件中已指定对应的测试脚本；
  1. 执行测试命令：`rally -d task start test_fio_bs_eqlx.yaml`；
  
      ```
      # 获取 html 格式的测试结果：
      # rally task report <task_uuid> --out /var/www/html/rally_report/vm/success/<file_name>.html

      # 获取 json 格式的测试结果：
      # rally task results <task_uuid> >> /var/www/html/rally_report/vm/success/<file_name>.json
      ```

  1. 在云主机中执行脚本的直接输出将在 Rally 测试执行完成后保存在 Rally 服务器的 /tmp/ 目录下，文件名为 `/tmp/fio_bs_*`；

  > ###### 说明：
  > 测试不同 IO 时，所设置的队列深度为 4，所测试的 IO 大小为：4k, 8k, 16k, 512k, 1M, 2M, 4M, 8M。

* 不同队列深度下性能的变化：

  1. 登录到 Rally 测试服务器；
  1. 使用测试文件 [test_fio_iodepth_eqlx.yaml](https://github.com/eayunstack/rally/blob/EayunStack_v1.0/use_rally/scenarions_with_args/vm/test_fio_iodepth_eqlx.yaml)，测试文件中已指定对应的测试脚本；
  1. 执行测试命令：`rally -d task start test_fio_iodepth_eqlx.yaml`；
  
      ```
      # 获取 html 格式的测试结果：
      # rally task report <task_uuid> --out /var/www/html/rally_report/vm/success/<file_name>.html

      # 获取 json 格式的测试结果：
      # rally task results <task_uuid> >> /var/www/html/rally_report/vm/success/<file_name>.json
      ```

  1. 在云主机中执行脚本的直接输出将在 Rally 测试执行完成后保存在 Rally 服务器的 /tmp/ 目录下，文件名为 `/tmp/fio_iodepth_*`；

  > ###### 说明：
  > 测试不同队列深度时，设置 bs=512k，所测试的队列深度为：1, 2, 4, 8, 16, 32, 64, 128, 256。

> ###### 注：
> Rally 的测试结果输出到 /var/www/html/ 目录下后，可以直接通过浏览器输入 Rally 服务器 IP 地址，以打开测试结果。

> ###### 注意：
> 为保证测试结果的可对比性，应该使用不同的 flavor 进行测试。
