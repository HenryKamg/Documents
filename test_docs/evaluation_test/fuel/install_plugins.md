# 安装 EayunStack 插件

## 列出已安装插件

* 前提：

  * Fuel 的安装已经完成，能够正常使用。

* 操作：

  1. 登录到 Fuel 节点；
  1. 执行命令查看可安装的插件：

    ```
    (fuel)# fuel plugins -l
    ```

* 预期结果：

  命令输出所有已经安装的插件：

    ```
    (fuel)# fuel plugins -l
    id | name           | version | package_version
    ---|----------------|---------|----------------
    1  | cinder_eqlx    | 1.0.0   | 1.0.0          
    2  | neutron-fwaas  | 1.0.0   | 1.0.0          
    3  | neutron-lbaas  | 1.0.0   | 1.0.0          
    4  | neutron-qos    | 1.0.0   | 1.0.0          
    5  | neutron-vpnaas | 1.0.0   | 1.0.0          
    ```

## 安装 Cinder Eqlx 插件

* 前提：

  * Fuel 的安装已经完成，能够正常使用；
  * Cinder Eqlx 插件未安装。

* 操作：

  1. 登录到 Fuel 节点；
  1. 执行命令安装 Eqlx 插件：

    ```
    (fuel)# fuel plugins --install /opt/eayunstack/cinder_eqlx-1.0.0.fp
    ```

* 预期结果：

   * 成功安装插件；
   * 如果插件已安装，执行命令后将报错；
   * 查看已安装的插件，输出的内容中包含 cinder_eqlx 插件的信息。

## 安装 Neutron LBaaS 插件

* 前提：

  * Fuel 的安装已经完成，能够正常使用；
  * Neutron LBaaS 插件未安装。

* 操作：

  1. 登录到 Fuel 节点；
  1. 执行命令安装 Neutron LBaaS 插件：

    ```
    (fuel)# fuel plugins --install /opt/eayunstack/neutron-lbaas-1.0.0.fp
    ```

* 预期结果：

   * 成功安装插件；
   * 如果插件已安装，执行命令后将报错；
   * 查看已安装的插件，输出的内容中包含 neutron-lbaas 插件的信息。

## 安装 Neutron FWaaS 插件

* 前提：

  * Fuel 的安装已经完成，能够正常使用；
  * Neutron FWaaS 插件未安装。

* 操作：

  1. 登录到 Fuel 节点；
  1. 执行命令安装 Neutron FWaaS 插件：

    ```
    (fuel)# fuel plugins --install /opt/eayunstack/neutron-fwaas-1.0.0.fp
    ```

* 预期结果：

   * 成功安装插件；
   * 如果插件已安装，执行命令后将报错；
   * 查看已安装的插件，输出的内容中包含 neutron-fwaas 插件的信息。

## 安装 Neutron VPNaaS 插件

* 前提：

  * Fuel 的安装已经完成，能够正常使用；
  * Neutron VPNaaS 插件未安装。

* 操作：

  1. 登录到 Fuel 节点；
  1. 执行命令安装 Neutron VPNaaS 插件：

    ```
    (fuel)# fuel plugins --install /opt/eayunstack/neutron-vpnaas-1.0.0.fp
    ```

* 预期结果：

   * 成功安装插件；
   * 如果插件已安装，执行命令后将报错；
   * 查看已安装的插件，输出的内容中包含 neutron-vpnaas 插件的信息。

## 安装 Neutron QoS 插件

* 前提：

  * Fuel 的安装已经完成，能够正常使用；
  * Neutron QoS 插件未安装。

* 操作：

  1. 登录到 Fuel 节点；
  1. 执行命令安装 Neutron QoS 插件：

    ```
    (fuel)# fuel plugins --install /opt/eayunstack/neutron-qos-1.0.0.fp
    ```

* 预期结果：

   * 成功安装插件；
   * 如果插件已安装，执行命令后将报错；
   * 查看已安装的插件，输出的内容中包含 neutron-qos 插件的信息。
