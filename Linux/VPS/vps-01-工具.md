# vps-01-工具

## 3.1 SuperSpeed.sh - VPS三网测速脚本  
使用方法(需要以root用户执行)  

```
sudo -i  
bash <(curl -Lso- https://git.io/superspeed_uxh)
```

## 3.2 Speedtest-cli - 测试VPS到任意区域的速度  
安装 https://www.speedtest.net/zh-Hans/apps/cli  
使用
```shell
# 显示附近测速服务器  
# 如果需要更多，可访问https://www.speedtest.net/api/js/servers?engine=js  
speedtest -L  
# 指定服务器测速  
speedtest -s  
```
以腾讯云香港轻量（Debian10）举例子：  

```shell
sudo apt-get install curl  
curl -s https://install.speedtest.net/app/cli/install.deb.sh | sudo bash  
sudo apt-get install speedtest  
speedtest -L
```

## 4.4 besttrace - 指定IP路由测试工具  
下载地址 https://cdn.ipip.net/17mon/besttrace4linux.zip  
使用 

```shell
bestrace <ip或域名>  
  
查看本地IP：https://ip.skk.moe/  
  
wget https://cdn.ipip.net/17mon/besttrace4linux.zip  
  
apt install zip  
  
unzip besttrace4linux.zip  
  
chmod +x besttrace  
  
  
./besttrace -q1 -g cn  8.8.8.8     # ./besttrace -q1 -g cn IP   换成你本
```