import  math
import numpy  as  np
import curses

class Student:
	def __iniit__(self, i,n, d):
		self.__id =  i
		self.__name = n
		self.__ dob =  d
		self._courses = []

	def get_id(self):
		return  self.__id

	def  get_name(self):
		return self.__name

	def add_course_mark(self, credit, mark):
		mark = math.floor(mark * 10) / 10
		self.__courses.append((credit, mark))

	def calculate_gpa(self):
		if not self.__courses:
			return 0.0

			credit  = np.arry([c[0] for  c  in self.__courses])
			marks = np.arry([c[1] for c in self.__courses])

			gpa = np.sum(credits * marks) / np.sum(credits)
			return round(gpa, 2)

	def  display(self):
		print(self.__id,"",self.__name,"GPA",  self.calculate_gpa())

class Course:

	def __iniit__(self, cid, name,  credit):
		self.__cid = cid
		self.__name = name
		self.__credit  =  credit

	def  get_id(self):
		return self.__cid
	def  get_credit(self):
		return self.__credit
	def display(self):
		print(self.__cid, "-", self.__name, "(", self.__credit, "credits )")
name = input("Student name: ")
dob = input("DOB: ")
self.students.append(Student(sid, name, dob))


def input_courses(self):
n = int(input("How many courses?: "))
for _ in range(n):
cid = input("Course ID: ")
cname = input("Course name: ")
credit = int(input("Credit: "))
self.courses.append(Course(cid, cname, credit))


def input_marks(self):
cid = input("Enter course ID for marks: ")
course = None
for c in self.courses:
if c.get_id() == cid:
course = c
break


if course is None:
print("Course not found")
return


for s in self.students:
try:
mk = float(input(f"Mark for {s.get_name()}: "))
except:
mk = 0
s.add_course_mark(course.get_credit(), mk)


def sort_by_gpa(self):
self.students.sort(key=lambda s: s.calculate_gpa(), reverse=True)


def show_students(self):
self.sort_by_gpa()
for s in self.students:
s.display()


def curses_ui(stdscr, students):
curses.curs_set(0)
stdscr.clear()
stdscr.addstr(0, 2, "STUDENT GPA LIST (DESC)", curses.A_BOLD)


row = 2
for s in students:
stdscr.addstr(row, 2, f"{s.get_id()} | {s.get_name()} | GPA: {s.calculate_gpa()}")
row += 1


stdscr.addstr(row + 1, 2, "Press any key to exit")
stdscr.refresh()
stdscr.getch()


def main():
sys = MarkSystem()
sys.input_students()
sys.input_courses()
sys.input_marks()
sys.sort_by_gpa()
curses.wrapper(curses_ui, sys.students)


if __name__ == "__main__":
main()