# 验证 Keystone 的 tenant 部分

|组件编号|组件名称|测试类型|
|--------|--------|--------|
|08|Keystone|功能测试|


|测试编号|测试目的|操作|预期结果|实际结果|备注|
|--------|--------|----|--------|--------|----|
|00080101|创建 tenant|<ol><li>创建 tenant，名称长度为 10。</li></ol>|<ul><li>创建成功，无报错信息。</li></ul>|||
|00080102|创建并列出 tenant|<ol><li>创建 tenant，名称长度为 10；</li><li>列出 tenant。</li></ol>|<ul><li>创建 tenant 成功；</li><li>列出的 tenant 中能看到所创建的 tenant。</li></ul>|||
|00080103|创建 tenant 并分配一些用户|<ol><li>创建 tenant，名称长度为10；</li><li>创建 10 个 user；</li><li>把这 10 个 user 分配给所创建的 tenant。</li></ol>|<ul><li>创建 tenant 成功；</li><li>创建 user 成功；</li><li>user 被成功分配到 tenant 中。</li></ul>|||

