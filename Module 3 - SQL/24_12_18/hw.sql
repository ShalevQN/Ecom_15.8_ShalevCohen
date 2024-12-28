--1
SELECT avg(grade), exam_year from grades
group by exam_year;

--2
SELECT avg(grade), student_name from grades
where exam_year = 2024
group by student_name;

--3
SELECT exam_year, subject_name, max(grade) from grades
group by exam_year, subject_name;

--3.5
SELECT exam_year, subject_name, min(grade) from grades
group by exam_year, subject_name;

--4
SELECT exam_year, subject_name, count(*) as exam_count from grades
group by exam_year, subject_name;

--5
SELECT subject_name, avg(grade) from grades
group by subject_name
having avg(grade) > 85;

--6
SELECT grade, count(*) from grades
where grade > 90
group by grade;