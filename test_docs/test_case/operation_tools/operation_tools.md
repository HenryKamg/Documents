#运维工具
|内容编号|内容名称|
|--------|--------|
|01|运维工具|

|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01090101|测试 ```eayunstack -h``` 命令的功能|<ol>CLI:<li>登录到任意节点;</li><li>执行命令```eayunstack -h```</li></ol>|<ol>CLI:<li>查看帮助成功</li></ol>||||
|01090102|测试 ```eayunstack list``` 命令的功能|<ol>CLI:<li>登录到任意节点</li><li>执行命令```eayunstack list```</li></ol>|<ol>CLI:<li>查看eayunstack节点列表成功</li></ol>||||
|01090103|测试 ```eayunstack doctor all``` 命令的功能|<ol>CLI:<li>登录到fuel节点</li><li>执行命令```eayunstack doctor all```</li></ol>|<lo>CLI:<li>检查所有对象成功</li></lo>||在其他节点执行则检查当前节点的状态|||



