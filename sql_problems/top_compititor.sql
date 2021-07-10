select b.hacker_id,b.name from 
submissions a inner join hackers b on a.hacker_id=b.hacker_id
inner join challenges c on a.challenge_id=c.challenge_id
inner join difficulty d on c.difficulty_level=d.difficulty_level
where a.score=d.score
group by b.hacker_id,b.name
having count(*)>1
order by count(*) desc,b.hacker_id