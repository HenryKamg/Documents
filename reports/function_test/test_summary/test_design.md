# 测试设计

由于 EayunStack 的系统特性，对功能的测试以模块进行划分，如下：

|模块名称|测试内容|用例总数|
|--------|--------|--------|
|Authenticate|各个模块的 token|5|
|Keystone|keystone 模块的功能|15|
|Glance|glance 模块的功能|13|
|Neutron|neutron 模块的功能|20|
|Nova|nova 模块的功能|42|
|Cinder|cinder 模块的功能|42|
|Quota|各个模块的 quota 功能|5|

## 模块测试内容

对各个模块进行测试，保证各个组件的功能可用。

每个测试都包括了 UI 的操作和 CLI (命令行或使用测试工具) 的操作，兼顾了 Horizon 组件的测试。

### Authenticate

|测试内容|用例数目|
|--------|--------|
|验证 keystone 模块的 token|1|
|验证 glance 模块的 token|1|
|验证 neutron 模块的 token|1|
|验证 nova 模块的 token|1|
|验证 cinder 模块的 token|1|

### Keystone

|测试内容|用例数目|
|--------|--------|
|tenant|4|
|user|7|
|entity|1|
|service|3|

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

### Nova

|测试内容|用例数目|
|--------|--------|
|server|30|
|flavor|7|
|keypair|2|
|secgroup|3|

### Cinder

|测试内容|用例数目|
|--------|--------|
|volume|33|
|snapshot|9|

### Quota

|测试内容|用例数目|
|--------|--------|
|nova quota|2|
|cinder quota|2|
|neutron quota|1|

## 测试范围

此功能测试仅仅针对 EayunStack 的功能本身进行测试，不涉及 EayunStack 之外的组件 (如 Fuel) 和性能测试。

对功能的测试包括**常规途径**和**非常规途径**：

* **常规途径**：预期结果为**正确**的操作
* **非常规途径**：预期结果为**错误**的操作

> ###### 注：
> 测试用例请参考[测试用例手册]()。
