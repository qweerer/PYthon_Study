# LNMP配置

## 系统自身nginx与php

- 由于unraid自身将php-fpm作为环境变量无法改变，所以只能新建一个nginx进程

在usersprit中创建

```shell
#!/bin/bash
#cp /boot/system_replace/nginx_conf/* /etc/nginx/conf.d/
sleep 120
nginx  -c /boot/system_replace/nginx.conf
alias nginx02='nginx -c /boot/system_replace/nginx.conf'
```

nginx02 的配置文件

![[unraid/system_replace/nginx.conf]] ![[unraid/system_replace/fastcgi_params]] ![[./unraid/system_replace/nginx_conf/18505-nextcloud.conf]] ![[./unraid/system_replace/nginx_conf/18500-homer.conf]]


## docker-php

- 由于自己需要使用nextcloud，所以将nextcloud作为php的docker, 对应的docker的`yml`版配置![mysql与nextcloud.yml](./unraid/mysql与nextcloud.yml)

### docker文件夹绑定

由于`nginx`使用远程`php-fpm`时，远程主机也需要有统一路径，所以需要双重绑定

```yml
app:
  image: nextcloud:fpm
  volumes:
    - /mnt/user/00-docker-conf/nextcloud/html:/var/www/html
```

### docker中安装php扩展


> adfasdf


