# 测试工具介绍

对于功能测试，采用黑盒测试方法。

EayunStack 功能测试所使用的方式有 2 种，如下：

* **Rally**: EayunStack 的基准测试工具；
* **人工**: 对于以上工具测试不到的地方，采用手工测试的办法，即通过执行命令行的方式进行测试。

  > ###### 说明：
  > * 主要采用 Rally 测试工具；
  > * Rally 无法进行测试的功能与团队研发的新功能，采用人工测试的方式。

  > ###### 注：
  > 关于 Rally 的使用，请参考 [wiki](https://oa.eayun.cn/wiki/doku.php?id=eayunstack:rally:基本使用)。

> **各模块测试方法统计：**

|模块名称|Rally 测试用例数目|
|--------|------------------|
|Authenticate|6|
|Keystone|15|
|Glance|3|
|Cinder|16|
|Neutron|26|
|Nova|34|
|Quota|5|
|Ceilometer|20|
|运维工具|0|
|总计|121|

> #### 说明：
> * 测试用例中部分用例可用 Rally 执行，但**测试用例总数不等与 Rally 测试用例数目与人工测试数目之和**，因为存在一个 Rally 测试用例可以测试 N 个测试用例的情况。
