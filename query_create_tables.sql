CREATE TABLE student(
	student_id SERIAL PRIMARY KEY NOT NULL,
	name VARCHAR(128) NOT NULL,
	surename VARCHAR(128) NOT NULL,
	class int
);

CREATE TABLE teacher(
	teacher_id SERIAL PRIMARY KEY,
	name VARCHAR(128) NOT NULL,
	surename VARCHAR(128) NOT NULL
);


CREATE TABLE course(
	course_id SERIAL PRIMARY KEY,
	name VARCHAR(128),
	teacher_id INT,
	CONSTRAINT fk_teacher FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id)
	);
	

CREATE TABLE student_course(
	student_id INT,
	course_id INT,
	CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES student(student_id),
	CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES course(course_id)
);

delete from student
where name = 'Petr'

Insert Into student (name, surename, class)
values
	('Petr', 'Kopecký', 5 ),
	('Tomas', 'Jedno', 9),
	('Jan', 'Nezkusil',2);
	
select * from student

Insert into teacher (name, surename)
values 
	('Jan', 'Vševěd'),
	('Helana', 'Přísná');

Insert  Into course (name, teacher_id)
Values
	('Matematika', 1),
	('Informatika', 1),
	('Angličtina', 2);
	
Insert into student_course (student_id, course_id)
values
	(2,1),
	(2,2),
	(2,3),
	(3,2),
	(4,1),
	(4,3);


SELECT student.student_id, student.name, student.surename, student.class, string_agg(course.name, ', ') 
FROM student
JOIN student_course 
	ON student.student_id = student_course.student_id
JOIN course 
	ON student_course.course_id = course.course_id
GROUP BY student.student_id
ORDER BY student.student_id


SELECT course.course_id, course.name, CONCAT(teacher.name, ' ', teacher.surename) "Teacher Name",count(student_course.student_id) "Count of students"  
FROM course
JOIN teacher 
	ON course.teacher_id = teacher.teacher_id
JOIN student_course 
	ON course.course_id = student_course.course_id
GROUP BY course.course_id, course.name, "Teacher Name"
ORDER BY course.course_id 

