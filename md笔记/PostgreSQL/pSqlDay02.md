# pSqlDay02

## 1、按照每个品牌做数据拆解

```sql
SELECT DISTINCT 品牌名称 FROM data3;

CREATE TABLE data_brand AS
    SELECT 品牌名称,商品id,COUNT(商品id) FROM data3 GROUP BY 品牌名称,商品id;
SELECT * FROM data_brand ORDER BY 品牌名称 LIMIT 20;
```

- 汇总数据 → 不同品牌的商品数量
- 这里去除掉了“日期”字段的影响

```sql
CREATE TABLE brand_price AS SELECT DISTINCT 品牌名称,商品id FROM data3;
```

- 创建空表格，只包括不同品牌的品牌名称、商品id

```sql
CREATE TABLE brand_price1105 AS SELECT 商品id,价格 FROM data3 WHERE 日期 = '2016-11-05';
CREATE TABLE brand_price1106 AS SELECT 商品id,价格 FROM data3 WHERE 日期 = '2016-11-06';
CREATE TABLE brand_price1107 AS SELECT 商品id,价格 FROM data3 WHERE 日期 = '2016-11-07';
CREATE TABLE brand_price1108 AS SELECT 商品id,价格 FROM data3 WHERE 日期 = '2016-11-08';
CREATE TABLE brand_price1109 AS SELECT 商品id,价格 FROM data3 WHERE 日期 = '2016-11-09';
CREATE TABLE brand_price1110 AS SELECT 商品id,价格 FROM data3 WHERE 日期 = '2016-11-10';
CREATE TABLE brand_price1111 AS SELECT 商品id,价格 FROM data3 WHERE 日期 = '2016-11-11';
CREATE TABLE brand_price1112 AS SELECT 商品id,价格 FROM data3 WHERE 日期 = '2016-11-12';
CREATE TABLE brand_price1113 AS SELECT 商品id,价格 FROM data3 WHERE 日期 = '2016-11-13';
CREATE TABLE brand_price1114 AS SELECT 商品id,价格 FROM data3 WHERE 日期 = '2016-11-14';
```

- 将不同品牌的商品价格按照“日期”导出

```sql
ALTER TABLE brand_price ADD COLUMN date1105 numeric;
ALTER TABLE brand_price ADD COLUMN date1106 numeric;
ALTER TABLE brand_price ADD COLUMN date1107 numeric;
ALTER TABLE brand_price ADD COLUMN date1108 numeric;
ALTER TABLE brand_price ADD COLUMN date1109 numeric;
ALTER TABLE brand_price ADD COLUMN date1110 numeric;
ALTER TABLE brand_price ADD COLUMN date1111 numeric;
ALTER TABLE brand_price ADD COLUMN date1112 numeric;
ALTER TABLE brand_price ADD COLUMN date1113 numeric;
ALTER TABLE brand_price ADD COLUMN date1114 numeric;
```

- 增加列 → 用于填充不同品牌的不同商品每日价格

```sql
UPDATE brand_price SET date1105 = 价格 FROM brand_price1105 WHERE brand_price1105.商品id = brand_price.商品id;
UPDATE brand_price SET date1106 = 价格 FROM brand_price1106 WHERE brand_price1106.商品id = brand_price.商品id;
UPDATE brand_price SET date1107 = 价格 FROM brand_price1107 WHERE brand_price1107.商品id = brand_price.商品id;
UPDATE brand_price SET date1108 = 价格 FROM brand_price1108 WHERE brand_price1108.商品id = brand_price.商品id;
UPDATE brand_price SET date1109 = 价格 FROM brand_price1109 WHERE brand_price1109.商品id = brand_price.商品id;
UPDATE brand_price SET date1110 = 价格 FROM brand_price1110 WHERE brand_price1110.商品id = brand_price.商品id;
UPDATE brand_price SET date1111 = 价格 FROM brand_price1111 WHERE brand_price1111.商品id = brand_price.商品id;
UPDATE brand_price SET date1112 = 价格 FROM brand_price1112 WHERE brand_price1112.商品id = brand_price.商品id;
UPDATE brand_price SET date1113 = 价格 FROM brand_price1113 WHERE brand_price1113.商品id = brand_price.商品id;
UPDATE brand_price SET date1114 = 价格 FROM brand_price1114 WHERE brand_price1114.商品id = brand_price.商品id;
```

- 更新数据 → 填充不同品牌的不同商品每日价格

```sql
DELETE FROM brand_price WHERE date1105 IS NULL
    or date1106 IS NULL
    or date1107 IS NULL
    or date1108 IS NULL
    or date1109 IS NULL
    or date1110 IS NULL
    or date1111 IS NULL
    or date1112 IS NULL
    or date1113 IS NULL
    or date1114 IS NULL;
```

- 删除缺失值

## 2、筛选出不同品牌的数据

```sql
CREATE TABLE xybc AS SELECT * FROM brand_price WHERE 品牌名称 = '相宜本草';
CREATE TABLE nwy AS SELECT * FROM brand_price WHERE 品牌名称 = '妮维雅';
CREATE TABLE zrt AS SELECT * FROM brand_price WHERE 品牌名称 = '自然堂';
```

- 筛选出3个品牌 → 相宜本草、妮维雅、自然堂

```sql
\COPY xybc TO 'C:\Users\iHJX_Alienware\Desktop\数据整理_相宜本草.csv' WITH CSV HEADER;
\COPY nwy TO 'C:\Users\iHJX_Alienware\Desktop\数据整理_妮维雅.csv' WITH CSV HEADER;
\COPY zrt TO 'C:\Users\iHJX_Alienware\Desktop\数据整理_自然堂.csv' WITH CSV HEADER;


-- 导出数据