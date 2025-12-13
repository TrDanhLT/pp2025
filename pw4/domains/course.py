class Course:
def __init__(self, cid, name, credit):
self.__cid = cid
self.__name = name
self.__credit = credit


def get_id(self):
return self.__cid


def get_credit(self):
return self.__credit