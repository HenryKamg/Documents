# EayunStack 1.0.1 Ceilometer 存在的问题

如前面章节所描述，Ceilometer 会收集 EayunStack 中几乎所有的数据，因此，巨大的数据量是 Ceilometer 的瓶颈之一。

由于数据量过大，当发起 API 请求查询数据时，将会出现超时,API请求堵塞,API最终无法对外提供服务。此外，对数据库节点的系统硬件如 CPU 等也造成了不小的压力，同时平台的稳定性也造成了一定的影响。

因此，针对这些问题在 EayunStack 1.1 版本的 Ceilometer 模块中，对此进行了优化。
