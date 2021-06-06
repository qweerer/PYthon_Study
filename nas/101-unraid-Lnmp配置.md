# LNMP配置

## 系统自身nginx与php

- 由于unraid自身将php-fpm作为环境变量无法改变，所以只能新建一个nginx进程

在usersprit中创建

```sh
#!/bin/bash
#cp /boot/system_replace/nginx_conf/* /etc/nginx/conf.d/
sleep 120
nginx  -c /boot/system_replace/nginx.conf
alias nginx02='nginx -c /boot/system_replace/nginx.conf'
```

nginx02 的主配置

[nginx.conf](nas\unraid\system_replace\nginx.conf)

## docker-php

- 由于自己需要使用nextcloud，所以将nextcloud作为php的docker, 对应的docker的`yml`版配置[mysql与nextcloud.yml](./unraid/mysql与nextcloud.yml)





