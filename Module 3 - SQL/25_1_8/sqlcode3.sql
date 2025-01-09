CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT NOT NULL,
    hours INTEGER NOT NULL);

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL);

CREATE TABLE grades (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    grade INTEGER NOT NULL,
    UNIQUE(student_id, course_id),
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);


	
INSERT INTO students (name, email)
VALUES ('Shalev', 'shalevch1@gmail.com'), 
('Bob', 'bob@gmail.com');

INSERT INTO courses (topic, hours)
VALUES('History', 20),
('Math', 26);


INSERT INTO grades (student_id, course_id, grade)
VALUES
    (1, 1, 93),
    (1, 2, 54),
    (2, 1, 78),
    (2, 2, 83);

SELECT courses.topic as course, avg(grades.grade) as average_grade
from grades
join courses on grades.course_id = courses.course_id
group by courses.course_id, courses.topic;