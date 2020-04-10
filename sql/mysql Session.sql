-- 1.别名查询
select
  goods_name as '商品名称',
  market_price as '商场价',
  shop_price as '本店价',
  click_count
from mr_sql.goods;
-- 2.多表查询出现相容
select
  user_address.mobile as '订单表中的电话号码',
  users.mobile as '用户收货信息表的电话号码',
  user_address.address
from mr_sql.user_address,
  mr_sql.users
where
  mr_sql.user_address.user_id = mr_sql.users.user_id;
-- 3.为使用聚合函数的列设置别名
select
  max(market_price) as '市场最高价',
  min(market_price) as '市场最低价'
from mr_sql.goods;
-- 4.去除重复数据
select
  user_id,
  district province
from mr_sql.users;
-- 5 限制查询(sql server 中使用top，mysql中使用LIMIT )
select
  goods_name,
  market_price
from mr_sql.goods
limit
  5;
-- 查看表中第3条数据开始的5条数据
select
  goods_name,
  market_price
from mr_sql.goods
limit
  2, 5;
-- 查询表中第3条数据开始的5条数据
select
  goods_name,
  market_price
from mr_sql.goods
limit
  5 OFFSET 2;
-- 6 连接列值
select
  name + cat_name as 品牌信息
from mr_sql.brand;
select
  goods_id as 商品ID,
  goods_name as 商品名称,(shop_price - cost_price) as 销售利润
from mr_sql.goods;
select
  goods_id as 商品ID,
  goods_name as 商品名称,(shop_price * sales_sum) as 销售额
from mr_sql.goods;

-- 7.使用表达式创建新列
select goods_id as 商品ID,goods_name as 商品名称,1+1,'字符'+'串列'from mr_sql.goods;
-- 8.where子句
select * from mr_sql.goods where goods_id=106;

select goods_id,goods_name,click_count from mr_sql.goods where click_count >50;
-- 不小于
select goods_id,goods_name,shop_price from mr_sql.goods where shop_price >= 2000;
-- 9.范围查询
select goods_id as 商品ID,goods_name as 商品名称,market_price as 市场价 from mr_sql.goods where market_price between 1000 and 3000;

-- 在between 中使用日期函数
select ISBN,BookName,INTime 数据录入时间 from mr_sql.bookinfo_zerobasis where INTime BETWEEN DATEADD(DAY,-1,datetime)AND datetime;
-- 查找不在两数之间的数据
select goods_id,goods_name,market_price from mr_sql.goods where market_price not BETWEEN 2000 and 3000;
-- 按指定日期查询数据
SELECT DAY(0) as MY_DAY1,day('02/03/2018') as MY_DAY2;
-- 逻辑运算符的优先级  NOT->AND->OR
-- 10 使用in运算符查询
select goods_name,shop_price from mr_sql.goods where shop_price in(3799-100,3799,3799+100)
-- 格式化结果集
SELECT user_id,email,reg_time,date_format(reg_time,'%Y/%m/%d') as teg_time2 FROM mr_sql.users limit 6;

-- 11 行数据过滤
SELECT (SELECT count(order_id) from mr_sql.orderform A where a.order_id >= B.order_id) 编号,order_id,order_sn,total_amount from mr_sql.orderform B order by 1;
-- 12 聚合函数 sum(求和)/avg(平均值)/min(最小)/max(最大)/count(district *)
select SUM(课程成绩) from mr_sql.grade;
-- 13 分组查询统计 group by
select cat_id as 商品ID, count(*) as 数量 from mr_sql.goods group by cat_id ;

SELECT cat_id as 商品种类ID,MIN(shop_price) 最低售价,max(cost_price) 最高成本价,avg(shop_price) 平均售价,count(*) as 数量 from mr_sql.goods group by cat_id order by max(cost_price) desc;
-- 14 多行子查询
select * from mr_sql.tb_book A where book_sort in(select tb_author_department from mr_sql.tb_book_author B where A.book_sort=B.tb_author_department) order by A.book_price
-- 过滤分组
select cat_id 商品种类ID,shop_price 商品售价,count(cat_id) 数量 from mr_sql.goods WHERE (store_count<1000) group by cat_id,shop_price HAVING(shop_price>(select avg(shop_price) from mr_sql.goods)) order by shop_price desc;
-- 15 内连接
SELECT gooods_id,goods_name,name from mr_sql.goods A inner join goods_type on A.goods_type=mr_sql.goods_type.id;
