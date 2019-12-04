import sys
import time

"""
made possible with ANSI escape codes
- Position the Cursor:
  \033[<L>;<C>H
     Or
  \033[<L>;<C>f
  puts the cursor at line L and column C.
- Move the cursor up N lines:
  \033[<N>A
- Move the cursor down N lines:
  \033[<N>B
- Move the cursor forward N columns:
  \033[<N>C
- Move the cursor backward N columns:
  \033[<N>D

- Clear the screen, move to (0,0):
  \033[2J
- Erase to end of line:
  \033[K

- Save cursor position:
  \033[s
- Restore cursor position:
  \033[u
"""
CURSOR_UP = '\033[F'

"""
Passwords
100 total | +56 unique | -10 duplicates | +/-34 remaining
					 reviewing 67 / 100
					(67% complete)
"""
for percentage in range(0, 100):
	sys.stdout.write('\r%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % (
								'\n\t\tPasswords:',' 67% complete',
								'\n',
								'100 total',
								' | ',
								'+', percentage, ' unique',
								' | ',
								'-', percentage, ' duplicates',
								' | ',
								'+/-', percentage, 'remaining',
								'\n\t\t', CURSOR_UP, CURSOR_UP, CURSOR_UP,
	))
	time.sleep(.5)	