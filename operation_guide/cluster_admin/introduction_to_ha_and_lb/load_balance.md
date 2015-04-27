# HAProxy
HAProxy 是 EayunStack 平台中实现负载均衡的服务程序。

配置文件为： `/etc/haproxy/haproxy.cfg` ，主要内容包括：

    global
      daemon
      group  haproxy
      log  /dev/log local0
      maxconn  16000
      pidfile  /var/run/haproxy.pid
      stats  socket /var/lib/haproxy/stats
      tune.bufsize  32768
      tune.maxrewrite  1024
      user  haproxy

    defaults
      log  global
      maxconn  8000
      mode  http
      option  splice-auto
      retries  3
      stats  enable
      timeout  http-request 10s
      timeout  queue 1m
      timeout  connect 10s
      timeout  client 1m
      timeout  server 1m
      timeout  check 10s

    listen Stats *:10000
      mode http
      stats enable
      stats uri /
      stats refresh 5s
      stats show-node
      stats show-legends
      stats hide-version

    include conf.d/*.cfg

EayunStack 平台中各服务组件的具体配置在 `/etc/haproxy/conf.d` 目录下。
