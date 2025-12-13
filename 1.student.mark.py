students = []       
courses = []        
marks = {}          

def input_number_of_students():
    n = int(input("Enter number of students: "))
    for _ in range(n):
        input_student_info()


def input_student_info():
    sid = input("Student ID: ")
    name = input("Name: ")
    dob = input("Date of Birth: ")
    students.append({
        "id": sid,
        "name": name,
        "dob": dob
    })


def input_number_of_courses():
    n = int(input("Enter number of courses: "))
    for _ in range(n):
        input_course_info()


def input_course_info():
    cid = input("Course ID: ")
    name = input("Course name: ")
    courses.append({
        "id": cid,
        "name": name
    })


def input_marks_for_course():
    cid = input("Enter course ID to input marks: ")
    if cid not in [c["id"] for c in courses]:
        print("Course not found!")
        return

    print("Entering marks for course {cid}")

    marks[cid] = []
    for st in students:
        m = float(input(f"Mark for student {st['name']} ({st['id']}): "))
        marks[cid].append((st["id"], m))

def list_courses():
    print("\nList of Courses")
    for c in courses:
        print(f"{c['id']} - {c['name']}")


def list_students():
    print("\nList of Students")
    for s in students:
        print(f"{s['id']} - {s['name']} - {s['dob']}")


def show_marks_for_course():
    cid = input("Enter course ID to show marks: ")

    if cid not in marks:
        print("No marks for this course!")
        return

    print("Marks for Course {cid}")
    for sid, m in marks[cid]:
        student_name = next(s["name"] for s in students if s["id"] == sid)
        print("{student_name} ({sid}): {m}")

def main():
    actions = {
        "1": self.input_students,
        "2": self.input_courses,
        "3": self.input_marks,
        "4": self.show_students,
        "5": self.show_courses,
        "6": self.show_marks
    }

    while True:
        print("1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks")
        print("4. Show Students")
        print("5. Show Courses")
        print("6. Show Marks")
        print("0. Exit")

        ch = input("ur choice: ")

        if ch == "0":
            print("bye bye")
            break

        action = actions.get(ch)
        if action:
            action()
        else:
            print("invalid choice??? try again maybe")
            
if __name__ == "main":
    main()
