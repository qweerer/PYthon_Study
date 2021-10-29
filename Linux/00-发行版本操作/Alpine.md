

[包搜索地址](https://pkgs.alpinelinux.org/packages)

## 安装 docker

-   Docker 包位于“社区”存储库中，因此如果 apk 添加失败且具有不可满足的约束，则需要编辑`/etc/apk/repositories`文件以添加（或取消注释）一行，如：[http://dl-cdn.alpinelinux.org/alpine/latest-stable/community](http://dl-cdn.alpinelinux.org/alpine/latest-stable/community)
-   更新索引存储库`apk update`
-   开始安装`apk add docker`
-   要在引导时启动 Docker 守护程序，请运行：`rc-update add docker boot`
-   然后手动启动 Docker 守护程序，运行：`rc-service docker start`
-   参考[alpinelinux Docker](https://wiki.alpinelinux.org/wiki/Docker)

### 运行

-   启动`service docker start`
-   `docker run hello-word`

### 开启docker远程访问管理

```shall
vi /etc/conf.d/docker

# any other random options you want to pass to docker
DOCKER_OPTS="-H=unix:///var/run/docker.sock -H=0.0.0.0:2375"
```