# 测试工具介绍

对于功能测试，采用黑盒测试方法。

EayunStack 功能测试所使用的方式有 3 种，如下：

* **Rally**: EayunStack 的基准测试工具；
* **Tempest**: EayunStack 的测试框架；
* **手工**: 对于已上工具测试不到的地方，采用手工测试的办法，即通过执行命令行的方式进行测试。

  > ###### 说明：
  > * 主要采用 Rally 测试工具；
  > * 由于 Tempest 的输出信息不易读，基本不采用 Tempest 测试工具；
  > * 少数使用手工测试。

  > ###### 注：
  > 关于 Rally 的使用，请参考 [wiki](https://oa.eayun.cn/wiki/doku.php?id=eayunstack:rally:基本使用)。

> **各模块测试方法统计：**

|模块名称|Rally 测试数目|手工测试数目|
|--------|--------------|------------|
|Authenticate|5|0|
|Keystone|9|6|
|Glance|11|2|
|Cinder|18|24|
|Neutron|13|7|
|Nova|30|12|
|Quota|5|0|
|总计|91|51|
