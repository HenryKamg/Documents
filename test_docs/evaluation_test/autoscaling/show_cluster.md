# 查看集群信息

## 查看集群资源

* 前提：

  * 已经创建好包含负载均衡的自动伸缩集群。

* 操作：

  1. 登录到 Controller 节点，加载所要查看自动伸缩集群的租户的环境变量脚本；
  1. 查看集群资源列表，执行：

    ```
    # heat resource-list <STACK_NAME or STACK_ID>
    ```
  1. 查看集群输出列表，执行：

    ```
    # heat output-list <STACK_NAME or STACK_ID>
    ```
  1. 查案集群事件列表；

    ```
    # heat event-list <STACK_NAME or STACK_ID>
    ```

* 预期结果：

  * 成功列出集群资源：

    ```
    # heat resource-list coffee_withlb
    +------------------+--------------------------------------+----------------------------+-----------------+----------------------+
    | resource_name    | physical_resource_id                 | resource_type              | resource_status | updated_time         |
    +------------------+--------------------------------------+----------------------------+-----------------+----------------------+
    | monitor          | de9fe43b-c16f-4359-ad64-955b2e7467f3 | OS::Neutron::HealthMonitor | CREATE_COMPLETE | 2015-10-10T03:55:40Z |
    | pool             | dd7c63db-00ef-4185-a318-5493847e0590 | OS::Neutron::Pool          | CREATE_COMPLETE | 2015-10-10T03:55:41Z |
    | lb               |                                      | OS::Neutron::LoadBalancer  | CREATE_COMPLETE | 2015-10-10T03:55:47Z |
    | lb_floating      | e52b2074-9d47-48a4-abde-9c3248771181 | OS::Neutron::FloatingIP    | CREATE_COMPLETE | 2015-10-10T03:55:47Z |
    | server_group     | 41e0234e-9048-42e8-9576-ec292a038a1e | OS::Heat::AutoScalingGroup | CREATE_COMPLETE | 2015-10-10T03:55:47Z |
    | scaledown_policy | c1e03e6fb081466e856d5ec9cafd2a18     | OS::Heat::ScalingPolicy    | CREATE_COMPLETE | 2015-10-10T03:56:00Z |
    | scaleup_policy   | 990cf9b9eb214d41905b61b94610d852     | OS::Heat::ScalingPolicy    | CREATE_COMPLETE | 2015-10-10T03:56:00Z |
    | cpu_alarm_high   | 38fe8b9a-8b4a-4bff-b0cc-7990e55e8b4d | OS::Ceilometer::Alarm      | CREATE_COMPLETE | 2015-10-10T03:56:02Z |
    | cpu_alarm_low    | 3a6db4a0-331a-4cfb-bfb5-d8fb80ed25b8 | OS::Ceilometer::Alarm      | CREATE_COMPLETE | 2015-10-10T03:56:02Z |
    +------------------+--------------------------------------+----------------------------+-----------------+----------------------+
    ```
  * 成功列出集群输出：

    ```
    # heat output-list coffee_withlb
    +------------------+-------------+
    | output_key       | description |
    +------------------+-------------+
    | ceilometer_query |             |
    |                  |             |
    | scale_dn_url     |             |
    |                  |             |
    | scale_up_url     |             |
    |                  |             |
    | website_url      |             |
    |                  |             |
    +------------------+-------------+
    ```
  * 成功列出集群事件：

    ```
    # heat event-list coffee_withlb
    +------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+--------------------+----------------------+
    | resource_name    | id                                   | resource_status_reason                                                                                                         | resource_status    | event_time           |
    +------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+--------------------+----------------------+
    | scaledown_policy | 834ef4b4-cf01-4f46-8302-41cb30bcd16c | alarm state changed from insufficient data to alarm (Transition to alarm due to 1 samples outside threshold, most recent: 2.1) | signal_COMPLETE    | 2015-10-10T04:01:54Z |
    | cpu_alarm_high   | f9b66cfb-cc37-4ee2-931a-f44ba36d8b92 | state changed                                                                                                                  | CREATE_COMPLETE    | 2015-10-10T03:56:03Z |
    | cpu_alarm_low    | 9fe7b134-8d7f-4e2c-bf8c-5dee5cee4f7f | state changed                                                                                                                  | CREATE_COMPLETE    | 2015-10-10T03:56:03Z |
    | cpu_alarm_high   | 404f3845-7751-479a-8895-bbcc7237d1d8 | state changed                                                                                                                  | CREATE_IN_PROGRESS | 2015-10-10T03:56:02Z |
    | cpu_alarm_low    | c23ac1f5-a825-4233-90cf-7fad423bd7df | state changed                                                                                                                  | CREATE_IN_PROGRESS | 2015-10-10T03:56:02Z |
    | scaleup_policy   | 171d51ec-e0a0-459c-bbc1-a3e486ceabb1 | state changed                                                                                                                  | CREATE_COMPLETE    | 2015-10-10T03:56:02Z |
    | scaledown_policy | 4465b8f8-0e05-406e-8fda-2029752799d1 | state changed                                                                                                                  | CREATE_COMPLETE    | 2015-10-10T03:56:02Z |
    | scaleup_policy   | 916f540d-8fd4-4af0-adfb-f2c8de4ef52c | state changed                                                                                                                  | CREATE_IN_PROGRESS | 2015-10-10T03:56:00Z |
    | scaledown_policy | 0de4cb10-48fe-4a85-b0ae-34f4806c5e11 | state changed                                                                                                                  | CREATE_IN_PROGRESS | 2015-10-10T03:56:00Z |
    | server_group     | e3493fe0-98b6-48de-8afc-ae078cb20e61 | state changed                                                                                                                  | CREATE_COMPLETE    | 2015-10-10T03:56:00Z |
    | lb_floating      | cc1cb7d8-fa79-4f15-895c-91d3f0f6eb3c | state changed                                                                                                                  | CREATE_COMPLETE    | 2015-10-10T03:55:51Z |
    | lb               | b4a0f5cd-d7b5-46c5-85b6-f498333ade69 | state changed                                                                                                                  | CREATE_COMPLETE    | 2015-10-10T03:55:51Z |
    | server_group     | 1d58c9c3-aadf-415a-945c-ddf0d45ac610 | state changed                                                                                                                  | CREATE_IN_PROGRESS | 2015-10-10T03:55:47Z |
    | lb_floating      | 0d0ab118-8bbf-4e6c-abf4-96c49ced282b | state changed                                                                                                                  | CREATE_IN_PROGRESS | 2015-10-10T03:55:47Z |
    | lb               | 52c8df60-fa34-4178-8132-441c21d02164 | state changed                                                                                                                  | CREATE_IN_PROGRESS | 2015-10-10T03:55:47Z |
    | pool             | 0af0b2ae-fbb5-48e2-941f-4f8bdfef37de | state changed                                                                                                                  | CREATE_COMPLETE    | 2015-10-10T03:55:47Z |
    | pool             | 5a256f60-bc68-4b74-baa9-a4da5cae5f85 | state changed                                                                                                                  | CREATE_IN_PROGRESS | 2015-10-10T03:55:41Z |
    | monitor          | 0ea20a3f-3f2c-493c-86ef-3c708196431f | state changed                                                                                                                  | CREATE_COMPLETE    | 2015-10-10T03:55:41Z |
    | monitor          | 6928c4c3-7d81-4322-bb94-1b195eab73b7 | state changed                                                                                                                  | CREATE_IN_PROGRESS | 2015-10-10T03:55:40Z |
    +------------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+--------------------+----------------------+
    ```
  * 如果有警报发生，会记录在事件中。

