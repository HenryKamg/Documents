# EayunStack 模块测试

EayunStack 的组件性能测试可以通过 Rally 来执行。

测试时，需要修改参数。

## Nova 模块

对 Nova 模块的性能测试主要关注同时启动 N 台云主机所需要的时间。

测试步骤如下：

1. 登录到 Rally 测试服务器；
1. 执行测试命令：`rally -d task start boot.yaml`；
1. 测试结束后，输出测试结果：

  ```
  # html 格式的测试结果
  # rally task report <UUID> --out /var/www/html/rally_report/nova/<file_name>.html

  # json 格式的测试结果
  # rally task results <UUID> >> /var/www/html/rally_report/nova/<file_name>.json
  ```

1. 可以通过浏览器打开 Rally 服务器地址查看测试结果。

## Cinder 模块

对 Cinder 模块的性能测试主要关注创建卷所需要的时间。

测试步骤如下：

1. 登录到 Rally 测试服务器；
1. 执行测试命令：`rally -d task start create-volume_rbd.yaml`；
1. 执行测试命令：`rally -d task start create-volume_eqlx.yaml`；
1. 测试结束后，输出测试结果：

  ```
  # html 格式的测试结果
  # rally task report <UUID> --out /var/www/html/tempest_report/cinder/<file_name>.html

  # json 格式的测试结果
  # rally task results <UUID> --json --ouput-file /var/www/html/rally_report/cinder/<file_name>.json
  ```

1. 可以通过浏览器打开 Rally 服务器地址查看测试结果。

## Glance 模块

对 Glance 模块的性能测试主要关注上传镜像所需要的时间。

测试步骤如下：

1. 登录到 Rally 测试服务器；
1. 执行测试命令：`rally -d task start xxxx.yaml`；
1. 测试结束后，输出测试结果：

  ```
  # html 格式的测试结果
  # rally task report <UUID> --out /var/www/html/rally_report/glance/<file_name>.html

  # json 格式的测试结果
  # rally task results <UUID> >> /var/www/html/rally_report/glance/<file_name>.json
  ```

1. 可以通过浏览器打开 Rally 服务器地址查看测试结果。

## Neutron 模块

测试步骤如下：

1. 登录到 Rally 测试服务器；
1. 执行测试命令：`rally -d verify start --set network`；
1. 测试结束后，输出测试结果：

  ```
  # html 格式的测试结果
  # rally verify results <UUID> --html --ouput-file /var/www/html/tempest_report/network/<file_name>.html

  # json 格式的测试结果
  # rally verify results <UUID> --json --ouput-file /var/www/html/tempest_report/network/<file_name>.json
  ```

1. 可以通过浏览器打开 Rally 服务器地址查看测试结果。

## Keystone 模块

Keystone 相关的测试需要 admin 权限来执行，因此，在测试之前需要修改配置文件：

1. 配置文件位置在与 rally/ 同一级目录下的 `.rally/tempest/for-deployment-\<deployment_uuid\>/tempest.conf`；
1. 打开配置文件，将 [identity] 小节下的 `username`、`password` 修改为具有 admin 权限的用户名和密码；
1. 保存后执行测试。

测试步骤如下：

1. 登录到 Rally 测试服务器；
1. 执行测试命令：`rally -d verify start --set identity`；
1. 测试结束后，输出测试结果：

  ```
  # html 格式的测试结果
  # rally verify results <UUID> --html --ouput-file /var/www/html/tempest_report/identity/<file_name>.html

  # json 格式的测试结果
  # rally verify results <UUID> --json --ouput-file /var/www/html/tempest_report/identity/<file_name>.json
  ```

1. 可以通过浏览器打开 Rally 服务器地址查看测试结果。

## 其他测试

除了按照模块划分测试外，还可以执行下列测试：

```
# DNS 的测试
# rally -d verify start --set dns

# 冒烟测试
# rally -d verify start --set smoke

# 场景测试（Tempest 定义的一些简单场景）
# rally -d verify start --set scenario

# 完全测试（执行所有测试）
# rally -d verify start --set full
```
