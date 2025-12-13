
class Student:
    def __init__(self, i, n, d):  
        self.__id = i
        self.__name = n
        self.__dob = d

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob

    def display(self):
        print(self.__id, "-", self.__name, "-", self.__dob)


class Course:
    def __init__(self, iddd, coursename):
        self.__cid = iddd
        self.__cname = coursename

    def get_id(self):
        return self.__cid

    def get_name(self):
        return self.__cname

    def display(self):
        print(self.__cid, "-", self.__cname)


class MarkSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
    def input_students(self):
        num = int(input("How many students u want?: "))
        for i in range(0, num):
            self.add_student()

    def add_student(self):
        # I keep changing var names lol
        sID = input("Student ID pls: ")
        sName = input("Student Name pls: ")
        birthday = input("DOB: ")

        st = Student(sID, sName, birthday)
        self.students.append(st)

    def show_students(self):
        print("\nStudents List")
        for st in self.students:
            st.display()

    def input_courses(self):
        cc = int(input("How many courses u want?: "))
        for _ in range(cc):
            self.add_course()

    def add_course(self):
        cid = input("Course ID: ")
        cname = input("Course name: ")
        c = Course(cid, cname)
        self.courses.append(c)

    def show_courses(self):
        print("\nCourses")
        for c in self.courses:
            c.display()

    def input_marks(self):
        cid = input("Which course ID for marks?: ")
        all_ids = []
        for c in self.courses:
            all_ids.append(c.get_id())

        if cid not in all_ids:
            print("Course doesn't exist... I think?")
            return
        self.marks[cid] = []

        for st in self.students:
            try:
                mk = float(input("Enter mark for " + st.get_name() + ": "))
            except:
                print("not a number, setting 0")
                mk = 0
            self.marks[cid].append((st.get_id(), mk))

    def show_marks(self):
        course_id = input("Which course marks to show?: ")

        if course_id not in self.marks:
            print("No marks for this")
            return

        print("\nMarks for", course_id)

        for tup in self.marks[course_id]:
            sid = tup[0]
            mk = tup[1]

            name_found = None
            for s in self.students:
                if s.get_id() == sid:
                    name_found = s.get_name()
                    break

            print(name_found, "(", sid, "):", mk)

    def run(self):
        while True:
            print("1. Input Students")
            print("2. Input Courses")
            print("3. Input Marks")
            print("4. Show Students")
            print("5. Show Courses")
            print("6. Show Marks")
            print("0. Exit")

            ch = input("ur choice: ")

            if ch == "1":
                self.input_students()
            elif ch == "2":
                self.input_courses()
            elif ch == "3":
                self.input_marks()
            elif ch == "4":
                self.show_students()
            elif ch == "5":
                self.show_courses()
            elif ch == "6":
                self.show_marks()
            elif ch == "0":
                print("bye bye")
                break
            else:
                print("invalid choice??? try again maybe")

if __name__ == "__main__":
    sys = MarkSystem()
    sys.run()
