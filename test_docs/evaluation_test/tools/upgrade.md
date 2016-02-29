# 升级 EayunStack

在EayunStack环境运行过程中，可能会出现需要对环境中的某个服务的配置或某个软件包进行升级，需要运维工具来执行。

## 环境配置

* 前提：

  * 在已有的 EayunStack 环境中升级；
  * 登录到 Fuel Master 节点；
  * 安装 YUM 源制作工具：

    ```
    (fuel)# yum install -y createrepo
    ```

* 操作：

  1. 配置 RSYNC 服务器及所有 OpenStack 节点的 YUM 源：

    ```
    (fuel)# eayunstack upgrade setup --myip 172.16.100.2
    ```
  1. 创建相关工作目录：

    ```
    (fuel)# mkdir -p /var/www/nailgun/eayunstack/repo
    ```
  1. 下在升级所须的 puppet 模块：

    ```
    (fuel)# git clone https://github.com/eayunstack/eayunstack-upgrade.git
    (fuel)# cp -r eayunstack-upgrade/puppet/ /var/www/nailgun/eayunstack/
    ```
  1. 将所要升级的 RPM 包放到 /var/www/nailgun/eayunstack/repo 目录中：

    ```
    (fuel)# tar xf EayunStack-1.1-RPMs.tgz -C /var/www/nailgun/eayunstack/repo
    ```
  1. 制作 YUM 源：

    ```
    (fuel)# createrepo /var/www/nailgun/eayunstack/repo/
    ```

> #### 注：
> `--myip` 中所使用的是 PXE 网络的 IP 地址。

* 预期结果：

  * YUM 源制作成功；
  * 环境的配置完成，可以开始升级。

## 环境升级

* 前提：

  * 已完成升级前的环境配置；
  * 登录到 Fuel Master 节点。

* 操作：

  1. 确认当前版本：

    ```
    (controller)# rpm -qa | grep openstack
    openstack-neutron-2014.2-18.eayunstack.1.0.1.noarch
    openstack-ceilometer-common-2014.2.2-2.eayunstack.1.0.1.noarch
    openstack-nova-objectstore-2014.2-6.eayunstack.1.0.1.noarch
    openstack-dashboard-2014.2.1-4.eayunstack.1.0.noarch
    openstack-keystone-2014.2-1.el7.centos.noarch
    openstack-ceilometer-alarm-2014.2.2-2.eayunstack.1.0.1.noarch
    openstack-nova-novncproxy-2014.2-6.eayunstack.1.0.1.noarch
    openstack-heat-api-cloudwatch-2014.2-1.el7.centos.noarch
    openstack-heat-api-cfn-2014.2-1.el7.centos.noarch
    openstack-cinder-2014.2.1-4.eayunstack.1.0.1.noarch
    openstack-nova-common-2014.2-6.eayunstack.1.0.1.noarch
    python-django-openstack-auth-1.1.7-2.eayunstack.1.0.noarch
    rubygem-openstack-1.1.2-1.el7.centos.noarch
    openstack-nova-cert-2014.2-6.eayunstack.1.0.1.noarch
    openstack-utils-2014.1-3.el7.centos.1.noarch
    openstack-heat-engine-2014.2-1.el7.centos.noarch
    openstack-ceilometer-notification-2014.2.2-2.eayunstack.1.0.1.noarch
    openstack-ceilometer-central-2014.2.2-2.eayunstack.1.0.1.noarch
    openstack-neutron-ml2-2014.2-18.eayunstack.1.0.1.noarch
    openstack-neutron-vpn-agent-2014.2-18.eayunstack.1.0.1.noarch
    openstack-nova-api-2014.2-6.eayunstack.1.0.1.noarch
    openstack-heat-common-2014.2-1.el7.centos.noarch
    openstack-ceilometer-collector-2014.2.2-2.eayunstack.1.0.1.noarch
    openstack-heat-api-2014.2-1.el7.centos.noarch
    openstack-ceilometer-api-2014.2.2-2.eayunstack.1.0.1.noarch
    openstack-neutron-openvswitch-2014.2-18.eayunstack.1.0.1.noarch
    openstack-glance-2014.2.1-2.el7.centos.noarch
    openstack-nova-console-2014.2-6.eayunstack.1.0.1.noarch
    openstack-nova-conductor-2014.2-6.eayunstack.1.0.1.noarch
    openstack-nova-scheduler-2014.2-6.eayunstack.1.0.1.noarch
    ```
  1. 升级第一个 Controller 节点：

    ```
    (fuel)# eayunstack upgrade go --myip 172.16.100.2
    ```
  1. 查看升级进度：

    ```
    (fuel)# eayunstack upgrade go --myip 172.16.100.2 --check-only
    ```
  1. 升级剩余节点：

    ```
    (fuel)# eayunstack upgrade go --myip 172.16.100.2
    ```
  1. 查看升级进度：

    ```
    (fuel)# eayunstack upgrade go --myip 172.16.100.2 --check-only
    ```

