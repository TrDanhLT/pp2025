import curses
from domains.mark_system import MarkSystem
import input as inp
import output




def main():
system = MarkSystem()
inp.input_students(system)
inp.input_courses(system)
inp.input_marks(system)
system.sort_by_gpa()
curses.wrapper(output.curses_ui, system.students)




if __name__ == "__main__":
main()