```bash
export EDITOR=vim
# create a dir storage
lxc storage create pool dir source=/opt/lxd
lxc profile edit default
lxc storage delete default

lxc image list tuna-images:alpine/edge/cloud/amd64
lxc image copy tuna-images:5aa8aaa3baa2 local: --copy-aliases 

lxc launch 5aa8aaa3baa2 alpine-test # -c security.privileged=true
lxc list -c n,s,4,image.description:image
```