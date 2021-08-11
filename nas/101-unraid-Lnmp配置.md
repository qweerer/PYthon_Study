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

### 01. 基于宿主机nginx的docker文件夹绑定

由于`nginx`使用远程`php-fpm`时，远程主机也需要有统一路径，所以需要双重绑定

```yml
app:
  image: nextcloud:fpm
  volumes:
 - /mnt/user/00-docker-conf/nextcloud/html/:/var/www/html/
 - /mnt/user/00-docker-conf/nextcloud/html/:/mnt/user/00-docker-conf/nextcloud/html/

 - /mnt/user/00-docker-conf/nextcloud/apps/:/var/www/html/custom_apps/
 - /mnt/user/00-docker-conf/nextcloud/apps/:/mnt/user/00-docker-conf/nextcloud/html/custom_apps/

 - /mnt/user/00-docker-conf/nextcloud/config/:/var/www/html/config/
 - /mnt/user/00-docker-conf/nextcloud/config/:/mnt/user/00-docker-conf/nextcloud/html/config/

 - /mnt/user/01-nextcloud/:/var/www/html/data
 - /mnt/user/01-nextcloud/:/mnt/user/00-docker-conf/nextcloud/html/data/

 - /mnt/user/www-data/:/mnt/user/www-data/
```

在宿主机中设置软链接

```shell
ln -s /mnt/user/00-docker-conf/nextcloud/apps /mnt/user/00-docker-conf/nextcloud/html/custom_apps

ln -s /mnt/user/00-docker-conf/nextcloud/config /mnt/user/00-docker-conf/nextcloud/html/config

ln -s /mnt/user/01-nextcloud /mnt/user/00-docker-conf/nextcloud/html/data
```

### 02. 基于docker版nginx的文件夹绑定

docker版nextcloud:fpm设置, 除了自身的网页文件映射外，还需加入`www-data`的映射, `www-data`为自己的网页文件地址

```yml
 ports:
 - 18506:9000
 volumes:
 - /mnt/user/www-data/:/mnt/user/www-data/
 
 - /mnt/user/00-docker-conf/nextcloud/html/:/var/www/html/
 - /mnt/user/00-docker-conf/nextcloud/apps/:/var/www/html/custom_apps/
 - /mnt/user/00-docker-conf/nextcloud/config/:/var/www/html/config/
 - /mnt/user/01-nextcloud/:/var/www/html/data
```

docker版nginx设置,

- 第1个目录映射为与`docker版nextcloud:fpm`同步的`www-data`路径, 
- 第2, 3个目录映射为`nginx.conf`的文件映射, 文件为[[./unraid/docker-nginx.conf]]

```yml
 ports:
 - 8080:80
 - 82:82
 - 18505:18505

 links:
 - nextcloud-fpm

 volumes:
 - /mnt/user/www-data/:/mnt/user/www-data/
 - /boot/system_replace/nginx_conf/:/boot/system_replace/nginx_conf/
 - /mnt/user/00-docker-conf/nginx/nginx.conf:/etc/nginx/nginx.conf:ro

 - /mnt/user/00-docker-conf/nextcloud/html/:/var/www/html/
 - /mnt/user/00-docker-conf/nextcloud/apps/:/var/www/html/custom_apps/
 - /mnt/user/00-docker-conf/nextcloud/config/:/var/www/html/config/
 - /mnt/user/01-nextcloud/:/var/www/html/data
```

### 03. docker中安装php扩展

docker版php的扩展源码存储与`/usr/src/php/ext`路径下, 如果docker带了源码

```shell
docker-php-ext-install
docker-php-ext-enable
```

如果没有, 则需先下载源码

```shell
docker cp /boot/system_replace/root/swoole.tgz containerID:/root
docker exec -it containerID /bin/bash
mkdir /usr/src/php/ext/swoole -p
tar zxvf  /root/swoole.tgz -C /root
cp /root/swoole-4.6.7 /usr/src/php/ext/swoole
docker-php-ext-install swoole
rm /root/*
php --ri swoole
```

### 03. docker中安装gd插件

```shell
#容器中
#echo "deb http://mirrors.163.com/debian/ stretch main contrib non-free\ndeb http://mirrors.163.com/debian/ stretch-updates main contrib non-free\ndeb http://mirrors.163.com/debian/ stretch-backports main contrib non-free" > /etc/apt/sources.list  #软件源修改为网易镜像站源
apt update  #更新软件源
apt install -y libwebp-dev libjpeg-dev libpng-dev libfreetype6-dev #安装各种库
docker-php-source extract #解压源码
cd /usr/src/php/ext/gd  #gd源码文件夹
docker-php-ext-configure gd --with-webp-dir=/usr/include/webp --with-jpeg-dir=/usr/include --with-png-dir=/usr/include --with-freetype-dir=/usr/include/freetype2   #准备编译
docker-php-ext-install gd   #编译安装
php -m | grep gd
#重启容器
```

## mariadb

数据库安装很简单, 模板在[mysql与nextcloud.yml](./unraid/mysql与nextcloud.yml)中, 需要注意的是, 由于mariadb可能不能设置初始密码, 所以需要运行

1. 进入docker然后修改密码

```shell
docker exec -it containerID /bin/bash
mysql -h主机地址  -u用户名  -p用户密码
```

```SQL
set password for root@% = password('123');
SELECT User, Host, Password FROM mysql.user;
```

2. 设置服务器权限时可以用`127.%`,`172.17.%`,`192.168.2.%`,`localhost`,来涵盖大多数内网访问情况, 记住一定要增加`localhost`访问权限, 否则命令行就无法进入数据库了.
