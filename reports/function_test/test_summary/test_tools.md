# 测试工具介绍

对于功能测试，采用黑盒测试方法。

EayunStack 功能测试所使用的方式有 3 种，如下：

* **Rally**: EayunStack 的基准测试工具；
* **Tempest**: EayunStack 的测试框架；
* **人工**: 对于以上工具测试不到的地方，采用手工测试的办法，即通过执行命令行的方式进行测试。

  > ###### 说明：
  > * 主要采用 Rally 测试工具；
  > * 由于 Tempest 的输出信息不易读且无法修改相关参数，在 EayunStack 1.1 版本的测试总已将该工具废弃使用；
  > * Rally 无法进行测试的功能与团队研发的新功能，采用人工测试的方式。

  > ###### 注：
  > 关于 Rally 的使用，请参考 [wiki](https://oa.eayun.cn/wiki/doku.php?id=eayunstack:rally:基本使用)。

> **各模块测试方法统计：**

|模块名称|Rally 测试数目|手工测试数目|
|--------|--------------|------------|
|Authenticate|6|0|
|Keystone|15|6|
|Glance|11|2|
|Cinder|18|29|
|Neutron|26|52|
|Nova|35|17|
|Quota|5|0|
|Ceilometer|20|0|
|运维工具|0|14|
|总计|136|120|
