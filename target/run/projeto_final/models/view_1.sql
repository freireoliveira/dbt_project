
  create view "projeto"."public"."view_1__dbt_tmp" as (
    select
	avg(walmart.profit / walmart.sales) as margin,
	walmart.category
from walmart
group by category
order by margin desc
  );