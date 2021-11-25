# npm包管理器

## 配置源

```bash
npm config get registry
npm config set registry http://registry.npm.taobao.org/

npx nrm use taobao
npx nrm use npm
```

## 部署

```bash
npm install -g yarn pm2 nodemon
```

## 缓存设置

```bash
yarn cache clean
npm cache clean --force

yarn config set cache-folder "/c/Develop/nodejs/node-cache/yarn"
npm config set cache "/c/Develop/nodejs/node-cache/npm"
npm config set prefix "D:\Program Files\npm_global"
npm config ls
yarn config list
```

## 其他命令

```bash
npm list -g
npm list vue
npm install npm@5.9.1
npm install -save moduleName
npm install -sav-dev moduleName

npm install --production
```


```bash
yarn buils
```

# pm2

```shell
npm install -g pm2
```

## 使用方法

```bash
$ pm2 start app.js

$ pm2 start bashscript.sh
$ pm2 start python-app.py --watch
$ pm2 start binary-file -- --port 1520

$ pm2 startup # 产生 init 脚本 保持进程活着

$ pm2 list # 显示所有进程状态  
$ pm2 show 0 # 显示0进程详细信息  
$ pm2 monit # 监视所有进程  
$ pm2 logs # 显示所有进程日志  
$ pm2 restart all # 重启所有进程  
$ pm2 reload all # 0秒停机重载进程 (用于 NETWORKED 进程)

$ pm2 stop all # 停止所有进程  
$ pm2 delete all # 杀死全部进程


$ pm2 save # 保存当前增加的应用
```

## 参数说明

```bash
# Specify an app name
--name <app_name>

# Watch and Restart app when files change
--watch

# Set memory threshold for app reload
--max-memory-restart <200MB>

# 标准输出日志文件的路径。
-o --output <path>

# 错误输出日志文件的路径。
-e --error <path>

# Specify log file
--log <log_path>

# Pass extra arguments to the script
-- arg1 arg2 arg3

# Delay between automatic restarts
--restart-delay <delay in ms>

# Prefix logs with time
--time

# Do not auto restart app
--no-autorestart

# Specify cron for forced restart
--cron <cron_pattern>

# Attach to application log
--no-daemon

# 启用多少个实例，可用于负载均衡。如果`-i 0`或者`-i max`，则根据当前机器核数确定实例数目。
-i --instances

# 排除监听的目录/文件，可以是特定的文件名，也可以是正则。比如`--ignore-watch="test node_modules "some scripts""`
--ignore-watch
```

```bash
$ pm2 restart app_name
$ pm2 reload app_name
$ pm2 stop app_name
$ pm2 delete app_name
```


## 环境切换

在实际项目开发中，我们的应用经常需要在多个环境下部署，比如开发环境、测试环境、生产环境等。在不同环境下，有时候配置项会有差异，比如链接的数据库地址不同等。

对于这种场景，pm2也是可以很好支持的。首先通过在配置文件中通过`env_xx`来声明不同环境的配置，然后在启动应用时，通过`--env`参数指定运行的环境。

### 环境配置声明

首先，在配置文件中，通过`env`选项声明多个环境配置。简单说明下：

-   `env`为默认的环境配置（生产环境），`env_dev`、`env_test`则分别是开发、测试环境。可以看到，不同环境下的`NODE_ENV`、`REMOTE_ADDR`字段的值是不同的。
-   在应用中，可以通过`process.env.REMOTE_ADDR`等来读取配置中生命的变量。

```javascript
  "env": {
    "NODE_ENV": "production",
    "REMOTE_ADDR": "http://www.example.com/"
  },
  "env_dev": {
    "NODE_ENV": "development",
    "REMOTE_ADDR": "http://wdev.example.com/"
  },
  "env_test": {
    "NODE_ENV": "test",
    "REMOTE_ADDR": "http://wtest.example.com/"
  }
```

### 启动指明环境

假设通过下面启动脚本（开发环境），那么，此时`process.env.REMOTE_ADDR`的值就是相应的 [http://wdev.example.com/](http://wdev.example.com/) ，可以自己试验下。

```powershell
pm2 start app.js --env dev
```

## 负载均衡

命令如下，表示开启三个进程。如果`-i 0`，则会根据机器当前核数自动开启尽可能多的进程。

```powershell
pm2 start app.js -i 3 # 开启三个进程
pm2 start app.js -i max # 根据机器CPU核数，开启对应数目的进程 
```

参考文档：[点击查看](http://pm2.keymetrics.io/docs/usage/cluster-mode/#automatic-load-balancing)