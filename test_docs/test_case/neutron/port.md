# 验证 Neutron 的 port 部分

|内容编号|内容名称|
|--------|--------|
|02|端口|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01070201|测试 neutron port-create 和 neutron port-list 命令的性能|<ul><li>UI:</li></ul><ol><li>登录dashboard；</li><li>neutron port-create 的创建再在建立网络与路由并且启动虚拟机时会自动产生，也可以使用命令行写```neutron port-create net1 --fixed-ip ip_address=192.168.2.40```；</li><li>```neutron port-list``` 使用命令行查看。</li></ol><ul><li>CLI:</li></ul><ol><li>登录rally测试服务器；</li><li>使用rally测试文件create_and_list_ports.json；</li><li>执行测试命令```rally task start create_and_list_ports.json```。|</li><li>能够成功的创建端口</li><li>能够查看到完整的端口列表||<ul><li>创建并列出端口</li><li>neutron port-list在UI中不能很好的查看，只能通过看各个网络下来看到，要想查看完整的列表使用命令行比较好|Rally:</br>create_and_list_ports.json|
|01070202|测试 neutron port-create 和 neutron port-delete 命令的性能|<ul><li>UI：</li></ul><ol><li>登录dashboard,在Project目录下点开Network选项在这个选项中创建网络和路由并且启动虚拟机会自动产生；</li><li>neutron port-create 的创建也可以使用命令行写```neutron port-create net1 --fixed-ip ip_address=192.168.2.40```；</li><li>测试neutron port-delete,同样登录dashboard,在Project目录下点击Network再选择路由选项；</li><li>在路由界面中可以选择你要删除的接口所在的路由进入，在接口表项中就可以删除接口。</li></ol><ul><li>CLI:</li></ul><ol><li>登录rally测试服务器；</li><li>使用rally测试文件create_and_delete_ports.json；</li><li>执行测试命令```rally task start create_and_delete_ports.json```；|</li><li>能够成功创建接口；</li><li>能够成功删除接口||</li><li>创建端口后，将其删除|Rally:</br>create_and_delete_ports.json|
|01070203|测试 neutron port-create 和 neutron port-update 命令的性能|<ul><li>UI:</li></ul><ol><li>登录dashboard,在Project目录下点开Network选项在这个选项中创建网络和路由并且启动虚拟机会自动产生；</li><li>neutron port-create 的创建也可以使用命令行写```neutron port-create net1 --fixed-ip ip_address=192.168.2.40```；</li><li>可以使用命令修改端口neutron port-update。</li></ol><ul><li>CLI:</li></ul><ol><li>登录rally服务器；</li><li>使用rally测试文件create_and_update_ports.json；</li><li>执行测试命令```rally task start create_and_update_ports.json```。|</li><li>能够成功的创建端口</li><li>能够成功的修改端口||</li><li>创建端口后，修改端口</li><li>修改端口，在UI当中只能修改端口名字，使用命令可以修改端口更多基本信息，在rally当中修改更多基本信息。|Rally:</br>create_and_update_ports.json|

