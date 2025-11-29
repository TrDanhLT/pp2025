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

    print(f"Entering marks for course {cid}")

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

    print(f"Marks for Course {cid}")
    for sid, m in marks[cid]:
        student_name = next(s["name"] for s in students if s["id"] == sid)
        print(f"{student_name} ({sid}): {m}")

def main():
    while True:
        print("\n===== Student Mark Management =====")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks for a course")
        print("0. Exit")

        choice = input("Your choice: ")

        if choice == "1":
            input_number_of_students()
        elif choice == "2":
            input_number_of_courses()
        elif choice == "3":
            input_marks_for_course()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_marks_for_course()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")


if __name__ == "main":
    main()