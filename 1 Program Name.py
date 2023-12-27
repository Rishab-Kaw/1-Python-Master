import curses

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # Print a string at the top of the screen
    stdscr.addstr("Curses programming in Python")

    # Refresh the screen to show the changes
    stdscr.refresh()

    # Wait for user input
    stdscr.getkey()

curses.wrapper(main)
