# log.io
[官方文档](https://github.com/NarrativeScience/log.io)
> 由于不想把log.io装到全局，所以新建一个项目文件安装这个服务

```shell
yarn add log.io
yarn add log.io-file-input
ln -s ./node_modules/log.io/config.json ./logio-server.json
touch ./logio-inputs.json
```

> 对于`log.io-file-input`, 需要设置环境变量, 可以使用PM2启动,并在pm2的配置文件中加入`env`
```js
 },{
 name : "log.io-file",
 script : "./node_modules/.bin/log.io-file-input",
 cwd : "/env/app-node/log.io.2/",
 max_memory_restart : "150M",
 out_file : "/env/app-node/log.io-file.log",
 env : {"LOGIO_FILE_INPUT_CONFIG_PATH":"/env/app-node/log.io.2/logio-inputs.json"},
```

