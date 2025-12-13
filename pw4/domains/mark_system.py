from domains.student import Student
from domains.course import Course


class MarkSystem:
def __init__(self):
self.students = []
self.courses = []


def add_student(self, sid, name, dob):
self.students.append(Student(sid, name, dob))


def add_course(self, cid, name, credit):
self.courses.append(Course(cid, name, credit))


def find_course(self, cid):
for c in self.courses:
if c.get_id() == cid:
return c
return None


def sort_by_gpa(self):
self.students.sort(key=lambda s: s.calculate_gpa(), reverse=True)