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


测试用例请参考[测试用例手册]()。
