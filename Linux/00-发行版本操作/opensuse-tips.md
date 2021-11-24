# opensuse

- 自动不安装推荐

```
vim /etc/zypp/zypp.conf
solver.onlyRequires = true
```

- 删除多余包

```shell
zypper al openssh-server vim wget
zypper rm -u openssh-clients
zypper al dhcp dhcp-client iptables
zypper rm -u samba NetworkManager iw iproute2
zypper rm -u e2fsprogs
```

- 使用`wicked`

```shell
wicked show all
wicked show-xml eth0
wicked ifreload br0
```

## 微码
suse中微码为`microcode_ctl` 、`linux-firmware` 和 `ucode-intel`这三个包

```shell


```