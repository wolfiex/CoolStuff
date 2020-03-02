# local yum 

```
mkdir -p ~/rpm
yumdownloader --destdir ~/rpm --resolve vim-common

mkdir ~/centos
cd ~/centos && rpm2cpio ~/rpm/x.rpm | cpio -id


```

BashRC

```
export PATH="$HOME/centos/usr/sbin:$HOME/centos/usr/bin:$HOME/centos/bin:$PATH"

L='/lib:/lib64:/usr/lib:/usr/lib64'
export LD_LIBRARY_PATH="$L:$HOME/centos/usr/lib:$HOME/centos/usr/lib64"
```
