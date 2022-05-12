# Cmder

## 下载

```url
http://cmder.net/
```

## 设置全局右键

在管理员下:

```shell
Cmder.exe /REGISTER ALL
```

## 乱码

> 环境变量中设置

```shell
set LANG=zh_CN.UTF-8
set LC_ALL=zh_CN.utf8
```

> git出现乱码

```shell
git config --gloabal il8n.logoutputencoding utf-8
```

## 使用外部链接打开

>按键&宏 > 高亮

```shell
start "run" "%3" -cur_console:n
```

### 修改标识符

```shell
 if not prompt_lambSymbol then
      prompt_lambSymbol = "λ"
    end
```