> ###### 说明：
> * 由于列出信息基本一致，实验使用包含负载均衡的集群作为测试对象；
> * 列出集群输出的测试中，对集群输出的描述过长，由于篇幅问题，在预期的输出中已将描述内容删除；实际输出结果以创建时对输出的描述为准。

## 查看资源的详细内容

* 前提：

  * 已经创建好包含负载均衡的自动伸缩集群。

* 操作：

  1. 登录到 Controller 节点，加载所要查看集群的租户的环境变量脚本；
  1. 列出负载均衡资源的详细信息：

    ```
    # heat resource-show <STACK_NAME or STACK_ID> <RESOURCE_NAME>
    ```

* 预期结果：

  * 成功列出集群负载均衡资源的详细信息：

    ```
    # heat resource-show coffee_withlb lb
    +------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | Property               | Value                                                                                                                                  |
    +------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | description            |                                                                                                                                        |
    | links                  | http://25.0.0.2:8004/v1/bf87349ae6704a87af75ebe9546d4af6/stacks/coffee_withlb/702c0b4d-751b-4fd1-9c35-f9bb9f8676b7/resources/lb (self) |
    |                        | http://25.0.0.2:8004/v1/bf87349ae6704a87af75ebe9546d4af6/stacks/coffee_withlb/702c0b4d-751b-4fd1-9c35-f9bb9f8676b7 (stack)             |
    | logical_resource_id    | lb                                                                                                                                     |
    | physical_resource_id   |                                                                                                                                        |
    | required_by            |                                                                                                                                        |
    | resource_name          | lb                                                                                                                                     |
    | resource_status        | CREATE_COMPLETE                                                                                                                        |
    | resource_status_reason | state changed                                                                                                                          |
    | resource_type          | OS::Neutron::LoadBalancer                                                                                                              |
    | updated_time           | 2015-10-10T03:55:47Z                                                                                                                   |
    +------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
    ```

