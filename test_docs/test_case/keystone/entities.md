# 验证 keystoe 实体

|内容编号|内容名称|
|--------|--------|
|03|实体|

|测试编号|测试目的|操作|预期结果|实际结果|备注|
|--------|--------|----|--------|--------|----|
|01060301|通过 ID 获取 tenant/user/role/service 实例|<ol><li>创建 tenant；</li><li>获取某个 tenant 的信息；<li>创建 user；</li><li>获取某个 user 的信息；</li><li>创建 role；</li><li>获取某个 role 的信息；</li><li>获取 service 列表；</li><li>获取某个 service 的信息。</li></ol>|<ul><li>tenant 创建成功，能够通过 tenant-get 获取 tenant 的详细信息；</li><li>user 创建成功，能够通过 get 获取 user-get 的详细信息；</li><li>role 创建成功，能够通过 get 获取 role-get 的详细信息；</li><li>获取 service 列表成功，能够通过 service-get 获取 service 的详细信息。</li></ul>|||
