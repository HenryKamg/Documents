# 创建外部网络

通过外部网络，internet能很方便的接入云主机环境，默认情况下，外部接入时需要调整云主机安全组规则

### 通过Web horizon创建外部网络

* 登录Web horizon点击管理员----系统----网络----创建网络

![Networkext_Create](/operation_guide/basic_admin/Picture/network_create1.jpg)

> 填写名称、选择项目、供应商类型、勾选外部网络、点击创建网络

![Networkext_Create](/operation_guide/basic_admin/Picture/network_create2.jpg)

* 点击新建的网络，进入子网创建界面

![Networkext_Create](/operation_guide/basic_admin/Picture/network_create3.jpg)

> 填写子网名称、子网地址、网关

* 下一步，配置子网详情，配置完成后，点击创建

![Networkext_Create](/operation_guide/basic_admin/Picture/network_create4.jpg)

> 外部网络不用勾选dhcp与dns配置

* 点击已创建，创建完成



