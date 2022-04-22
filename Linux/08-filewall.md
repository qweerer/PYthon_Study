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

![7749898-d2d6c402a3a62680](7749898-d2d6c402a3a62680.png)


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
