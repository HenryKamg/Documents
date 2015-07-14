# Glance 组件 -- 上传镜像的性能

* 摘要

  对 Glance 组件的测试主要是上传镜像的测试，以分析上传速度。

测试中，对常用镜像进行了测试，统计如下：

|镜像|镜像大小|镜像格式|
|----|----|--------|
|cirros-0.3.4-x86_64-raw.img|13|RAW|
|centos-6.5-x86_64-raw.img|341|RAW|
|centos-7.0-x86_64-raw.img|400|RAW|
|ubuntu-10.04-i386-raw.img|212|RAW|
|ubuntu-10.04-x86_64-raw.img|216|RAW|
|ubuntu-12.04-i386-raw.img|228|RAW|
|ubuntu-12.04-x86_64-raw.img|251|RAW|
|ubuntu-14.04-i386-raw.img|242|RAW|
|ubuntu-14.04-x86_64-raw.img|246|RAW|
|fedora-20-i386-raw.img|202|RAW|
|fedora-20-x86_64-raw.img|205|RAW|
|fedora-21-i386-raw.img|162|RAW|
|fedora-21-x86_64-raw.img|152|RAW|
|rhel-6.5-x86_64-raw.img|306|RAW|
|rhel-6.6-x86_64-raw.img|341|RAW|
|rhel-7.0-x86_64-raw.img|416|RAW|
|rhel-7.1-x86_64-raw.img|407|RAW|

> ###### 注意：
> EayunStack 环境仅支持 RAW 格式的镜像，因此只对 RAW 格式的镜像进行测试，其他格式不在考虑范围之内。

测试结果如下图显示：

![Glance 组件上传镜像所用时间]()

> ###### 说明：
> * 上述测试结果中，ubuntu-14.04-x86_64-raw.img 镜像的测试失败，因此不在上图中显示（但不会影响测试结果）；
> * 上图对镜像大小进行了排序。
