# 测试设计

由于 EayunStack 的系统特性，对功能的测试以模块进行划分，如下：

|模块名称|测试内容|
|--------|--------|
|Authenticate|各个模块的 token|
|Keystone|keystone 模块的功能|
|Glance|glance 模块的功能|
|Neutron|neutron 模块的功能|
|Nova|nova 模块的功能|
|Cinder|Cinder 模块的功能|
|Quota|各个模块的 quota 功能|

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
|tenant||
|user||
|entity||
|service||

### Glance

|测试内容|用例数目|
|--------|--------|
|image||

### Neutron

|测试内容|用例数目|
|--------|--------|
|network||
|subnet||
|port||
|router||

### Nova

|测试内容|用例数目|
|--------|--------|
|server||
|keypair||
|secgroup||

### Cinder

|测试内容|用例数目|
|--------|--------|
|volume||
|snapshot||

### Quota

|测试内容|用例数目|
|--------|--------|
|nova quota||
|cinder quota||
|neutron quota||

## 测试范围

此功能测试仅仅针对 EayunStack 的功能本身进行测试，不涉及 EayunStack 之外的组件 (如 Fuel) 和性能测试。

对功能的测试包括**常规途径**和**非常规途径**：

* **常规途径**：预期结果为**正确**的操作
* **非常规途径**：预期结果为**错误**的操作

> ###### 注：
> 测试用例请参考[测试用例手册]()。
