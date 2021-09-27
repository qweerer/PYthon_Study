
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

docker run -d --name vaultwarden \
-e ADMIN_TOKEN=token \
-e SIGNUPS_ALLOWED=false \
-e INVITATIONS_ALLOWED=true \
-e WEBSOCKET_ENABLED=true \
-e SHOW_PASSWORD_HINT=false \
-e ROCKET_PORT=18000 \
-p 18000:18000 \
-v /storage/emulated/0/00-www-data/18000-vaultwarden/:/data/ \
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
```

