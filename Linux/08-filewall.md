# 08-filewall

#linux 

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

```
sudo firewall-cmd --add-service=cockpit
sudo firewall-cmd --add-service=cockpit --permanent

```
> 查看规则

## iptables

```shell
iptables -P INPUT DROP
iptables -D INPUT 6
iptables -t filter -D INPUT -s 0.0.0.0/0 -j DROP
iptables -t filter -D INPUT -j REJECT --reject-with icmp-host-prohibited
```

## ufw

```shell
ufw deny from 208.176.0.50
sudo ufw allow 53
sudo ufw allow 22/tcp
```