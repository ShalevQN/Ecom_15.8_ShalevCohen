--1
SELECT Courses.course_id, Courses.name, Lecturers.name as lecturer_name from Courses
inner join Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id;

--2
SELECT Courses.course_id, Courses.name, Lecturers.name as lecturer_name from Courses
left join Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id;

--3
SELECT Lecturers.name, Courses.course_id, Courses.name from Lecturers
left join Courses on Lecturers.lecturer_id = Courses.lecturer_id;

--4
SELECT Courses.course_id, Courses.name from Courses
left join Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id
where Courses.lecturer_id is NULL;

--5
SELECT Lecturers.name from Lecturers
left join Courses on Lecturers.lecturer_id = Courses.lecturer_id
where Courses.lecturer_id is NULL;

--6
SELECT Courses.course_id, Courses.name as course_name, Lecturers.name as lecturer_name from Courses
full join Lecturers on Courses.lecturer_id = Lecturers.lecturer_id;

--7
SELECT Courses.course_id, Courses.name as course_name, Lecturers.name as lecturer_name from Courses
full join Lecturers on Courses.lecturer_id = Lecturers.lecturer_id
where Lecturers.lecturer_id is NULL or Courses.course_id is NULL;

--8
SELECT Lecturers.name from Lecturers
where Lecturers.name like "%i%";

--9
SELECT count(*) from Lecturers;

--10
SELECT count(*) from Courses;