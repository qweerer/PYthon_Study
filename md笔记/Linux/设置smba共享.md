# 安装
```
sudo apt install samba samba-commom
```
# 创建共享文件夹
```
mkdir share
```
修改权限
```
chomd 777 share
```
# 修改配置文件
```
vi /etc/samba/smb.conf
```
在末尾添加
```
[share]
    path = share文件夹目录
    available = yes
    browseable = yes
    writable = yes
```
# 创建samba账户
```
sudo touch /etc/samba/smbpasswd
```
```
smbpasswd -a 用户名（必须是系统的）
```
# 重启samba
```
sudo /etc/init.d/smbd restart
```
