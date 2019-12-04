import sys
import time

for percentage in range(0, 100):
    sys.stdout.write("\r[%s]" % ('=' * percentage))
    sys.stdout.flush()
    time.sleep(.05)