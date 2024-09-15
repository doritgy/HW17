#a
select c.*, l.first_name, l.last_name
from courses c
inner join lecturers l
on c.lecturer_id = l.lecturer_id

 #b
select  c.*, l.first_name, l.last_name
from courses c left join lecturers l
on c.lecturer_id = l.lecturer_id
where c.lecturer_id NOTNULL

#c
select * from courses c
left join lecturers l
on c.lecturer_id = l.lecturer_id

#d
SELECT  l.first_name, l.last_name, l.email, c.course_name
from courses c inner join lecturers l
on c.lecturer_id = l.lecturer_id

#e
SELECT  l.first_name, l.last_name, l.email, c.course_name
from lecturers l left join courses c
on l.lecturer_id = c.lecturer_id
where c.lecturer_id ISNULL

#f
select l.first_name, l.last_name, l.email, c.course_name
from lecturers l left join courses c
on c.lecturer_id  = l.lecturer_id

#g
select l.first_name, l.last_name, l.email, c.course_name
from lecturers l full outer join courses c
on c.lecturer_id  = l.lecturer_id

#h
select l.first_name, l.last_name, c.course_name from lecturers l
left join courses c
on l.lecturer_id = c.lecturer_id
where c.lecturer_id  NOTNULL