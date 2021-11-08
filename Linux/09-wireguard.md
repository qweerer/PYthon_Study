# 09-wireguard

#linux 

## 生成密钥
```shell


# 服务器密钥
wg genkey | tee router-abc-private | wg pubkey > router-abc-public

# 客户端密钥·
wg genpsk > 00-phone-abc-sharekey
wg genkey | tee 00-phone-abc-private | wg pubkey > 00-phone-abc-public
````


```bash
# 1、设置网卡
ip link add wg0 type wireguard    # 自动处理内核模块加载
ip address add 192.168.3.1/24 dev wg0

# 用法：Usage: wg set <interface> [listen-port <port>] [fwmark <mark>] [private-key <file path>]  [peer <base64 public key> [remove] [preshared-key <file path>] [endpoint <ip>:<port>] [persistent-keepalive <interval seconds>] [allowed-ips <ip1>/<cidr1>[,<ip2>/<cidr2>]...] ]...
# 3、设置本地wg0网卡侦听端口与私钥
wg set wg0  listen-port 81  private-key /opt/www/00-config/wireguard-ssh/router-whyred-private

# 4、设置客户端公钥及允许客户端访问服务器的ip范围，多个时以逗号分隔（客户端需要生成相关信息才可执行下面的命令，方法同上）；设置保持连接（peer在nat防火墙后面的或者是动态地址的需要加上，服务器端一般有固定地址，所以不需要）
wg  set wg0  peer DePB2Q2Iq0e+9zkTXvR29qhlDQu5aPLMNPo25j4Taio=  allowed-ips 192.168.3.101/32 preshared-key /opt/www/00-config/wireguard-ssh/01-laptop-msi-sharekey persistent-keepalive 25

# 5、激活网卡
ip link set wg0 up
wg
```