

# 1. 下载缺失的字体文件
下载缺失的字体文件，然后复制到Linux系统中的`/usr/share/fonts`文件夹中。

国外下载地址：<font color=blue>www.dropbox.com/s/lfy4hvq95ilwyw5/wps_symbol_fonts.zip<font>

国内下载地址：<font color=blue>pan.baidu.com/s/1eS6xIzo<font>

（上述数据来源网络，侵删）

下载完成后，解压并进入目录中，继续执行：
```
sudo cp * /usr/share/fonts
```
# 2. 执行以下命令,生成字体的索引信息：
```
sudo mkfontscale

sudo mkfontdir
```
# 3. 运行fc-cache命令更新字体缓存。
```
sudo fc-cache
```
# 4. 重启wps即可，字体缺失的提示不再出现。