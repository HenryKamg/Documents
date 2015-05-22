# 安装插件

## 注意

Fuel节点在部署时会自动尝试安装以下插件，此处需要使用以下命令查看已经安装成功的插件列表。

```
[fuel]# fuel plugins -l
id | name           | version | package_version
---|----------------|---------|----------------
1  | cinder_eqlx    | 1.0.0   | 1.0.0          
2  | neutron-fwaas  | 1.0.0   | 1.0.0          
3  | neutron-lbaas  | 1.0.0   | 1.0.0          
4  | neutron-vpnaas | 1.0.0   | 1.0.0
```

如某个插件未成功安装，使用以下命令尝试重新安装对应插件。

## 安装Cinder Eqlx插件

* 登录Fuel节点，执行以下命令，安装Cinder Eqlx插件。

 ```
# fuel plugins --install /opt/eayunstack/cinder_eqlx-1.0.0.fp
```

## 安装Neutron LBaaS插件

* 登录Fuel节点，执行以下命令，安装Neutron LBaaS插件。

 ```
# fuel plugins --install /opt/eayunstack/neutron-lbaas-1.0.0.fp
```

## 安装Neutron FWaaS插件

* 登录Fuel节点，执行以下命令，安装Neutron FWaaS插件。

 ```
# fuel plugins --install /opt/eayunstack/neutron-fwaas-1.0.0.fp
```

## 安装Neutron VPNaaS插件

* 登录Fuel节点，执行以下命令，安装Neutron VPNaaS插件。

 ```
# fuel plugins --install /opt/eayunstack/neutron-vpnaas-1.0.0.fp
```
