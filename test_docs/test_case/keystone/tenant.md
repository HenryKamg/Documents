# 验证 Keystone 的 tenant 部分

|内容编号|内容名称|
|--------|--------|
|01|租户|


|测试编号|测试目的|操作|预期结果|实际结果|备注|Rally/Tempest/None|
|--------|--------|----|--------|--------|----|------------------|
|01060101|创建 tenant|<ol><li>创建 tenant，名称长度为 10。</li></ol>|<ul><li>创建成功，无报错信息。</li></ul>||||
|01060102|创建并列出 tenant|<ol><li>创建 tenant，名称长度为 10；</li><li>列出 tenant。</li></ol>|<ul><li>创建 tenant 成功；</li><li>列出的 tenant 中能看到所创建的 tenant。</li></ul>||||
|01060103|创建 tenant 并分配一些用户|<ol><li>创建 tenant，名称长度为10；</li><li>创建 10 个 user；</li><li>把这 10 个 user 分配给所创建的 tenant。</li></ol>|<ul><li>创建 tenant 成功；</li><li>创建 user 成功；</li><li>user 被成功分配到 tenant 中。</li></ul>||||

