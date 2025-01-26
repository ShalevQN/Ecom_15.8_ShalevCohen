--a
SELECT courses.course_id, courses.course_name, lecturers.first_name as lecturer_name from courses
inner join lecturers ON courses.lecturer_id = lecturers.lecturer_id;
--b
SELECT Courses.course_id, Courses.course_name, lecturers.first_name as lecturer_name from Courses
left join Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id
where Courses.lecturer_id is NULL;
--c
SELECT Courses.course_id, Courses.course_name, Lecturers.first_name as lecturer_name from Courses
left join Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id;
--d
SELECT Lecturers.first_name, Courses.course_id, Courses.course_name from Lecturers
left join Courses on Lecturers.lecturer_id = Courses.lecturer_id
where courses.course_id is not NULL;
--e
SELECT Lecturers.first_name, courses.course_id from Lecturers
left join Courses on Lecturers.lecturer_id = Courses.lecturer_id
where Courses.lecturer_id is NULL;
--f
SELECT Lecturers.first_name, Courses.course_id, Courses.course_name from Lecturers
left join Courses on Lecturers.lecturer_id = Courses.lecturer_id;
--g
SELECT Courses.course_id, Courses.course_name as course_name, Lecturers.first_name as lecturer_name from Courses
full join Lecturers on Courses.lecturer_id = Lecturers.lecturer_id;
--h
SELECT Courses.course_id, Courses.course_name as course_name, Lecturers.first_name as lecturer_name from Courses
cross join Lecturers;