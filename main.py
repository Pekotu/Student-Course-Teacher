"""
This tool allow create, display and change information about Students, Teachers and Courses. 
It means that students visit some curses and teachers are teaching on curses. 
Each course can have just one teacher and many students.
Each student can visit 0 to many courses
Each teacher can teach in 0 to many courses  
All data are stored in Posgres SQL database 
This tool is consol app with main many which alow to do all actions  
"""
import psycopg2
import os
########################################################

def print_menu():
    content= """
MAIN MENU:
    (1) Display Students
    (2) Display Courses
    (3) Display Teachers
    (4) Add Student
    (5) Add Courses
    (6) Add Teacher
    (7) Edit/Delete Student
    (8) Edit/Delete Courses
    (9) Edit/Delete Teacher
"""
    print(content)
    operation = input("write number from brackets to call operation: ")
    return operation
########################################################

def get_all_db_table(table):
    with conn, conn.cursor() as cur:
        cur.execute(f"select * from {table};")
        data = cur.fetchall()

    return data
########################################################

def get_all_students_with_courses():
    
    with conn, conn.cursor() as cur:
        cur.execute(f"""
SELECT student.student_id, student.name, student.surename, student.class, string_agg(course.name, ', ') 
FROM student
JOIN student_course 
	ON student.student_id = student_course.student_id
JOIN course 
	ON student_course.course_id = course.course_id
GROUP BY student.student_id
ORDER BY student.student_id;""")
        data = cur.fetchall()

    return data

########################################################
def display_students():
    data_student = get_all_students_with_courses()
    print("Students:")
    
    for row in data_student:
        text = f"{'ID:':<5}{row[0]:<6}{'Name, Surename:':<17}{row[1]+ " " + row[2]:<20}{'Class:':<8}{row[3]:<5}{'Courses:':<10}{row[4]}"
        print(text)


########################################################

def get_all_courses_with_teachers_students():
    
    with conn, conn.cursor() as cur:
        cur.execute(f"""
SELECT course.course_id, course.name, CONCAT(teacher.name, ' ', teacher.surename) "Teacher Name",count(student_course.student_id) "Count of students"  
FROM course
JOIN teacher 
	ON course.teacher_id = teacher.teacher_id
JOIN student_course 
	ON course.course_id = student_course.course_id
GROUP BY course.course_id, course.name, "Teacher Name"
ORDER BY course.course_id ;""")
        data = cur.fetchall()

    return data

######################################################
def display_courses():
    data_course = get_all_courses_with_teachers_students()
    
    
    print("Courses:")
    for row in data_course:
        text = f"{'ID:':<5}{row[0]:<6}{'Course Name:':<14}{row[1]:<17}{'Teacher Name:':<15}{row[2]:<20}{'Students in Course:':<21}{row[3]:<6}"
        print(text)

########################################################


def get_all_teachers_with_corses():
    
    with conn, conn.cursor() as cur:
        cur.execute(f"""SELECT teacher.teacher_id, teacher.name, teacher.surename, string_agg(course.name, ', ') 
FROM teacher
LEFT JOIN course
	ON teacher.teacher_id = course.teacher_id
GROUP BY teacher.teacher_id, teacher.name, teacher.surename
ORDER BY teacher.teacher_id;""")
        data = cur.fetchall()

    return data

######################################################
def display_teachers():
    data_teachers = get_all_teachers_with_corses()
    
    print("Courses:")
    for row in data_teachers:
        text = f"{'ID:':<5}{row[0]:<6}{'Name, Surename:':<17}{row[1]+ " " + row[2]:<20}{'Courses:':<10}{row[3]}"
        print(text)

########################################################

#----------main------------
if __name__ == "__main__":    

    conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST", "localhost"),
    database = os.getenv("POSTGRES_DATABASE", "DB_Student_Curse_Teacher"),
    user = os.getenv("POSTGRES_USER", "postgres"),    
    password = os.getenv("POSTGRES_PASSWORD", "postgres"),
    port = os.getenv("POSTGRES_PORT", "5432")
    )

    
    
    display_students()
    display_courses()
    display_teachers()
    """
    operation = int(print_menu())

    match operation: 
        case 1:
            Display_Students()
        case 2:
            display_courses()
        case 3:    
            display_teachers()
        case 4:
            Add_Student()
        case 5:    
            Add_Courses()
        case 6:
            Add_Teacher()
        case 7:    
            Edit_Student()
        case 8:
            Edit_Courses()
        case 9:    
            Edit_Teacher()"""