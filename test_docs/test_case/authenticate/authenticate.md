# 验证组件的 Token

|类型编号|类型名称|模块编号|模块名称|
|--------|--------|--------|--------|
|01|功能测试|01|验证 Token|

|内容编号|内容名称|
|--------|--------|
|01|authenticate|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01010101|验证 keystone 客户端|<ul><li>UI:</li></ul><ol><li>登录到 dashboard；</li><li>点击上方项目选项点开再点击compute子选项点击下面的子选项实例，进入实界面；</li><li>在实例界面点击启动云主机选项；</li><li>进入详情填写界面，选择可用域，填写云主机名称“VM1”，云主机类型"m1.tiny",云主机数量“1”，云主机启动源“从镜像启动“；</li><li>访问&安全，使用默认安全组；</li><li>网络选择已经设定好的内网；</li><li>点击“运行”。</li></ol><ul><li>CLI:</li></ul><ol><li>登录rally测试服务器；</li><li>使用rally测试文档keystone.json；</li><li>执行测试命名rally task start keystone.json。|</li><li>UI:能够成功启动虚拟机，就表示验证成功。</li><li>CLI:rally测试成功。|||Rally:</br>keystone.json|
|01010102|验证 cinder 客户端的 token|||||Rally:</br>token_validate_cinder.json|
|01010103|验证 glance 客户端的 token|<ul><li>UI:</li></ul><ol><li>登录到dashboard；</li><li>点击上方项目点开点击compute子选项，再点击镜像选项进入镜像界面；</li><li>进入镜像界面点击创建镜像，名称“cirros1”，镜像源选择镜文件或（镜像地址），上传一个镜像文件，让他成为公有，不受保护的类型，点击创建镜像。</li></ol><ul><li>CLI:</li></ul><ol><li>登录rally测试服务器；</li><li>使用rally测试文档token_validate_cinder.json；</li><li>执行测试命令rally task start token_validate_cinder.json。|</li><li>UI:镜像创建成功，即验证成功。</li><li>CLI:rally测试成功。|||Rally:</br>token_validate_glance.json|
|01010104|验证 heat 客户端的 token|||||Rally:</br>token_validate_heat.json|
|01010105|验证 neutron 客户端的 token|<ul><li>UI:</li></ul><ol><li>||||Rally:</br>token_validate_neutron.json|
|01010106|验证 nova 客户端的 token|<ul><li>Ter:</li></ul><ol><li>登录到控制节点，使用nova启动一个实例；</li><li>执行命令nova image-list；</li><li>执行命令nova flavor-list；</li><li>启动虚拟机实例之前记录下你所需的镜像和云主机的类型ID，执行命令，启动一个名为my_instance的虚拟机，执行如下命令:nova boot --image 949c80c8-b4ac-4315-844e-69f9bef39ed1 --flavor 2 my_instance；</li><li>执行命令查看虚拟机 nova list；</li><li>执行nova show命令查看虚拟机具体信息。</li></ol><ul><li>CLI:</li></ul><ol><li>登录rally测试服务器；</li><li>使用rally测试文档token_validate_nova.json；</li><li>执行测试命令rally task start token_validate_nova.json。|</li><li>UI:能够成功的启动实例，nova list和nova show都能够成功的查看到。</li><li>CLI:rally测试成功。||从图形化界面操作在可用域选项选择nova|Rally:</br>token_validate_nova.json|

