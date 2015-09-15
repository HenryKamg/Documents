####MongoDB安装

> 通过RPM包安装

* 安装Mongodb服务软件mongodb-server

  yum install mongodb-server

* 安装Mongodb客户端软件mongodb

  yum install mongodb


> 通过二进制源码包安装

  二进制源码包安装，直接下载文件，解压文件后，通过配置即可启动mongodb服务

####MongoDB常用配置

  Mongodb配置通过配置mongodb.conf文件进行配置，常用配置如下：

  |配置项|作用|
  |------|----|
  |bind_ip|配置服务去绑定IP地址，配置为本地服务器IP地址|
  |fork=true|以守护进程方式运行Mongodb|
  |port=27017|配置服务启动后绑定端口|
  |dbpath=/var/lib/mongo|配置mongodb启动后，数据文件存储位置|
  |pidfilepath=/var/run/mongodb/mongodb.pid|配置mongodb启动后PID文件|
  |auth=true|配置启用登录认证|
  |setParameter=logLevel=2|配置mongodb日志存储|
  |smallfiles=true|使用最小方式启动数据库，不配置此项，启动时通过比例计算数据存储文件占用空间大小，此种模式下，数据较大|
  |journal=true|写日志|
  |replSet=ceilometer|配置副本集名称|
  |keyFile =/etc/file.key|配置认证key文件|

  以上在配置副本集中：replSet、keyFile必须配置

> keyFile 文件生成

  使用`openssl rand -base64 100 > /mongodb/scheme2/file.key` --文件内容采base64编码，一共100个字符,key文件的权限为`600`且属主别需为mongodb

### 常用命令

####服务启动与停止

```
[root@node-9 ~](mongo)# systemctl start mongod （服务启动）
[root@node-9 ~](mongo)# systemctl stop mongod  （服务停止）
[root@node-9 ~](mongo)# systemctl status mongod （服务状态查看）
mongod.service - High-performance, schema-free document-oriented database
   Loaded: loaded (/usr/lib/systemd/system/mongod.service; enabled)
   Active: active (running) since 二 2015-09-15 11:05:33 CST; 1min 57s ago
  Process: 19181 ExecStart=/usr/bin/mongod $OPTIONS run (code=exited, status=0/SUCCESS)
 Main PID: 19183 (mongod)
   CGroup: /system.slice/mongod.service
           └─19183 /usr/bin/mongod --quiet -f /etc/mongodb.conf run

9月 15 11:05:33 node-9.eayun.com mongod[19181]: about to fork child process, waiting until server is ready ...ons.
9月 15 11:05:33 node-9.eayun.com mongod[19181]: forked process: 19183
9月 15 11:05:33 node-9.eayun.com mongod[19181]: child process started successfully, parent exiting
9月 15 11:05:33 node-9.eayun.com systemd[1]: Started High-performance, schema-free document-oriented database.
Hint: Some lines were ellipsized, use -l to show in full.

```

####mongodb 监控

```
通过mongostat查看mongo数据库信息
[root@node-9 ~]# mongostat -u sa -p  （使用mongo用户与密码登录）
Enter password:
connected to: 127.0.0.1
insert  query update delete getmore command flushes mapped  vsize    res faults  locked db idx miss %     qr|qw   ar|aw  netIn netOut  conn        set repl       time
    *0     *0     *0     *0       0     1|0       0  4.31g  9.27g    88m      0  test:0.0%          0       0|0     0|0    62b     3k    11 ceilometer  PRI   23:13:57
    *0     *0     *0     *0       2     4|0       0  4.31g  9.27g    88m      0  test:0.0%          0       0|0     0|0   594b     4k    11 ceilometer  PRI   23:13:58
    *0     *0     *0     *0       0     1|0       0  4.31g  9.27g    88m      0  test:0.0%          0       0|0     0|0    62b     3k    11 ceilometer  PRI   23:13:59
    *0     *0     *0     *0       0     4|0       0  4.31g  9.27g    88m      0  test:0.0%          0       0|0     0|0   500b     4k    11 ceilometer  PRI   23:14:00
    *0     *0     *0     *0       1     1|0       0  4.31g  9.27g    88m      0  test:0.0%          0       0|0     0|0   109b     3k    11 ceilometer  PRI   23:14:01
    *0     *0     *0     *0       0     4|0       0  4.31g  9.27g    88m      0 local:0.0%          0       0|0     0|0   500b     4k    11 ceilometer  PRI   23:14:02
    *0     *0     *0     *0       2     1|0       0  4.31g  9.27g    88m      0  test:0.0%          0       0|0     0|0   156b     3k    11 ceilometer  PRI   23:14:03
    *0     *0     *0     *0       0     4|0       0  4.31g  9.27g    88m      0  test:0.0%          0       0|0     0|0   500b     4k    11 ceilometer  PRI   23:14:04
    *0     *0     *0     *0       0     1|0       0  4.31g  9.27g    88m      0  test:0.0%          0       0|0     0|0    62b     3k    11 ceilometer  PRI   23:14:05
    *0     *0     *0     *0       1     4|0       0  4.31g  9.27g    88m      0  test:0.0%          0       0|0     0|0   547b     4k    11 ceilometer  PRI   23:14:06

通过serverStatus获取与的MongoDB服务器统计信息
[root@node-9 ~]# mongo 127.0.0.1:27017/admin -u sa -p
MongoDB shell version: 2.6.11
Enter password:
connecting to: 127.0.0.1:27017/admin
ceilometer:PRIMARY> db.runCommand({"serverStatus":1})
{
	"host" : "node-9",
	"version" : "2.6.11",
	"process" : "mongod",
	"pid" : NumberLong(23022),
	"uptime" : 66735,
	"uptimeMillis" : NumberLong(66735149),
	"uptimeEstimate" : 65503,
	"localTime" : ISODate("2015-09-15T03:19:43.174Z"),
	"asserts" : {
		"regular" : 0,
		"warning" : 0,
		"msg" : 0,
		"user" : 20,
		"rollovers" : 0
	},
	"backgroundFlushing" : {
		"flushes" : 1112,
		"total_ms" : 21903,
		"average_ms" : 19.696942446043167,
		"last_ms" : 124,
		"last_finished" : ISODate("2015-09-15T03:19:28.365Z")
	},
	"connections" : {
		"current" : 12,
		"available" : 807,
		"totalCreated" : NumberLong(6692)
	},


		"storage" : {
			"freelist" : {
				"search" : {
					"bucketExhausted" : NumberLong(0),
					"requests" : NumberLong(2),
					"scanned" : NumberLong(4)
				}
			}
		},
		"ttl" : {
			"deletedDocuments" : NumberLong(0),
			"passes" : NumberLong(1112)
		}
	},
	"ok" : 1
}
ceilometer:PRIMARY>
该收集中信息比齐全，包括网络，复制集，存储等，因信息较多，未全部贴出
```

####Mongo 导入/导出

 Mongodb支持数据导入与到操作，通过使用`mongoexport、mongoimport`导出导入



