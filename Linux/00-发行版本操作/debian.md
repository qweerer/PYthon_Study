# debian

```shell
sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
sed -i 's/mirrors.163.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

apt install apt-transport-https ca-certificates

sed -i 's|http://mirrors.ustc.edu.cn|https://mirrors.tuna.tsinghua.edu.cn|g' /etc/apt/sources.list

apt install unzip wget 
```


## 清理包

使用`dpkg --list`可以查看所有包的状态，其中前两位表示状态，第一位为期望的状态，第二位为实际的状态。可以大致理解为：当我们输入安装命令时，第一位置为i（表示install），当命令完成时，第二位置为i。  
更细节的表示可以参考文档，或者查看：[https://linuxprograms.wordpress.com/2010/05/11/status-dpkg-list/](https://linuxprograms.wordpress.com/2010/05/11/status-dpkg-list/)

一个常见的非理想状态是：第一位为r（removed），第二位为c（Cfg-file存在)。

```bash
# 查看rc状态的包
dpkg --list |grep "^rc"
# 清除
dpkg --list |grep "^rc" | cut -d " " -f 3 | xargs sudo dpkg --purge
# 或者使用aptitude
sudo aptitude purge "~c"
```