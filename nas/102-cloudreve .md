# cloudreve


先创建目录与文件

```shell
mkdir -p /mnt/user/00-docker-conf/cloudreve \
    && touch /mnt/user/00-docker-conf/cloudreve/conf.ini \
    && touch /mnt/user/00-docker-conf/cloudreve/cloudreve.db
```

配置运行docker, 文件为[[./unraid/cloudreve.yml]]

完成后运行`docker logs -f cloudreve`获取密码

## nginx设置

```conf
server {
  listen 99;
  location / {
    proxy_pass http://127.0.0.1:5212;
    proxy_set_header Host $host;
  }
}
```

