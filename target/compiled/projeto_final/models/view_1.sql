select
	avg(walmart.profit / walmart.sales) as margin,
	walmart.category
from walmart
group by category
order by margin desc