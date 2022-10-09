[oznu/alpine-node: Node.js binaries for Alpine Linux on x86_64, armhf and aarch64. (github.com)](https://github.com/oznu/alpine-node)


[pnpm文档](https://pnpm.io/npmrc)

## 查看

```bash
# 查看全局已安装
npm ls -g
npm ls -g --depth 0
# 查看项目中已安装
npm ls --depth 0
# 如果只想显示生产环境依赖的包
npm ls --depth 0 --prod
# 只显示开发环境依赖的包
npm ls --depth 0 --dev


# yarn
yarn global list
```

### pnpm
```bash
pnpm --version    # pnpm版本
pnpm config set store-dir "C:\Develop\msys2\opt\node-app\.pnpm-store"    # pnpm全局仓库路径(类似 .git 仓库)
pnpm config set global-dir "D:\nodejs\pnpm\pnpm-global"    # pnpm全局安装路径
pnpm config set global-bin-dir "C:\Develop\nodejs\bin"    # pnpm全局bin路径
pnpm config set state-dir "C:\Develop\msys2\opt\node-app"    # pnpm创建pnpm-state.json文件的目录
pnpm config set cache-dir "D:\nodejs\pnpm\cache"    # pnpm全局缓存路径
./node_modules/.bin/pnpm store path
pnpm store prune
```

## 卸载 & 安装

```
npm install -g pnpm

npm uninstall -g <package>
npm uninstall <package>



```




