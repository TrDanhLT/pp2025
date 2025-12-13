import curses




def curses_ui(stdscr, students):
curses.curs_set(0)
stdscr.clear()
stdscr.addstr(0, 2, "STUDENT GPA LIST", curses.A_BOLD)
row = 2
for s in students:
stdscr.addstr(row, 2, f"{s.get_id()} | {s.get_name()} | GPA: {s.calculate_gpa()}")
row += 1
stdscr.addstr(row + 1, 2, "Press any key to exit")
stdscr.refresh()
stdscr.getch()