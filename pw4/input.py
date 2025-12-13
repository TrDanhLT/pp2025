def input_students(system):
n = int(input("How many students?: "))
for _ in range(n):
sid = input("Student ID: ")
name = input("Name: ")
dob = input("DOB: ")
system.add_student(sid, name, dob)




def input_courses(system):
n = int(input("How many courses?: "))
for _ in range(n):
cid = input("Course ID: ")
name = input("Course name: ")
credit = int(input("Credit: "))
system.add_course(cid, name, credit)




def input_marks(system):
cid = input("Enter course ID for marks: ")
course = system.find_course(cid)
if not course:
print("Course not found")
return
for s in system.students:
try:
mk = float(input(f"Mark for {s.get_name()}: "))
except:
mk = 0
s.add_course_mark(course.get_credit(), mk)