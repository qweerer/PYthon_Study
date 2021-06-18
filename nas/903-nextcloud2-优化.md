
## 无权限管理

安装nextcloud

注意一点，如果nextcloud指定的存储位置的硬盘格式是NTFS，启动的时候可能会提示权限不能为0777之类的，需要在config/config.php中添加'check_data_directory_permissions' => false用来跳过校验，如果硬盘的ext4就没有权限的问题。

## 设置redis

在config/config.php文件中添加如下

```php
    'memcache.locking' => '\\OC\\Memcache\\Redis',
    'memcache.distributed' => '\\OC\\Memcache\\Redis',
     'redis' => 
      array (
     	'host' => '192.168.1.185',
     	'port' => 6379,
  ),
```

## 设置定时任务

定时任务执行cron.php定时任务，不然nextcloud会在页面刷新的时候执行，导致页面卡顿,这里借助mov的计划任务，在计划任务中添加一天计划任务即可

```shell
docker exec nextcloud(容器的名字或id) php cron.php
//如果硬盘格式是ext4 ，需要使用www-data的权限执行
docker exec --user www-data nextcloud-fpm php cron.php
```

```/etc/crontab
*/5  *  *  *  * docker exec --user www-data nextcloud(容器的名字或id) php cron.php
```

## 添加文件到nextcloud

把自己本地的文件复制到nextcloud相应的用户目录中，nextcloud中并不会显示，因为数据库中没有相应的数据，这里就需要手动执行命令，nextcloud才会把文件数据添加进数据库里

```shell
docker exec nextcloud php occ files:scan --all
//或
docker exec --user www-data nextcloud php occ files:scan --all
```


## MariaDB 数据库的优化

在数据库容量小于1GB时，且内存足够的情况下：

mariadb/custom.cnf

```cnf
[mysqld]
innodb_buffer_pool_size=1G
innodb_io_capacity=4000
```

## [#](https://tvtv.fun/pc-to-nas/23th.html#php-fpm-的优化)PHP-FPM 的优化

/usr/local/etc/php-fpm.d/

```shell
cp /usr/local/etc/php-fpm.d/* /var/www/html/config/111/
cp /var/www/html/config/111/* /usr/local/etc/php-fpm.d/
```

```conf
[www]
pm = dynamic
pm.max_children = 60
pm.start_servers = 6
pm.min_spare_servers = 3
pm.max_spare_servers = 9
```

## [#](https://tvtv.fun/pc-to-nas/23th.html#通过-occ-命令修改配置)通过 OCC 命令修改配置

通过 OCC 命令可以直接修改 Nextcloud 的各项配置，避免手动修改 config.php 文件经常出现的格式错误和拼写错误。

用户身份

你需要使用在安装 Nextcloud 时通过 PUID 参数指定的用户身份去执行OCC命令，其他任何用户（包括root在内）都无法正常执行这个命令。

### 添加受信任的域名

**查看已经设置的域名/IP**

```
$ docker exec -it nextcloud occ config:system:get trusted_domains

192.168.1.118
```

**添加新的域名**

以下命令会在受信任的域名数组中，添加 `omv5.local` 域名，它数组中的编号为 `1`。

```
$ docker exec -it nextcloud occ config:system:set trusted_domains 1 --value omv5.local
```

注意编号

> 在 PHP 数组中，编号是以 `0` 开始的，即第一个域名的编号为`0`，值为`192.168.1.118`，第二个域名的编号为`1`，值为`omv5.local`。

### 设置预览图尺寸

**设置预览图的最大宽度**，以下命令将预览图的最大宽度设置为`1000`像素，默认值为`4096`像素。

```
$ docker exec -it nextcloud-fpm occ config:system:set preview_max_x --value=1000
```

****设置预览图的最大高度**，以下命令将预览图的最大宽度设置为`800`像素，默认值为`4096`像素。**

```
$ docker exec -it nextcloud-fpm occ config:system:set preview_max_y --value=800
```


在config/config.php文件中添加如下

```php
 'preview\_max\_x' \=> 1000,
 'preview\_max\_y' \=> 800,
```
 
## 检查CPU是否支持AES-NI指令集

```
$ grep flags /proc/cpuinfo
```