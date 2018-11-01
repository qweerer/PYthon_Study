# PostgreSQL第一天

`默认为port为'5432'`

## 检测是否安装完成

1. 打开`SQL SHELL`回车
2. 查看是否出错

## 链接

```shell
psql -U username -h ipaddress -d dbname
psql -U postgres -h ipaddress -d dbname
```

## 切换数据库

```shell
\c dbname
```

## 常用命令

### 列出所有的数据库

```shell
\l
```

 Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------|----------|----------|-------------|-------------|-----------------------
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres postgres=CTc/postgres
 wzz       | wzz      | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 

### 列出当前书库库下的表

```shell
\d
```

### 显示当前数据库

```shell
select current_database();
```

### 列出表的所有字段

```shell
\d tablename
```

### 查看表的基本情况

```shell
\d+ tablename
```

