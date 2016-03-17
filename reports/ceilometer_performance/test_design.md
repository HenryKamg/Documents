# Ceilometer 性能测试设计

## 测试思路

鉴于 Ceilometer 所存在的问题，我们的性能测试思路如下：

1. 测试 EayunStack 1.0.1 和 EayunStack 1.1 版本中 Ceilometer 的性能，记录指标，作为优化前后的对比；
1. 通过请求时发起不同数目的进程数，观察不同并发请求下的性能变化；
1. 对 Ceilometer API 请求的返回时间作记录，作为一个性能指标。
1. 发起 Ceilometer API 请求时，记录数据库的 CPU 使用率，作为一个性能指标。

## 详细设计

1. 在测试环境中创建 200 个租户，每个租户下创建 2 台虚拟机，共 400 台虚拟机，以脚本方式完成创建；
1. 发起 Ceilometer API 请求：

  1. 每次随机查询 200 个租户中产生的半个小时内的 meter 数据，包括：

    * cpu_util
    * disk.read.bytes.rate
    * disk.write.bytes.rate
    * network.incoming.bytes.rate
    * network.outgoing.bytes.rate
  1. 以不同的进程数发起并发请求，发起 10000 次请求。
1. 记录不同线程数发起请求所用的时间和 CPU 使用率，记录到测试结果中；
1. 分别在 Ceilometer 升级前后进行测试，将结果输出作为对比数据；
1. 测试完成后，将所创建的租户和虚拟机删除。

Ceilometer 性能测试过程通过脚本进行，测试人员将测试结果整理和输出。
