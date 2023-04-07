select
    avg(date(walmart.ship_date) - date(walmart.order_date)) as order_ship_delta,
	walmart.state
from walmart
group by walmart.state
order by order_ship_delta asc