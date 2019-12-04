import sys
import time

"""
Passwords
100 total | +56 unique | -10 duplicates | +/-34 remaining
					 reviewing 67 / 100
					(67% complete)
"""
sys.stdout.write('\nPasswords\n')
for percentage in range(0, 100):
	sys.stdout.write('\r%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('100 total',
								' | ',
								'+', percentage, ' unique',
								' | ',
								'-', percentage, 'duplicates',
								' | ',
								'+/-', percentage, 'remaining',
	))
	sys.stdout.flush()
	time.sleep(.5)	