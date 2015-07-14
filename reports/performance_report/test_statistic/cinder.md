# Cinder 组件 -- 创建卷的性能

* 摘要

  对 Cinder 组件的测试主要是创建卷的测试，卷的类型（存储的后端）包括 Ceph 和 Eqlx 两种，对二者测试后进行相应的对比。

## 创建空卷

创建空卷的测试选用了不同大小的卷：1G、10G、50G、100G。

卷类型分为 Ceph 和 Eqlx。

## 从镜像创建卷

测试从镜像创建卷，使用常用镜像进行测试，如下：

|镜像|镜像大小|镜像格式|
|----|--------|--------|
|cirros-0.3.4-x86_64-raw||RAW|
|centos-6.5-x86_64-raw||RAW|
|centos-7.0-x86_64-raw||RAW|
|ubuntu-10.04-i386-raw||RAW|
|ubuntu-10.04-x86_64-raw||RAW|
|ubuntu-12.04-i386-raw||RAW|
|ubuntu-12.04-x86_64-raw||RAW|
|ubuntu-14.04-i386-raw||RAW|
|ubuntu-14.04-x86_64-raw||RAW|
|fedora-20-i386-raw||RAW|
|fedora-20-x86_64-raw||RAW|
|fedora-21-i386-raw||RAW|
|fedora-21-x86_64-raw||RAW|
|rhel-6.5-x86_64-raw||RAW|
|rhel-6.6-x86_64-raw||RAW|
|rhel-7.0-x86_64-raw||RAW|
|rhel-7.1-x86_64-raw||RAW|

卷类型分为 Ceph 和 Eqlx。

