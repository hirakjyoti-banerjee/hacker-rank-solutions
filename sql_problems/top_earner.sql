select earning ,count(*) from (select *,months*salary as earning,rank() over(order by months*salary desc) as rn from Employee) a
where rn=1
group by earning