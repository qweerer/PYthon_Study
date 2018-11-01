# PostgreSQL第一天

`默认为port为'5432'`

## 检测是否安装完成

1. 打开`SQL SHELL`回车
2. 查看是否出错

## 链接

```SQL
psql -U username -h ipaddress -d dbname
psql -U postgres -h ipaddress -d dbname
```

## 查看用户

```sql
\du
```

## 数据库操作

### 创建数据库

```SQL
CREATE DATABASE wzy_tyk charset=utf8;
```

### 切换数据库

```SQL
\c dbname
```

## 表操作

### 创建表

```sql
CREATE TABLE data(
    update_time date,
    id text,
    title text,
    price numeric,
    sale_count int,
    comment_count int,
    店名 text
    );
```

### 复制csv数据

```sql
 \COPY data FROM 'C:\Users\iHJX_Alienware\Desktop\体验课资料_双十一淘宝美妆数据.csv' WITH CSV HEADER;
```

- 导入数据
- with csv header → 代表将表头作为列名，导入时忽略第一行

### 数据查看

```sql
\d data;
```

### 查看数据属性

```SQL
SELECT * FROM data WHERE update_time IS NULL LIMIT 10;
SELECT * FROM data WHERE id IS NULL LIMIT 10;
SELECT * FROM data WHERE title IS NULL LIMIT 10;
SELECT * FROM data WHERE price IS NULL LIMIT 10;
SELECT * FROM data WHERE sale_count IS NULL LIMIT 10;
SELECT * FROM data WHERE comment_count IS NULL LIMIT 10;
SELECT * FROM data WHERE 店名 IS NULL LIMIT 10;
```

- 查看缺失值
- 可以看到，sale_count/comment_count 是包含缺失值的

### 删除缺失值

```aql
DELETE FROM data WHERE sale_count IS NULL;
DELETE FROM data WHERE comment_count IS NULL;
```

- 数据清洗 → 删除缺失值

### 查看前几个数据

```sql
SELECT * FROM data LIMIT 10;
SELECT * FROM data LIMIT 5 OFFSET 5;
```

- LIMIT → 限制返回数量，
- LIMIT 5 OFFSET 5 → 从第五条数据开始看后5条数据

```sql
SELECT 店名,title FROM data LIMIT 20;
```

- 查看数据“店名”、“title”字段的前20条数据

```sql
SELECT 店名,title,price FROM data ORDER BY price DESC LIMIT 20;
```

- 按照价格排序，查看数据
- DESC → 倒序

### 查看唯一值

```sql
SELECT DISTINCT 店名 FROM data;
```

- 查看有多少个品牌
- SELECT DISTINCT → 去重

```sql
SELECT DISTINCT title FROM data WHERE 店名 = '娇兰';
SELECT DISTINCT title,price FROM data WHERE 店名 = '娇兰' and price > 1000;
```

- 查看SKII品牌的商品
- 查看SKII品牌价格大于1000的商品
- WHERE → 判断语句

### 查看特定值

```sql
SELECT DISTINCT title,id,price,update_time FROM data 
    WHERE update_time = '2016-11-10' or update_time = '2016-11-11' 
    ORDER BY id LIMIT 20;
```

- 查看不同商品，11.11和11.10两天的价格情况
- 这里通过id的排序来查看

### 修改列名

```sql
ALTER TABLE data RENAME COLUMN id TO 商品id;
ALTER TABLE data RENAME COLUMN update_time TO 日期;
ALTER TABLE data RENAME COLUMN title TO 商品名称;
ALTER TABLE data RENAME COLUMN price TO 价格;
ALTER TABLE data RENAME COLUMN sale_count TO 销售量;
ALTER TABLE data RENAME COLUMN comment_count TO 评价数量;
ALTER TABLE data RENAME COLUMN 店名 TO 品牌名称;
```

### 列计算

```sql
ALTER TABLE data ADD 销售额 numeric;
UPDATE data SET 销售额 = 价格 * 销售量;
```

- ALTER TABLE ... ADD ... → 添加列
- UPDATE ... SET ... → 计算列

```sql
CREATE TABLE data2 AS
    SELECT 商品id,MAX(价格),MIN(价格) FROM data GROUP BY 商品id;
ALTER TABLE data2 ADD 折扣力度 numeric;
UPDATE data2 SET 折扣力度 = min/max;
ALTER TABLE data2 RENAME COLUMN 商品id TO 商品id2;
CREATE TABLE data3 AS
    SELECT * FROM data,data2 WHERE data.商品id = data2.商品id2;
ALTER TABLE data3 DROP max;
ALTER TABLE data3 DROP min;
ALTER TABLE data3 DROP 商品id2;
```

- 计算折扣力度
- 新建表格，包括不同商品的价格最大最小值
- 计算折扣力度
- 修改列名，连接表格
- 删除多余列

### 数据导出

```sql
\COPY data3 TO 'C:\Users\iHJX_Alienware\Desktop\清洗结果数据.csv' WITH CSV HEADER;
```

## 常用命令

### 列出所有的数据库

```SQL
\l
```

 Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges
-----------|----------|----------|-------------|-------------|-----------------------
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres postgres=CTc/postgres
 wzz       | wzz      | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 

### 列出当前书库库下的表

```SQL
\d
```

### 显示当前数据库

```SQL
select current_database();
```

### 列出表的所有字段

```SQL
\d tablename
```

### 查看表的基本情况

```SQL
\d+ tablename
```