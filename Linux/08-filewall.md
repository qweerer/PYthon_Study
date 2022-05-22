# 08-filewall

#linux 

> 工具：`ntop` `iptraf` `iftop`

- Quagga路由器

## iptables

> 查看是否启用

```shell
lsmod | egrep 'nat|filter' 

# 加载内核模块
modprobe ip_tables
modprobe iptable_filer
modprobe iptable_nat
modprobe ip_conntrack
modprobe ip_conntrack_ftp
modprobe ip_nat_ftp
modprobe ipt_state
```

```shell
iptables save
iptables -P INPUT DROP
iptables -D INPUT 6
iptables -A INPUT   -p tcp --dport 22 -j DROP
iptables -I INPUT 2 -p tcp --dport 22 -j DROP
iptables -A INPUT   -s 192.168.1.1/24 -j DROP    #源ip
iptables -A INPUT ! -s 113.108.118.250  -j DROP  #非源ip
iptables -A INPUT ! -d 192.168.1.20   -j DROP    #非目标ip
iptables -A INPUT -i eth0 -o eth1 -s 192.168.1.114  -j DROP #从eth0进入,从eth1出
iptables -A INPUT -p icmp --icmp-type 8 -j DROP  #封ping

iptables -t filter -D INPUT -s 0.0.0.0/0 -j DROP
iptables -t filter -D INPUT -j REJECT --reject-with icmp-host-prohibited

iptables -F #清空所有规则
iptables -X #清空用户链
iptables -Z #清空计数器

# -p all|tcp|udp|icmp
# -m state --state NEW|ESTABLISHED|RELATED|INVALID (新|已建立|正在启动|非法)
# -m limit
# 		--limit n/{second|minute|hour} 限制速率
#       --limit-burst 5                同一时间允许请求的个数,默认为5
iptables -A FORWARD -d 192.168.2.20 -p icmp --icmp-type 8 -m limit --limit 20/min --limit-burst 3 -j ACCEPT  #封ping
```

> 查看规则

```bash
iptables -S
iptables -S -t nat
```

### 匹配

可直接使用,不依赖于其他条件或扩展. `包括网络协议、IP地址、网络接口等条件`
1. **协议匹配:：** -p 协议名  
  - 常用协议：tcp、udp、icmp、all（所有）

2. **地址匹配：** -s 源地址 -d 目的地址  
例：

```shell
-s 192.168.20.10  ##源地址 默认子网掩码32位的主机地址
-d 192.168.20.0/24  ##目标地址为 网段地址
```

3. **接口匹配：** -i 入站网口 -o 出站网口（网卡）  

```shell
iptables -t nat -A POSTROUTING -s 192.168.20.0/24 -i ens33 -p all -j ACCEPT
                                                  -o ens37
```

4. **端口匹配：**- -sport 源端口、- -dport 目的端口
> 要求以特定的协议匹配作为前提  
> 包含端口、TCP标记、ICMP类型等条件  

```shell
iptables -A INPUT -s 192.168.20.0/24 -p udp --deport 53 -j ACCEPT
iptables -A OUTPUT -s 192.168.20.0/24 -p udp --sport 53:20:21 -j ACCEPT
```

5. **ICMP类型匹配：**–icmp-type ICMP类型  
> 要求以特定的协议匹配作为前提  
> 包含端口、TCP标记、ICMP类型等条件  
> ICMP类型：8（request）拒绝、0（reply）丢弃、3（host unreachable）主机不可达  

例：

```javascript
-p icmp --icmp-type 8
```

#### 显式匹配

要求以"-m 扩展模块"的形式明确指出类型. 包含多端口、MAC地址、IP范围、数据包状态等条件  
6. **多端口匹配：**  


```javascript
-m multiport --sports 源端口列表  
-m multiport --dports 目的端口列表  
-m multiport --deport 20,21,53,80
```

7. **IP范围匹配：**-m iprange --src-range 源IP范围  

```javascript
-m iprange --dst-range 目标IP范围  
-m iprange --src-range 192.168.20.10-192.168.20.20
-m iprange --dst-range 192.168.20.10-192.168.20.20
```

8. **MAC地址匹配：**-m mac --mac-source MAC地址  

```javascript
-m mac --mac-source 00:0c:29:7d:b8:d5
```

9. **状态匹配：**-m state --state 连接状态  
  - NEW：与任何连接无关  
  - ESTABLISHED：相应请求或已建连接  
  - RELATED：与已有连接有相关性的，如FTP数据连接  
例：

```javascript
-m -state --state NEW -p tcp !--syn -j DROP
```



