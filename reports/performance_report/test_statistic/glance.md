# Glance 组件 -- 上传镜像的性能

* 摘要

  对 Glance 组件的测试主要是上传镜像的测试，以分析上传速度。

测试中，对常用镜像进行了测试，镜像信息如下：

|镜像|镜像大小|镜像格式|
|----|--------|--------|
|cirros-0.3.4-x86_64-raw.img||RAW|
|centos-6.5-x86_64-raw.img  |8.0G|RAW|
|centos-7.0-x86_64-raw.img  |8.0G|RAW|
|ubuntu-10.04-i386-raw.img  |2.2G|RAW|
|ubuntu-10.04-x86_64-raw.img|2.2G|RAW|
|ubuntu-12.04-i386-raw.img  |2.2G|RAW|
|ubuntu-12.04-x86_64-raw.img|2.2G|RAW|
|ubuntu-14.04-i386-raw.img  |2.2G|RAW|
|ubuntu-14.04-x86_64-raw.img|2.2G|RAW|
|fedora-20-i386-raw.img     |2.0G|RAW|
|fedora-20-x86_64-raw.img   |2.0G|RAW|
|fedora-21-i386-raw.img     |3.0G|RAW|
|fedora-21-x86_64-raw.img   |3.0G|RAW|
|rhel-6.5-x86_64-raw.img    |16G |RAW|
|rhel-6.6-x86_64-raw.img    |16G |RAW|
|rhel-7.0-x86_64-raw.img    |10G |RAW|
|rhel-7.1-x86_64-raw.img    |10G |RAW|

> ###### 注意：
> EayunStack 环境仅支持 RAW 格式的镜像，因此只对 RAW 格式的镜像进行测试，其他格式不在考虑范围之内。


> ###### 说明：
> * 上述测试结果中，ubuntu-14.04-x86_64-raw.img 镜像的测试失败，因此不在上图中显示（但不会影响测试结果）；
> * 上图对镜像大小进行了排序。
