
https://github.com/multiarch/qemu-user-static/blob/master/README.md

https://www.cnblogs.com/Wu13241454771/p/14349439.html
## 使docker可执行虚拟化
```shell
$ docker run --rm -t arm64v8/ubuntu uname -m
standard_init_linux.go:211: exec user process caused "exec format error"

$ docker run --rm --privileged multiarch/qemu-user-static:x86_64-aarch64 -p yes
$ docker run --rm --privileged multiarch/qemu-user-static --reset -p yes

$ docker run --rm -t arm64v8/ubuntu uname -m 
aarch64
```
## 部署 Docker:

```shell
docker pull --platform arm64 vaultwarden/server:latest
docker inspect vaultwarden/server

openssl rand -base64 48

docker run -itd --name vaultwarden \
-e ADMIN_TOKEN=token \
-e SIGNUPS_ALLOWED=false \
-e INVITATIONS_ALLOWED=true \
-e WEBSOCKET_ENABLED=true \
-e SHOW_PASSWORD_HINT=false \
-e LOG_FILE=/data/vaultwarden.log \
-e LOG_LEVEL=warn \
-e EXTENDED_LOGGING=true \
-e ROCKET_PORT=18000 \
-p 18000:18000 \
-v /storage/emulated/0/00-www-data/18000-vaultwarden/:/data/ \
--restart=always \
4c99199a7cb8 

vaultwarden/server:latest \
```

## 导出chroot环境

```shell
mkdir rootfs
cd rootfs
docker export fb36d714da86 -o vaultwarden_arm64.tar
tar -xf vaultwarden_arm64.tar
chroot /root/rootfs /bin/bash
```

## 参考代码

```shell
docker run \
-itd \
-e PGID=1000 \
-e PUID=1000 \
--name=bitwardenrs \
--net=你的自定义网络名称 \
-e TZ=Asia/Shanghai \
-e SERVER_ADMIN_EMAIL=你的email \
-e SIGNUPS_ALLOWED=false \
-e INVITATIONS_ALLOWED=true \
-e WEBSOCKET_ENABLED=true \
-e ADMIN_TOKEN=你的token \
-p 8086:80/tcp \
-v /opt/docker/appdata/bitwarden:/data:rw 
bitwardenrs/server:latest


sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /root/app-data/ssl/key.pem -out /root/app-data/ssl/pub.pem
```

## 安装openrc管理服务

在`/etc/init.d`中创建服务文件

```shell
#!/sbin/openrc-run

name="app-nps-c"
command="/root/nps-c/app-nps-c.sh"
command_args=""
pidfile="/var/run/app-nps-c.pid"
extra_commands="log"

depend() {
	need net
	after firewall
}

log() {
	tail -f /root/www/01-log/nps-c.log
}
```
`command`中的脚本文件如下
```shell
#!/bin/sh
nohup /root/nps-c/npc -server=192.168.2.1:8284 -vkey=2222 >> /root/www/01-log/nps-c.log 2>&1 & 
echo $! > /var/run/app-nps-c.pid
```

## XXXX

详见：[servicectl-github](https://github.com/smaknsk/servicectl)

### 安装

```shell
wget https://github.com/smaknsk/servicectl/archive/1.0.tar.gz
tar -xf 1.0.tar.gz -C /usr/local/lib/
ln -s /usr/local/lib/servicectl-1.0/servicectl /usr/local/bin/servicectl
ln -s /usr/local/lib/servicectl-1.0/serviced /usr/local/bin/serviced
```

### Usage

```shell
sudo servicectl action service
```

This command just exec `${action}` from `file /usr/lib/systemd/system/${service}.service` If passed action enable or disable, servicectl create or delete symlink on `${service}.service` for use serviced.

Params:

action - can be {start, stop, restart, reload, enable, disable}
service - file name in folder /usr/lib/systemd/system/