> ###### 说明：
> 所有资源的详细信息都可以查看，本实验仅查看了其中一种资源的详细信息。

## 查看事件的详细信息

* 前提：

  * 已经创建好包含负载均衡的自动伸缩集群。

* 操作：

  1. 登录到 Controller 节点，加载所要查询集群的租户的环境变量脚本；
  1. 列出某个事件的详细信息：

    ```
    # heat event-show <STACK_NAME or STACK_ID> <RESOURCE_NAME> <EVENT_ID>
    ```

* 预期结果：

  * 成功列出某个事件的详细信息：

    ```
    # heat event-show coffee_withlb scaledown_policy 5eb5d1fc-ace4-4264-b7e1-28c0496d96bb
    +------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Property               | Value                                                                                                                                                                                            |
    +------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | event_time             | 2015-10-10T05:26:57Z                                                                                                                                                                             |
    | id                     | 5eb5d1fc-ace4-4264-b7e1-28c0496d96bb                                                                                                                                                             |
    | links                  | http://25.0.0.2:8004/v1/bf87349ae6704a87af75ebe9546d4af6/stacks/coffee_withlb/702c0b4d-751b-4fd1-9c35-f9bb9f8676b7/resources/scaledown_policy/events/5eb5d1fc-ace4-4264-b7e1-28c0496d96bb (self) |
    |                        | http://25.0.0.2:8004/v1/bf87349ae6704a87af75ebe9546d4af6/stacks/coffee_withlb/702c0b4d-751b-4fd1-9c35-f9bb9f8676b7/resources/scaledown_policy (resource)                                         |
    |                        | http://25.0.0.2:8004/v1/bf87349ae6704a87af75ebe9546d4af6/stacks/coffee_withlb/702c0b4d-751b-4fd1-9c35-f9bb9f8676b7 (stack)                                                                       |
    | logical_resource_id    | scaledown_policy                                                                                                                                                                                 |
    | physical_resource_id   | c1e03e6fb081466e856d5ec9cafd2a18                                                                                                                                                                 |
    | resource_name          | scaledown_policy                                                                                                                                                                                 |
    | resource_properties    | {                                                                                                                                                                                                |
    |                        |   "auto_scaling_group_id": "coffee_withlb-server_group-ttgtcdyquepm",                                                                                                                            |
    |                        |   "adjustment_type": "change_in_capacity",                                                                                                                                                       |
    |                        |   "scaling_adjustment": -1,                                                                                                                                                                      |
    |                        |   "cooldown": 60                                                                                                                                                                                 |
    |                        | }                                                                                                                                                                                                |
    | resource_status        | signal_COMPLETE                                                                                                                                                                                  |
    | resource_status_reason | alarm state changed from insufficient data to alarm (Transition to alarm due to 1 samples outside threshold, most recent: 0.107491856678)                                                        |
    | resource_type          | OS::Heat::ScalingPolicy                                                                                                                                                                          |
    +------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    ```

## 查询某个输出的详细信息

* 前提：

  * 已经创建好包含负载均衡的自动伸缩集群。

* 操作：

  1. 登录到 Controller 节点，加载所要查询集群的租户的环境变量脚本；
  1. 查询 Ceilometer 模块中的详细信息：

    ```
    # heat output-show <STACK_NAME or STACK_ID> <OUTPUT_NAME>
    ```

* 预期结果：

  * 成功查询 Ceilometer 模块中的详细信息：

    ```
    # heat output-show coffee_withlb ceilometer_query
    "ceilometer statistics -m cpu_util -q metadata.user_metadata.stack=702c0b4d-751b-4fd1-9c35-f9bb9f8676b7 -p 600 -a avg\n"
    ```

> ###### 说明：
> 根据上述查询输出列表的测试，可以查看的输出有：ceilometer_query、scale_up_url、scale_dn_url、website_url。
