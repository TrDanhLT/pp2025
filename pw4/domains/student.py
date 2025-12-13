import math
import numpy as np


class Student:
def __init__(self, sid, name, dob):
self.__id = sid
self.__name = name
self.__dob = dob
self.__courses = [] # (credit, mark)


def get_id(self):
return self.__id


def get_name(self):
return self.__name


def add_course_mark(self, credit, mark):
mark = math.floor(mark * 10) / 10
self.__courses.append((credit, mark))


def calculate_gpa(self):
if not self.__courses:
return 0.0
credits = np.array([c[0] for c in self.__courses])
marks = np.array([c[1] for c in self.__courses])
return round((credits * marks).sum() / credits.sum(), 2)import math
import numpy as np


class Student:
def __init__(self, sid, name, dob):
self.__id = sid
self.__name = name
self.__dob = dob
self.__courses = [] # (credit, mark)


def get_id(self):
return self.__id


def get_name(self):
return self.__name


def add_course_mark(self, credit, mark):
mark = math.floor(mark * 10) / 10
self.__courses.append((credit, mark))


def calculate_gpa(self):
if not self.__courses:
return 0.0
credits = np.array([c[0] for c in self.__courses])
marks = np.array([c[1] for c in self.__courses])
return round((credits * marks).sum() / credits.sum(), 2)