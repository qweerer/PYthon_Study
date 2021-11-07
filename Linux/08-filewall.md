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
```

```shell
sudo firewall-cmd --set-default-zone=public
firewall-cmd --change-zone=enp0s3 --zone=trusted
firewall-cmd --add-port=2222/tcp 
firewall-cmd --add-port=2222/tcp --zone=public
firewall-cmd --permanent --zone=public --add-port=100-500/tcp
```

> 查看规则