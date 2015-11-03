# 测试工具介绍

由于极限测试需要模拟不同的 API 请求数目和并行数，我们选择 Rally 作为测试工具。

* 在模拟不同的 API 请求数目时，可修改任务文件中的 "times" 参数，表示总的 API 请求数目；
* 在模拟不同的 API 并行数目时，可修改任务文件中的 "concurrency" 参数，表示在本次任务中每次发起 API 请求的并行数目。

所用到的测试用例如下所示：

* Nova:
  * NovaServers.boot_and_list_server
  * NovaServers.boot_and_delete_server
* Neutron:
  * NeutronNetworks.create_and_list_networks
  * NeutronNetworks.create_and_delete_networks
  * NeutronNetworks.create_and_list_subnets
  * NeutronNetworks.create_and_delete_subnets
  * NeutronNetworks.create_and_list_routers
  * NeutronNetworks.create_and_delete_routers
  * NeutronNetworks.create_and_list_ports
  * NeutronNetworks.create_and_delete_ports
* Glance:
  * GlanceImages.create_and_list_image
  * GlanceImages.create_and_delete_image
* Cinder:
  * CinderVolumes.create_and_list_volume
  * CinderVolumes.create_and_delete_volume

> ###### 备注：
> * 由于环境中对配额有限制，为了防止配额对测试的影响，可以在任务文件中的 `context` 处添加如下内容（以 nova 为例）：
>   ```
>   context:
>     ...
>     quotas:
>       nova:
>         instances: -1
>   ```
