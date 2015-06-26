# EayunStack 模块测试

EayunStack 的组件性能测试可以通过 Tempest 来执行。

而 Rally 对 Tempest 进行了一定的封装，可以直接通过 Rally 执行 Tempest 测试，并生成易于理解的测试结果。

## Nova 模块

测试步骤如下：

1. 登录到 Rally 测试服务器；
1. 执行测试命令：`rally -d verify start --set compute`；
1. 测试结束后，输出测试结果：

  ```
  # html 格式的测试结果
  # rally verify results <UUID> --html --ouput-file /var/www/html/tempest_report/compute/<file_name>.html

  # json 格式的测试结果
  # rally verify results <UUID> --json --ouput-file /var/www/html/tempest_report/compute/<file_name>.json
  ```

1. 可以通过浏览器打开 Rally 服务器地址查看测试结果。

## Cinder 模块

测试步骤如下：

1. 登录到 Rally 测试服务器；
1. 执行测试命令：`rally -d verify start --set volume`；
1. 测试结束后，输出测试结果：

  ```
  # html 格式的测试结果
  # rally verify results <UUID> --html --ouput-file /var/www/html/tempest_report/volume/<file_name>.html

  # json 格式的测试结果
  # rally verify results <UUID> --json --ouput-file /var/www/html/tempest_report/volume/<file_name>.json
  ```

1. 可以通过浏览器打开 Rally 服务器地址查看测试结果。

## Glance 模块

测试步骤如下：

1. 登录到 Rally 测试服务器；
1. 执行测试命令：`rally -d verify start --set image`；
1. 测试结束后，输出测试结果：

  ```
  # html 格式的测试结果
  # rally verify results <UUID> --html --ouput-file /var/www/html/tempest_report/image/<file_name>.html

  # json 格式的测试结果
  # rally verify results <UUID> --json --ouput-file /var/www/html/tempest_report/image/<file_name>.json
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
