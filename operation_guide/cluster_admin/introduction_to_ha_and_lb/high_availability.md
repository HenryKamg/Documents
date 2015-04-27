# Corosync
Corosync 在 EayunStack 高可用集群中为 Pacemaker 提供有效的节点信息。

配置文件是 `/etc/corosync/corosync.conf` ，主要的配置内容是 `totem` 部分，其中对集群心跳和认证方式进行了定义，如：

    totem {
        version:                             2
        token:                               3000
         token_retransmits_before_loss_const: 10
         join:                                60
         consensus:                           3600
         vsftype:                             none
         max_messages:                        20
         clear_node_high_bit:                 yes
         rrp_mode:                            none
         secauth:                             off
         threads:                             12
         transport:                           udpu
         interface {
             member {
                memberaddr: 172.16.101.3
             }
             member {
                memberaddr: 172.16.101.4
             }
             member {
                memberaddr: 172.16.101.5
             }
            ringnumber:  0
            bindnetaddr: 172.16.101.3
            mcastport:   5405
         }
    }

# Pacemaker
Pacemaker 是 EayunStack 高可用集群中的资源管理器，是 OpenStack 各组件服务、Mysql Galera 集群、RabbitMQ 集群、HAProxy 集群的实际管理者。

Pacemaker 不使用静态的配置文件，对集群（包括集群属性、集群资源等）的配置和管理都通过相应的命令行工具完成，如：`pcs` ， `crm` 。

CIB （Cluster information base ，集群信息数据库）是整个高可用的配置和状态信息的存储中心，数据存储的格式为 `XML` ，通过集群心跳连接在所有节点之间进行同步，可以通过 `pcs cluster cib` 查看，如：（ CIB 中包含的数据很多，下面的示例有省略）

    # pcs cluster cib
    <cib epoch="239" num_updates="10824" admin_epoch="0" validate-with="pacemaker-1.2" crm_feature_set="3.0.7" have-quorum="1" dc-uuid="1" cib-last-written="Wed Apr 22 17:25:20 2015" update-origin="node-1.domain.tld" update-client="crm_resource">
      <configuration>
        <crm_config>
          <cluster_property_set id="cib-bootstrap-options">
            <nvpair id="cib-bootstrap-options-dc-version" name="dc-version" value="1.1.10-32.el7_0.1-368c726"/>
            ...
           </cluster_property>
           ...
        </crm_config>
        ...
      </configuration>
      ...
    </cib> 
