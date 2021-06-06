
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
docker exec --user www-data nextcloud(容器的名字或id) php cron.php
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