* 预期结果：

  * 升级第一个节点后，如果升级完成，查看进读时输出以下信息：

    ```
    [root@fuel ~](fuel)# eayunstack upgrade go --myip 172.16.100.2 --check-only
    [ INFO  ] (fuel) (fuel.domain.tld): Process on node 17 is still running.
    [root@fuel ~](fuel)# eayunstack upgrade go --myip 172.16.100.2 --check-only
    [ INFO  ] (fuel) (fuel.domain.tld): Process on node 17 is finished.
    ```
  * 升级剩余节点，升级完成时，查看进读则输出以下信息：

    ```
    [root@fuel ~](fuel)# eayunstack upgrade go --myip 172.16.100.2 --check-only
    [ INFO  ] (fuel) (fuel.domain.tld): No upgrade process is currently on the way.
    ```
  * 环境升级完成后，环境中的 RPM 包为所升级的目标版本：

    ```
    (controller)# rpm -qa | grep openstack
    openstack-nova-conductor-2014.2-8.eayunstack.1.1.noarch
    openstack-neutron-vpn-agent-2014.2-19.eayunstack.1.1.noarch
    openstack-ceilometer-common-2014.2.2-2.eayunstack.1.0.1.noarch
    openstack-dashboard-2014.2.1-4.eayunstack.1.0.noarch
    openstack-keystone-2014.2-1.el7.centos.noarch
    openstack-nova-novncproxy-2014.2-8.eayunstack.1.1.noarch
    openstack-ceilometer-alarm-2014.2.2-2.eayunstack.1.0.1.noarch
    openstack-heat-api-cloudwatch-2014.2-1.el7.centos.noarch
    openstack-heat-api-cfn-2014.2-1.el7.centos.noarch
    python-django-openstack-auth-1.1.7-2.eayunstack.1.0.noarch
    rubygem-openstack-1.1.2-1.el7.centos.noarch
    openstack-nova-cert-2014.2-8.eayunstack.1.1.noarch
    openstack-nova-api-2014.2-8.eayunstack.1.1.noarch
    openstack-neutron-openvswitch-2014.2-19.eayunstack.1.1.noarch
    openstack-utils-2014.1-3.el7.centos.1.noarch
    openstack-neutron-2014.2-19.eayunstack.1.1.noarch
    openstack-neutron-metering-agent-2014.2-19.eayunstack.1.1.noarch
    openstack-heat-engine-2014.2-1.el7.centos.noarch
    openstack-ceilometer-notification-2014.2.2-2.eayunstack.1.0.1.noarch
    openstack-ceilometer-central-2014.2.2-2.eayunstack.1.0.1.noarch
    openstack-nova-objectstore-2014.2-8.eayunstack.1.1.noarch
    openstack-nova-scheduler-2014.2-8.eayunstack.1.1.noarch
    openstack-nova-common-2014.2-8.eayunstack.1.1.noarch
    openstack-heat-common-2014.2-1.el7.centos.noarch
    openstack-ceilometer-collector-2014.2.2-2.eayunstack.1.0.1.noarch
    openstack-heat-api-2014.2-1.el7.centos.noarch
    openstack-ceilometer-api-2014.2.2-2.eayunstack.1.0.1.noarch
    openstack-cinder-2014.2.1-5.eayunstack.1.1.noarch
    openstack-nova-console-2014.2-8.eayunstack.1.1.noarch
    openstack-glance-2014.2.1-2.el7.centos.noarch
    openstack-neutron-ml2-2014.2-19.eayunstack.1.1.noarch
    ```

> #### 注：
> * 本次升级测试中没有包含 Ceilometer 的包，因此升级完成后，Ceilometer 的版本没有变化。
> * 如果升级失败，需要先删除 /var/run/eayunstack 目录下的文件：`rm /var/run/eayunstack/*`，然后重新执行升级操作。
