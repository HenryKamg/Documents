# 测试设计

由于 EayunStack 的系统特性，对功能的测试以模块进行划分，如下：

|模块名称|测试内容|用例总数|新增数目|
|--------|--------|--------|--------|
|Authenticate|各个模块的 token|6|1|
|Keystone|keystone 模块的功能|21|6|
|Glance|glance 模块的功能|13|0|
|Neutron|neutron 模块的功能|78|58|
|Nova|nova 模块的功能|52|10|
|Cinder|cinder 模块的功能|46|4|
|Quota|各个模块的 quota 功能|5|0|
|Ceilometer|Ceilometer 模块的功能|20|20|
|AutoScaling|集群自动伸缩功能|-|-|
|运维工具|运维工具的各项功能|15|15|
|总计|-|256|114|

> ###### 注：
> * 其中【新增数目】为相对于上个版本，即 EayunStack 1.0 版本中，测试用例所增加的数目。

> ###### 注：
> 其中的 AutoScaling 功能比较特殊且比较复杂，没有直接的测试用例，但进行了相关的场景测试，详情请参考[EayunStack 场景实验手册](http://docs.eayun.cn/zh-CN/EayunStack/1.0/html/evaluation_test/index.html)中的集群自动伸缩章节。

> ###### 注：
> 运维工具属于团队自主研发的内容，不属于 EayunStack 本身的组件。

## 模块测试内容

对各个模块进行测试，保证各个组件的功能可用。

测试用例中包括了 UI 的操作和 CLI (命令行或使用测试工具) 的操作，兼顾了 Horizon 组件的测试。

如果没有 UI 上的操作，则仅有 CLI 操作与 Rally 的测试操作（如果 Rally 有对应的测试用例的话）。

### Authenticate

|测试内容|用例数目|
|--------|--------|
|验证 keystone 模块的 token|1|
|验证 glance 模块的 token|1|
|验证 neutron 模块的 token|1|
|验证 nova 模块的 token|1|
|验证 cinder 模块的 token|1|
|验证 heat 模块的 token|1|

### Keystone

|测试内容|用例数目|
|--------|--------|
|tenant|4|
|user|10|
|entity|1|
|service|3|
|role|3|

### Glance

|测试内容|用例数目|
|--------|--------|
|image|13|

### Neutron

|测试内容|用例数目|
|--------|--------|
|network|4|
|subnet|8|
|port|3|
|router|5|
|FWaaS|13|
|LBaaS|13|
|VPN|13|
|Floating IP|7|
|QoS|12|

### Nova

|测试内容|用例数目|
|--------|--------|
|server|40|
|flavor|7|
|keypair|2|
|secgroup|3|

### Cinder

|测试内容|用例数目|
|--------|--------|
|volume|37|
|snapshot|9|

### Quota

|测试内容|用例数目|
|--------|--------|
|nova quota|2|
|cinder quota|2|
|neutron quota|1|

### Ceilometer

|测试内容|用例数目|
|--------|--------|
|alarm|8|
|event|3|
|meter|3|
|resource|2|
|sample|2|
|trait|2|

### AutoScaling

|测试内容|用例数目|
|--------|--------|
|集群自动伸缩|-|

### 运维工具

|测试内容|用例数目|
|--------|--------|
|运维工具各功能|15|

## 测试范围

此功能测试仅仅针对 EayunStack 的功能本身与运维工具进行测试，不涉及 EayunStack 之外的组件 (如 Fuel) 和性能测试。

对功能的测试包括**常规途径**和**非常规途径**：

* **常规途径**：预期结果为**正确**的操作
* **非常规途径**：预期结果为**错误**的操作

> ###### 注：
> * 测试用例请参考[测试用例手册](http://docs.eayun.cn/zh-CN/EayunStack/1.1/html/test_case/index.html)。
> * 测试用例中，部分可用 Rally 进行测试，部分需要人工测试。