### NAT
```shell
# 开启路由功能
echo "net.ipv4.ip_forward=1" > /etc/sysctl.conf  ##配置路由功能配置文件
sysctl -p  ##更新路由配置
```

> `SNAT`与`DNAT`只需要配置一次iptables, 返程数据会自动更改收到`dst addr`

#### SNAT

原理：修改数据包中的源IP地址  
作用：局域网主机共享单个公网IP地址接入Internet  
配置：nat表中的POSTROUTING链（出战）

> 主机A想访问互联网上的主机C，首先将请求数据包发送到防火墙所在主机B，B收到后将数据包源地址改为本机公网网卡的ip，然后经互联网发送给C。
```shell
iptables -t nat -A POSTROUTING -s 192.168.20.0/24 -o ens37 -j SNAT--to-source 218.29.30.31
##  -s 内网网段
##  -o 防火墙服务器外网网卡
##  -j SNAT策略
##  --to-source 防火墙服务器外网口IP地址
```
#### DNET
搜索：`iptables DNAT`

```shell
# 开启路由功能
echo "net.ipv4.ip_forward=1" > /etc/sysctl.conf  ##配置路由功能配置文件
sysctl -p  ##更新路由配置
```

原理：修改数据包中的目标IP地址  
作用：将位于企业局域网中的服务器进行发布至互联网  
配置：nat表中的PREROUTING链（入站）

> 互联网主机C想访问企业内部的web服务器A，但A的地址是私有地址，无法直接访问。此时，C可以访问防火墙的公网地址，C的请求数据包到达防火墙B后，在B上将请求数据包的目标地址进行修改，并将数据包发送给A。

```shell
iptables -t nat -A PREROUTING -d 218.29.30.31 -i ens37 -j DNAT --to-destination 192.168.20.10
##  -d 防火墙服务器外网口IP地址
##  -i 防火墙服务器外网网卡
##  -j DNAT策略
##  --to-destination 内网服务器IP地址
```

```shell
# 这条命令用处很少, 让`本机出口`目标为 **192.168.2.20:55** 的流量转到 192.168.2.21:53
iptables -t nat -A OUTPUT -p tcp -d 192.168.2.20 --dport 55 -j DNAT --to-destination 192.168.2.21:53
```



![7749898-d2d6c402a3a62680|L](7749898-d2d6c402a3a62680.png)


### 查看刚才发生的网络链接
```
cat /proc/net/nf_conntrack
```

### netfilter

五表：**filter** **nat** **mangle** **raw** **security**
五链条: **prerouting** **input** **forward** **output** **postrouting**


## firewalld

```shell
firewall-cmd --reload
sudo firewall-cmd --get-zones

#==========[out]==========#    
block dmz docker drop external home internal public trusted work

sudo firewall-cmd --get-default-zone

#==========[out]==========#    
public

firewall-cmd --get-zone-of-interface
firewall-cmd --list-all
firewall-cmd --list-all-zones
```

```shell
sudo firewall-cmd --set-default-zone=public
firewall-cmd --change-zone=enp0s3 --zone=trusted
firewall-cmd --add-port=2222/tcp 
firewall-cmd --zone=public --add-port=2222/tcp 
firewall-cmd --permanent --zone=public --add-port=100-500/tcp

```

```shell
sudo firewall-cmd --add-service=cockpit
sudo firewall-cmd --add-service=cockpit --permanent

```


## ufw

```shell
ufw default allow|deny
ufw deny from 208.176.0.50
sudo ufw allow 53
sudo ufw allow 22/tcp


ufw [--dry-run] [delete] [insert NUM] [prepend] allow|deny|reject|limit [in|out] [log|log-all] [ PORT[/PROTOCOL] | APPNAME ] [comment COMMENT]
    

ufw [--dry-run] [rule] [delete] [insert NUM] [prepend] allow|deny|reject|limit [in|out [on INTERFACE]] [log|log-all] [proto PROTOCOL] [from ADDRESS [port PORT | app APPNAME ]] [to ADDRESS [port PORT | app APPNAME ]] [comment COMMENT]
```

# route

```shell
ifconfig eth0:1 192.168.70.1 netmask 255.255.255.0
route #查看路由表

# 路由表添加（网段与主机），del与add方法相同
route add -net 10.0.0.1 netmask 255.255.255.0 gw 192.168.0.1
route add -host 10.0.0.2 gw 192.168.0.1
```

## ip工具

```shell
ip macaddress
# 添加ip地址
ip addr add 192.168.70.10/24 dev eth0

# 添加route
ip route add 10.0.0.2/24 via 192.168.70.1

# 查看网络邻居
ip n/neigh
```
