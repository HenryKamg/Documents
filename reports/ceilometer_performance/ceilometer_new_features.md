# EayunStack 1.1 Ceilometer 的改进

为了得到更好的性能和稳定性，EayunStack 1.1 对 Ceilometer 作了如下优化：

* Ceilometer API重构，通过使用 Apache调用 Ceilometer mod_wsgi 提高 API 的性能和稳定性；
* Ceilometer 后端存储数据库实现高可用；
* Mongodb 数据库性能优化，通过建立查询索引，将 Mongo 索引数据放入内存中，提高查询性能。

